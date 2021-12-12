from abc import ABC, abstractmethod
from typing import List
from entities.manager import Manager


class ManagerDAO(ABC):
    # for login purposes
    @abstractmethod
    def get_manager_by_username(self, user_name: str) -> Manager:
        pass
