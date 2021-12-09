from abc import ABC, abstractmethod

from entities.employee import Employee


class EmployeeDAO(ABC):
    @abstractmethod
    def create_new_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        pass
