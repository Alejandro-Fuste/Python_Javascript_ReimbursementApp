from data_access_layer.abstract_classes.employee_dao import EmployeeDAO
from entities.employee import Employee
from utils.database_connection import connection


class EmployeePostgresDAO(EmployeeDAO):
    def get_employee_by_username(self, user_name: str) -> Employee:
        pass
