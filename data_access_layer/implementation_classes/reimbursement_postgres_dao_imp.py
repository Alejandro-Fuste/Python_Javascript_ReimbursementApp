from typing import List

from data_access_layer.abstract_classes.reimbursement_dao import ReimbursementDAO
from entities.reimbursement import Reimbursement
from utils.database_connection import connection


class ReimbursementPostgresDAO(ReimbursementDAO):
    def create_new_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        # sql =
        pass

    def get_all_reimbursement_requests(self) -> List[Reimbursement]:
        pass

    def get_reimbursements_by_employee_id(self, employee_id: int) -> List[Reimbursement]:
        pass

    def update_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    def get_total_reimbursements_amount(self) -> float:
        pass

    def get_total_reimbursements_amount_by_employee(self) -> float:
        pass

    def get_total_reimbursements_amount_by_month(self) -> float:
        pass

    def get_total_reimbursements_amount_by_category(self) -> float:
        pass

    def get_top_five_highest_amounts(self) -> List[Reimbursement]:
        pass
