from custom_exceptions.invalid_credentials_exception import InvalidCredentialsException
from data_access_layer.implementation_classes.manager_postgres_dao_imp import ManagerPostgresDAO
from service_layer.implementation_services.manager_postgres_service import ManagerPostgresServiceImp

manager_dao = ManagerPostgresDAO()
manager_service = ManagerPostgresServiceImp(manager_dao)

non_manager = 'anakin_skywalker'


def test_manager_not_found_for_get_manager_by_username():
    try:
        manager_service.service_get_manager_by_username(non_manager)
        assert False
    except InvalidCredentialsException as e:
        assert str(e) == "The provided credentials are invalid."
