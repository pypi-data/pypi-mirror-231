import logging
from datetime import datetime
from dateutil.rrule import rrule, MONTHLY

from spaceone.core.manager import BaseManager
from spaceone.cost_analysis.manager.identity_manager import IdentityManager
from spaceone.cost_analysis.manager.cost_manager import CostManager
from spaceone.cost_analysis.manager.budget_manager import BudgetManager
from spaceone.cost_analysis.model.budget_usage_model import BudgetUsage
from spaceone.cost_analysis.model.budget_model import Budget

_LOGGER = logging.getLogger(__name__)


class BudgetUsageManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.budget_mgr: BudgetManager = self.locator.get_manager('BudgetManager')
        self.budget_usage_model: BudgetUsage = self.locator.get_model('BudgetUsage')

    def create_budget_usages(self, budget_vo: Budget):
        if budget_vo.time_unit == 'TOTAL':
            start_dt = datetime.strptime(budget_vo.start, '%Y-%m')
            end_dt = datetime.strptime(budget_vo.end, '%Y-%m')

            dts = [dt for dt in rrule(MONTHLY, dtstart=start_dt, until=end_dt)]
            limit_per_month = round(budget_vo.limit / len(dts), 3)

            for dt in dts:
                budget_usage_data = {
                    'budget_id': budget_vo.budget_id,
                    'name': budget_vo.name,
                    'date': dt.strftime("%Y-%m"),
                    'cost': 0,
                    'limit': limit_per_month,
                    'currency': budget_vo.currency,
                    'provider_filter': budget_vo.provider_filter.to_dict(),
                    'budget': budget_vo,
                    'project_id': budget_vo.project_id,
                    'project_group_id': budget_vo.project_group_id,
                    'data_source_id': budget_vo.data_source_id,
                    'domain_id': budget_vo.domain_id
                }

                self.budget_usage_model.create(budget_usage_data)

        else:
            for planned_limit in budget_vo.planned_limits:
                budget_usage_data = {
                    'budget_id': budget_vo.budget_id,
                    'name': budget_vo.name,
                    'date': planned_limit['date'],
                    'cost': 0,
                    'limit': planned_limit.limit,
                    'currency': budget_vo.currency,
                    'provider_filter': budget_vo.provider_filter.to_dict(),
                    'budget': budget_vo,
                    'project_id': budget_vo.project_id,
                    'project_group_id': budget_vo.project_group_id,
                    'data_source_id': budget_vo.data_source_id,
                    'domain_id': budget_vo.domain_id
                }

                self.budget_usage_model.create(budget_usage_data)

    def update_budget_usage_by_vo(self, params, budget_usage_vo):
        def _rollback(old_data):
            _LOGGER.info(f'[update_budget_usage_by_vo._rollback] Revert Data : '
                         f'{old_data["budget_id"]} / {old_data["date"]}')
            budget_usage_vo.update(old_data)

        self.transaction.add_rollback(_rollback, budget_usage_vo.to_dict())
        return budget_usage_vo.update(params)

    def update_cost_usage(self, budget_id, domain_id):
        _LOGGER.info(f'[update_cost_usage] Update Budget Usage: {budget_id}')
        cost_mgr: CostManager = self.locator.get_manager('CostManager')

        budget_vo = self.budget_mgr.get_budget(budget_id, domain_id)
        self._update_monthly_budget_usage(budget_vo, cost_mgr)

    def update_budget_usage(self, domain_id, data_source_id):
        budget_vos = self.budget_mgr.filter_budgets(domain_id=domain_id, data_source_id=data_source_id)
        for budget_vo in budget_vos:
            self.update_cost_usage(budget_vo.budget_id, domain_id)

    def filter_budget_usages(self, **conditions):
        return self.budget_usage_model.filter(**conditions)

    def list_budget_usages(self, query={}):
        return self.budget_usage_model.query(**query)

    def stat_budget_usages(self, query):
        return self.budget_usage_model.stat(**query)

    def analyze_budget_usages(self, query):
        query['date_field'] = 'date'
        query['date_field_format'] = '%Y-%m'
        return self.budget_usage_model.analyze(**query)

    def _update_monthly_budget_usage(self, budget_vo: Budget, cost_mgr: CostManager):
        update_data = {}
        query = self._make_cost_analyze_query(budget_vo)
        _LOGGER.debug(f'[_update_monthly_budget_usage]: query: {query}')

        result = cost_mgr.analyze_costs_by_granularity(query, budget_vo.domain_id, budget_vo.data_source_id)
        for cost_usage_data in result.get('results', []):
            if date := cost_usage_data.get('date'):
                update_data[date] = cost_usage_data.get('cost', 0)

        budget_usage_vos = self.budget_usage_model.filter(budget_id=budget_vo.budget_id)
        for budget_usage_vo in budget_usage_vos:
            if budget_usage_vo.date in update_data:
                budget_usage_vo.update({'cost': update_data[budget_usage_vo.date]})
            else:
                budget_usage_vo.update({'cost': 0})

    def _make_cost_analyze_query(self, budget_vo: Budget):
        query = {
            'granularity': 'MONTHLY',
            'start': budget_vo.start,
            'end': budget_vo.end,
            'fields': {
                'cost': {
                    'key': 'cost',
                    'operator': 'sum'
                }
            },
            'filter': [
                {'k': 'domain_id', 'v': budget_vo.domain_id, 'o': 'eq'},
                {'k': 'data_source_id', 'v': budget_vo.data_source_id, 'o': 'eq'},
            ]
        }

        if budget_vo.project_id:
            query['filter'].append({'k': 'project_id', 'v': budget_vo.project_id, 'o': 'eq'})

        else:
            identity_mgr: IdentityManager = self.locator.get_manager('IdentityManager')
            response = identity_mgr.list_projects_in_project_group(budget_vo.project_group_id,
                                                                   budget_vo.domain_id, True)

            project_ids = []
            for project_info in response.get('results', []):
                project_ids.append(project_info['project_id'])

            query['filter'].append({'k': 'project_id', 'v': project_ids, 'o': 'in'})

        if budget_vo.provider_filter and budget_vo.provider_filter.state == 'ENABLED':
            query['filter'].append({'k': 'provider', 'v': budget_vo.provider_filter.providers, 'o': 'in'})

        return query
