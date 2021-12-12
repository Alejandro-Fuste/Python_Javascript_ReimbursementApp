from abc import ABC, abstractmethod
from typing import List
from entities.employee import Employee


class EmployeeDAO(ABC):
    # for login purposes
    @abstractmethod
    def get_employee_by_username(self, user_name: str) -> Employee:
        pass
