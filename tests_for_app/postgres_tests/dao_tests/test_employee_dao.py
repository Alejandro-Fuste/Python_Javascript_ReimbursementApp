from data_access_layer.implementation_classes.employee_postgres_dao_imp import EmployeePostgresDAO
from entities.employee import Employee

employee_dao = EmployeePostgresDAO()

def test_get_employee_by_username():
