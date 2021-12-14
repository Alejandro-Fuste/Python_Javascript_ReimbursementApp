from typing import List

from custom_exceptions.invalid_credentials_exception import InvalidCredentialsException
from data_access_layer.implementation_classes.manager_postgres_dao_imp import ManagerPostgresDAO
from entities.manager import Manager
from service_layer.abstract_services.manager_service import ManagerService


class ManagerPostgresServiceImp(ManagerService):
    def __init__(self, manager_dao: ManagerPostgresDAO):
        self.manager_dao = manager_dao

    def service_validate_manager(self, user_name: str, password: str) -> Manager:
        manager = self.manager_dao.get_manager_by_username(user_name)
        if manager.user_name == user_name:
            if manager.user_password == password:
                return manager
        raise InvalidCredentialsException("The provided credentials are invalid.")

    def get_all_managers(self) -> List[Manager]:
        return self.manager_dao.get_all_managers()
