from custom_exceptions.duplicate_reimbursement_exception import DuplicateReimbursementException
from custom_exceptions.employee_not_found_exception import EmployeeNotFoundException
from data_access_layer.implementation_classes.reimbursement_postgres_dao_imp import ReimbursementPostgresDAO
from entities.reimbursement import Reimbursement
from service_layer.abstract_services.reimbursement_service import ReimbursementService
from typing import List


class ReimbursementPostgresServiceImp(ReimbursementService):
    def __init__(self, reimbursement_dao: ReimbursementPostgresDAO):
        self.reimbursement_dao = reimbursement_dao

    def service_create_new_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        reimbursements = self.reimbursement_dao.get_all_reimbursement_requests()
        for current_reimbursement in reimbursements:
            if current_reimbursement.decision_date == reimbursement.decision_date:
                raise DuplicateReimbursementException("This reimbursement has already been created.")
        created_reimbursement = self.reimbursement_dao.create_new_reimbursement_request(reimbursement)
        return created_reimbursement

    def service_get_all_reimbursement_requests(self) -> List[Reimbursement]:
        return self.reimbursement_dao.get_all_reimbursement_requests()

    def service_get_reimbursements_by_employee_id(self, employee_id: int) -> List[Reimbursement]:
        reimbursements = self.reimbursement_dao.get_all_reimbursement_requests()
        for current_reimbursement in reimbursements:
            if current_reimbursement.employee_id == employee_id:
                return self.reimbursement_dao.get_reimbursements_by_employee_id(employee_id)
            raise EmployeeNotFoundException("This reimbursement was not found.")

    def service_update_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    def service_get_total_reimbursements_amount(self) -> float:
        pass

    def service_get_total_reimbursements_amount_by_employee(self, employee_id: int) -> float:
        pass

    def service_get_total_reimbursements_amount_by_month(self, begin_date: str, end_date: str) -> float:
        pass

    def service_get_total_reimbursements_amount_by_category(self, category: str) -> float:
        pass

    def service_get_top_five_highest_amounts(self) -> List[Reimbursement]:
        pass
