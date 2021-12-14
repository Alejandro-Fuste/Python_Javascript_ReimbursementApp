from custom_exceptions.invalid_credentials_exception import InvalidCredentialsException
from data_access_layer.implementation_classes.employee_postgres_dao_imp import EmployeePostgresDAO
from entities.employee import Employee
from service_layer.abstract_services.employee_service import EmployeeService


class EmployeePostgresServiceImp(EmployeeService):
    def __init__(self, employee_dao: EmployeePostgresDAO):
        self.employee_dao = employee_dao

    def service_get_employee_by_username(self, user_name: str) -> Employee:
        pass

    def get_all_employees(self):
        pass
