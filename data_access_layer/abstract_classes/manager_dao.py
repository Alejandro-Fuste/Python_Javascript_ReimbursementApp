from abc import ABC, abstractmethod
from typing import List
from entities.manager import Manager


class EmployeeDAO(ABC):
    # for login purposes
    @abstractmethod
    def get_manager_by_username(self) -> Manager:
        pass
