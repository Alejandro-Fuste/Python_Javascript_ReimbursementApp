from abc import ABC, abstractmethod
from entities.employee import Employee


class EmployeeService(ABC):
    # for login purposes
    @abstractmethod
    def get_employee_by_username(self, user_name: str) -> Employee:
        pass
    