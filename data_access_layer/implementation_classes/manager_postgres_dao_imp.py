from data_access_layer.abstract_classes.manager_dao import ManagerDAO
from entities.manager import Manager
from utils.database_connection import connection


class ManagerPostgresDAO(ManagerDAO):
    def get_manager_by_username(self, user_name: str) -> Manager:
        pass
