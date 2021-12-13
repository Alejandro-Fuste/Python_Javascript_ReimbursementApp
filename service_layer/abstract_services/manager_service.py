from abc import ABC, abstractmethod
from typing import List

from entities.manager import Manager


class ManagerService(ABC):
    # for login purposes
    @abstractmethod
    def service_get_manager_by_username(self, user_name: str) -> Manager:
        pass

    @abstractmethod
    def get_all_managers(self) -> List[Manager]:
        pass
