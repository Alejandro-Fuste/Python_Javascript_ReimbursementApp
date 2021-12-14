from custom_exceptions.employee_not_found_exception import EmployeeNotFoundException
from custom_exceptions.duplicate_reimbursement_exception import DuplicateReimbursementException
from data_access_layer.implementation_classes.reimbursement_postgres_dao_imp import ReimbursementPostgresDAO
from entities.reimbursement import Reimbursement
from service_layer.implementation_services.reimbursement_postgres_service import ReimbursementPostgresServiceImp

reimbursement_dao = ReimbursementPostgresDAO()
reimbursement_service = ReimbursementPostgresServiceImp(reimbursement_dao)

duplicate_reimbursement = Reimbursement(1, 20.00, 'Gas', 'Travel gas', '12-9-2021', 'pending', 'null', 'null',
                                        1, 1)


def test_catch_duplicate_reimbursement_request():
    try:
        reimbursement_service.service_create_new_reimbursement_request(duplicate_reimbursement)
        assert False
    except DuplicateReimbursementException as e:
        assert str(e) == "This reimbursement has already been created."


def test_catch_get_reimbursements_by_employee_id_request():
    try:
        reimbursement_service.service_get_reimbursements_by_employee_id(100)
        assert False
    except EmployeeNotFoundException as e:
        assert str(e) == "This reimbursement was not found."
