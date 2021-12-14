from abc import ABC, abstractmethod
from entities.employee import Employee


class EmployeeService(ABC):
    # for login purposes
    @abstractmethod
    def service_validate_employee(self, user_name: str, password: str) -> Employee:
        pass

    @abstractmethod
    def service_get_all_employees(self):
        pass
