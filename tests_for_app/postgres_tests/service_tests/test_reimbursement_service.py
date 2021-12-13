from data_access_layer.implementation_classes.reimbursement_postgres_dao_imp import ReimbursementPostgresDAO
from entities.reimbursement import Reimbursement
from service_layer.implementation_services.reimbursement_postgres_service import ReimbursementPostgresServiceImp

reimbursement_dao = ReimbursementPostgresDAO()
reimbursement_service = ReimbursementPostgresServiceImp(reimbursement_dao)

duplicate_reimbursement = Reimbursement(1, 20.00, 'Gas', 'Travel gas', '12-9-2021', 'pending', 'null', 'null',
                                        'Rey', 'Skywalker', 'Luke', 'Skywalker')

def test_catch_duplicate_reimbursement_request():
    try:
        reimbursement_service.service_create_new_reimbursement_request(duplicate_reimbursement)
        assert False
    except