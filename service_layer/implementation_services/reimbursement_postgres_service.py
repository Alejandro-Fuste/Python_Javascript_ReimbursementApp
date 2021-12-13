from data_access_layer.implementation_classes.reimbursement_postgres_dao_imp import ReimbursementPostgresDAO
from entities.reimbursement import Reimbursement
from service_layer.abstract_services.reimbursement_service import ReimbursementService
from typing import List


class ReimbursementPostgresServiceImp(ReimbursementService):
    def __init__(self, reimbursement_dao: ReimbursementPostgresDAO):
        self.reimbursement_dao = reimbursement_dao

    def service_create_new_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    def service_get_all_reimbursement_requests(self) -> List[Reimbursement]:
        pass

    def service_get_reimbursements_by_employee_id(self, employee_id: int) -> List[Reimbursement]:
        pass

    def service_update_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    def service_get_total_reimbursements_amount(self) -> float:
        pass

    def service_get_total_reimbursements_amount_by_employee(self) -> float:
        pass

    def service_get_total_reimbursements_amount_by_month(self) -> float:
        pass

    def service_get_total_reimbursements_amount_by_category(self) -> float:
        pass

    def service_get_top_five_highest_amounts(self) -> List[Reimbursement]:
        pass
