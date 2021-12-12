from abc import ABC, abstractmethod
from typing import List

from entities.reimbursement import Reimbursement


class ReimbursementDAO(ABC):
    # for employees to create new request
    @abstractmethod
    def create_new_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    # so manager can view approved, denied, and pending reimbursements
    @abstractmethod
    def get_all_reimbursement_requests(self) -> List[Reimbursement]:
        pass

    # to view all the employees reimbursements
    @abstractmethod
    def get_reimbursements_by_employee_id(self, employee_id: int) -> List[Reimbursement]:
        pass

    # for manager to approve/deny and leave comments
    @abstractmethod
    def update_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    # get statistics
    @abstractmethod
    def get_total_reimbursements_amount(self) -> float:
        pass

    @abstractmethod
    def get_total_reimbursements_amount_by_employee(self) -> float:
        pass

    @abstractmethod
    def get_total_reimbursements_amount_by_month(self) -> float:
        pass

    @abstractmethod
    def get_total_reimbursements_amount_by_category(self) -> float:
        pass

    @abstractmethod
    def get_top_five_highest_amounts(self) -> List[Reimbursement]:
        pass


