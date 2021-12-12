from data_access_layer.implementation_classes.reimbursement_postgres_dao_imp import ReimbursementPostgresDAO
from entities.reimbursement import Reimbursement

reimbursement_dao = ReimbursementPostgresDAO()
reimbursement: Reimbursement = Reimbursement(0, 20.00, 'Gas', 'Travel gas', '12-9-2021', 'pending', 'null',
                                             'null', 'Rey', 'Skywalker', 'Luke', 'Skywalker')

updated_reimbursement = Reimbursement(0, 100.00, 'Gas', 'Travel gas', '12-9-2021', 'pending', 'null',
                                             'null', 'Rey', 'Skywalker', 'Luke', 'Skywalker')

def test_create_new_reimbursement_request():
    create_reimbursement = reimbursement_dao.create_new_reimbursement_request(reimbursement)
    assert create_reimbursement.reimbursement_id != 0

def test_get_all_reimbursement_requests():
    reimbursements = reimbursement_dao.get_all_reimbursement_requests()
    assert len(reimbursements) > 2

def test_get_reimbursements_by_employee_id():
    employee_reimbursements = reimbursement_dao.get_reimbursements_by_employee_id(1)
    assert len(employee_reimbursements) > 1

def test_update_reimbursement_request():
    updated_request = reimbursement_dao.update_reimbursement_request(updated_reimbursement)
    assert updated_request.employee_last_name == updated_reimbursement.employee_last_name

def test_

    assert

def test_

    assert

def test_

    assert

def test_

    assert

def test_

    assert

