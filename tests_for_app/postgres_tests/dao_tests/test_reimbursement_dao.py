from data_access_layer.implementation_classes.reimbursement_postgres_dao_imp import ReimbursementPostgresDAO
from entities.reimbursement import Reimbursement

reimbursement_dao = ReimbursementPostgresDAO()
reimbursement: Reimbursement = Reimbursement(0, 20.00, 'Gas', 'Travel gas', '12-9-2021', 'pending', 'null',
                                             'null', 1, 1)

updated_reimbursement = Reimbursement(0, 100.00, 'Gas', 'Travel gas', '12-9-2021', 'pending', 'null',
                                      'null', 1, 1)
begin_date = '12-1-2021'
end_date = '12-31-2021'
category = 'Gas'


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
    assert updated_request.employee_id == updated_reimbursement.employee_id


def test_get_total_reimbursements_amount():
    total = reimbursement_dao.get_total_reimbursements_amount()
    assert total > 0


def test_get_total_reimbursements_amount_by_employee():
    employee_total = reimbursement_dao.get_total_reimbursements_amount_by_employee(1)
    assert employee_total > 0


def test_get_total_reimbursements_amount_by_month():
    monthly_total = reimbursement_dao.get_total_reimbursements_amount_by_month(begin_date, end_date)
    assert monthly_total > 0


def test_get_total_reimbursements_amount_by_category():
    category_total = reimbursement_dao.get_total_reimbursements_amount_by_category(category)
    assert category_total > 0


def test_get_top_five_highest_amounts():
    amounts = reimbursement_dao.get_top_five_highest_amounts()
    assert len(amounts) > 4
