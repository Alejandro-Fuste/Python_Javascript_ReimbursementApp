from abc import ABC, abstractmethod
from typing import List

from entities.reimbursement import Reimbursement


class ReimbursementService(ABC):
    # for employees to create new request
    @abstractmethod
    def service_create_new_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    # so manager can view approved, denied, and pending reimbursements
    @abstractmethod
    def service_get_all_reimbursement_requests(self) -> List[Reimbursement]:
        pass

    # to view all the employees reimbursements
    @abstractmethod
    def service_get_reimbursements_by_employee_id(self, employee_id: int) -> List[Reimbursement]:
        pass

    # for manager to approve/deny and leave comments
    @abstractmethod
    def service_update_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    # get statistics
    @abstractmethod
    def service_get_total_reimbursements_amount(self) -> float:
        pass

    @abstractmethod
    def get_rejected_reimbursements(self) -> List[Reimbursement]:
        pass

    @abstractmethod
    def service_get_total_reimbursements_amount_by_employee(self, employee_id: int) -> float:
        pass

    @abstractmethod
    def service_get_total_reimbursements_amount_by_category(self, category: str) -> float:
        pass

    @abstractmethod
    def service_get_top_five_highest_amounts(self) -> List[Reimbursement]:
        pass

    # @abstractmethod
    # def service_get_total_reimbursements_amount_by_month(self, begin_date: str, end_date: str) -> float:
    #     pass
