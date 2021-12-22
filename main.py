from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import logging

from custom_exceptions.employee_not_found_exception import EmployeeNotFoundException
from custom_exceptions.invalid_credentials_exception import InvalidCredentialsException
from custom_exceptions.duplicate_reimbursement_exception import DuplicateReimbursementException

from data_access_layer.implementation_classes.category_postgres_dao_imp import CategoryPostgresDao
from data_access_layer.implementation_classes.employee_postgres_dao_imp import EmployeePostgresDAO
from data_access_layer.implementation_classes.manager_postgres_dao_imp import ManagerPostgresDAO
from data_access_layer.implementation_classes.reimbursement_postgres_dao_imp import ReimbursementPostgresDAO

from entities.reimbursement import Reimbursement

from service_layer.implementation_services.category_postgres_service import CategoryPostgresServiceImp
from service_layer.implementation_services.employee_postgres_service import EmployeePostgresServiceImp
from service_layer.implementation_services.manager_postgres_service import ManagerPostgresServiceImp
from service_layer.implementation_services.reimbursement_postgres_service import ReimbursementPostgresServiceImp

category_dao = CategoryPostgresDao()
category_service = CategoryPostgresServiceImp(category_dao)
employee_dao = EmployeePostgresDAO()
employee_service = EmployeePostgresServiceImp(employee_dao)
manager_dao = ManagerPostgresDAO()
manager_service = ManagerPostgresServiceImp(manager_dao)
reimbursement_dao = ReimbursementPostgresDAO()
reimbursement_service = ReimbursementPostgresServiceImp(reimbursement_dao)

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


# post to validate employee
@app.post("/employee")
@cross_origin()
def validate_employee():
    try:
        employee_data = request.get_json()
        user_name = employee_data['userName']
        user_password = employee_data['userPassword']
        employee_to_return = employee_service.service_validate_employee(user_name, user_password)
        employee_as_dictionary = employee_to_return.return_employee_credentials()
        employee_as_json = jsonify(employee_as_dictionary)
        return employee_as_json, 200
    except InvalidCredentialsException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400


# post to validate manager
@app.post("/manager")
def validate_manager():
    try:
        manager_data = request.get_json()
        user_name = manager_data['userName']
        user_password = manager_data['userPassword']
        manager_to_return = manager_service.service_validate_manager(user_name, user_password)
        manager_as_dictionary = manager_to_return.return_manager_credentials()
        manager_as_json = jsonify(manager_as_dictionary)
        return manager_as_json, 200
    except InvalidCredentialsException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400


# Create new reimbursement
@app.post("/reimbursement")
def create_reimbursement():
    try:
        reimbursement_data = request.get_json()
        new_reimbursement = Reimbursement(
            reimbursement_data['reimbursementId'],
            float(reimbursement_data['reimbursementAmount']),
            reimbursement_data['category'],
            reimbursement_data['reimbursementReason'],
            reimbursement_data['reimbursementDate'],
            reimbursement_data['status'],
            reimbursement_data['decisionDate'],
            reimbursement_data['reason'],
            reimbursement_data['employeeId'],
            reimbursement_data['managerId']
        )
        reimbursement_to_return = reimbursement_service.service_create_new_reimbursement_request(new_reimbursement)
        reimbursement_as_dictionary = reimbursement_to_return.make_reimbursement_dictionary()
        reimbursement_as_json = jsonify(reimbursement_as_dictionary)
        return reimbursement_as_json, 201
    except DuplicateReimbursementException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400


# get all categories route
@app.get("/categories")
def get_all_categories():
    categories = category_service.service_get_all_categories()
    categories_as_dictionary = []
    for category in categories:
        dictionary_categories = category.make_category_dictionary()
        categories_as_dictionary.append(dictionary_categories)
    return jsonify(categories_as_dictionary), 200


# get all employees
@app.get("/employees")
def get_all_employees():
    employees = employee_service.service_get_all_employees()
    employees_as_dictionary = []
    for employee in employees:
        dictionary_employees = employee.make_employee_dictionary()
        employees_as_dictionary.append(dictionary_employees)
    return jsonify(employees_as_dictionary), 200


# get all managers
@app.get("/managers")
def get_all_managers():
    managers = manager_service.service_get_all_managers()
    managers_as_dictionary = []
    for manager in managers:
        dictionary_managers = manager.make_manager_dictionary()
        managers_as_dictionary.append(dictionary_managers)
    return jsonify(managers_as_dictionary), 200


# get all reimbursements
@app.get("/reimbursements/all")
def get_all_reimbursements():
    reimbursements = reimbursement_service.service_get_all_reimbursement_requests()
    reimbursements_as_dictionary = []
    for reimbursement in reimbursements:
        dictionary_reimbursements = reimbursement.make_reimbursement_dictionary()
        reimbursements_as_dictionary.append(dictionary_reimbursements)
    return jsonify(reimbursements_as_dictionary), 200


# get all reimbursements by employee id
@app.get("/reimbursements/<employee_id>")
def get_all_employee_reimbursements(employee_id: str):
    try:
        reimbursements = reimbursement_service.service_get_reimbursements_by_employee_id(int(employee_id))
        reimbursements_as_dictionary = []
        for reimbursement in reimbursements:
            dictionary_reimbursements = reimbursement.make_reimbursement_dictionary()
            reimbursements_as_dictionary.append(dictionary_reimbursements)
        return jsonify(reimbursements_as_dictionary), 200
    except EmployeeNotFoundException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400


# get total reimbursements amount
@app.get("/reimbursements/total")
def get_total_reimbursement():
    amount = reimbursement_service.service_get_total_reimbursements_amount()
    amount_dictionary = {"total": amount}
    return jsonify(amount_dictionary), 200


# get list of rejected reimbursements
@app.get('/reimbursements/rejected')
def get_total_rejected_reimbursement():
    amount = reimbursement_service.service_get_total_reject_reimbursements_amount()
    amount_dictionary = {"total": amount}
    return jsonify(amount_dictionary), 200


# get total reimbursements amount by employee
@app.get("/reimbursements/total/<employee_id>")
def get_total_reimbursements_amount_by_employee(employee_id: str):
    try:
        amount = reimbursement_service.service_get_total_reimbursements_amount_by_employee(int(employee_id))
        amount_dictionary = {"total": amount}
        return jsonify(amount_dictionary), 200
    except EmployeeNotFoundException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400


# get total reimbursements amount by category
@app.get("/reimbursements/total/category/<category>")
def get_total_reimbursement_by_category(category: str):
    amount = reimbursement_service.service_get_total_reimbursements_amount_by_category(category)
    amount_dictionary = {"total": amount}
    return jsonify(amount_dictionary), 200


# get list of the top five highest reimbursements
@app.get('/reimbursements/topFive')
def get_top_five_highest_amounts():
    reimbursements = reimbursement_service.service_get_top_five_highest_amounts()
    reimbursements_as_dictionary = []
    for reimbursement in reimbursements:
        dictionary_reimbursements = reimbursement.make_reimbursement_dictionary()
        reimbursements_as_dictionary.append(dictionary_reimbursements)
    return jsonify(reimbursements_as_dictionary), 200


# update an employee's reimbursement
@app.patch("/reimbursements")
def update_employee_reimbursement():
    try:
        reimbursement_data = request.get_json()
        update_reimbursement = Reimbursement(
            int(reimbursement_data['reimbursementId']),
            float(reimbursement_data['reimbursementAmount']),
            reimbursement_data['category'],
            reimbursement_data['reimbursementReason'],
            reimbursement_data['reimbursementDate'],
            reimbursement_data['status'],
            reimbursement_data['decisionDate'],
            reimbursement_data['reason'],
            int(reimbursement_data['employeeId']),
            int(reimbursement_data['managerId'])
        )
        updated_reimbursement = reimbursement_service.service_update_reimbursement_request(update_reimbursement)
        return jsonify("Reimbursement was updated successfully."), 200
    except EmployeeNotFoundException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json, 400


app.run()
