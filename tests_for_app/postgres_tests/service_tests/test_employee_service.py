from custom_exceptions.invalid_credentials_exception import InvalidCredentialsException
from data_access_layer.implementation_classes.employee_postgres_dao_imp import EmployeePostgresDAO

from service_layer.implementation_services.employee_postgres_service import EmployeePostgresServiceImp

employee_dao = EmployeePostgresDAO()
employee_service = EmployeePostgresServiceImp(employee_dao)

non_employee = 'anakin_skywalker'


def test_employee_validation():
    try:
        employee_service.service_get_employee_by_username(non_employee)
        assert False
    except InvalidCredentialsException as e:
        assert str(e) == "The provided credentials are invalid."
