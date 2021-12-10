from abc import ABC, abstractmethod
from typing import List
from entities.employee import Employee


class EmployeeDAO(ABC):
    # to view all the employees reimbursements
    @abstractmethod
    def get_all_reimbursements(self) -> List[Employee]:
        pass

    # for login purposes
    @abstractmethod
    def get_employee_by_username(self) -> Employee:
        pass
