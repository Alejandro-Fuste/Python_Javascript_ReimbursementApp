from custom_exceptions.invalid_credentials_exception import InvalidCredentialsException
from data_access_layer.implementation_classes.employee_postgres_dao_imp import EmployeePostgresDAO
from entities.employee import Employee
from service_layer.abstract_services.employee_service import EmployeeService


class EmployeePostgresServiceImp(EmployeeService):
    def __init__(self, employee_dao: EmployeePostgresDAO):
        self.employee_dao = employee_dao

    def service_get_employee_by_username(self, user_name: str):
        employees = self.employee_dao.get_all_employees()
        for current_employee in employees:
            if current_employee.user_name == user_name:
                return self.employee_dao.get_employee_by_username(user_name)
            raise InvalidCredentialsException("The provided credentials are invalid.")

    def service_validate_employee(self, user_name: str, password: str) -> Employee:
        employees = self.employee_dao.get_all_employees()
        for current_employee in employees:
            if current_employee.user_name == user_name:
                if current_employee.user_password == password:
                    return current_employee
        raise InvalidCredentialsException("The provided credentials are invalid.")

    def service_get_all_employees(self):
        return self.employee_dao.get_all_employees()
