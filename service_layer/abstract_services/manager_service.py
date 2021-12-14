from abc import ABC, abstractmethod
from typing import List

from entities.manager import Manager


class ManagerService(ABC):
    # for login purposes
    @abstractmethod
    def service_validate_manager(self, user_name: str, password: str) -> Manager:
        pass

    @abstractmethod
    def get_all_managers(self) -> List[Manager]:
        pass
