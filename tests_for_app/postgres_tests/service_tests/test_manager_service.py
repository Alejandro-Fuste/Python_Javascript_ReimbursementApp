from custom_exceptions.invalid_credentials_exception import InvalidCredentialsException
from data_access_layer.implementation_classes.manager_postgres_dao_imp import ManagerPostgresDAO
from service_layer.implementation_services.manager_postgres_service import ManagerPostgresServiceImp

manager_dao = ManagerPostgresDAO()
manager_service = ManagerPostgresServiceImp(manager_dao)

non_manager_username = 'anakin_skywalker'
non_manager_password = 'darkside'


def test_manager_validation():
    try:
        manager_service.service_validate_manager(non_manager_username, non_manager_password)
        assert False
    except InvalidCredentialsException as e:
        assert str(e) == "The provided credentials are invalid."
