from abc import ABC, abstractmethod
from entities.manager import Manager


class ManagerService(ABC):
    # for login purposes
    @abstractmethod
    def service_get_manager_by_username(self, user_name: str) -> Manager:
        pass
