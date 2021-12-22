from typing import List

from custom_exceptions.invalid_credentials_exception import InvalidCredentialsException
from data_access_layer.implementation_classes.manager_postgres_dao_imp import ManagerPostgresDAO
from entities.manager import Manager
from service_layer.abstract_services.manager_service import ManagerService


class ManagerPostgresServiceImp(ManagerService):
    def __init__(self, manager_dao: ManagerPostgresDAO):
        self.manager_dao = manager_dao

    def service_validate_manager(self, user_name: str, password: str) -> Manager:
        managers = self.manager_dao.get_all_managers()
        for current_manager in managers:
            if current_manager.user_name == user_name:
                if current_manager.user_password == password:
                    return current_manager
            raise InvalidCredentialsException("The provided credentials are invalid.")

    def service_get_all_managers(self) -> List[Manager]:
        return self.manager_dao.get_all_managers()
