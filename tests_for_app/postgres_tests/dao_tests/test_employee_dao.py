from data_access_layer.implementation_classes.employee_postgres_dao_imp import EmployeePostgresDAO
from entities.employee import Employee

employee_dao = EmployeePostgresDAO()

sample_user_name = 'Master Jedi'


def test_get_employee_by_username():
    user = employee_dao.get_employee_by_username(sample_user_name)
    assert user.user_name == sample_user_name
