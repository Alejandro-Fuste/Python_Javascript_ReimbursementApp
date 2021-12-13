from data_access_layer.implementation_classes.manager_postgres_dao_imp import ManagerPostgresDAO


manager_dao = ManagerPostgresDAO()

sample_manager = 'Master Jedi'


def test_get_employee_by_username():
    manager = manager_dao.get_manager_by_username(sample_manager)
    assert manager.user_name == sample_manager


def test_get_all_managers():
    managers = manager_dao.get_all_managers()
    assert len(managers) > 0
