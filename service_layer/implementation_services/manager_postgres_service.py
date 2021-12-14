from typing import List

from data_access_layer.implementation_classes.manager_postgres_dao_imp import ManagerPostgresDAO
from entities.manager import Manager
from service_layer.abstract_services.manager_service import ManagerService


class ManagerPostgresServiceImp(ManagerService):
    def __init__(self, manager_dao: ManagerPostgresDAO):
        self.manager_dao = manager_dao

    def service_get_manager_by_username(self, user_name: str) -> Manager:
        pass

    def get_all_managers(self) -> List[Manager]:
        return self.manager_dao.get_all_managers()
