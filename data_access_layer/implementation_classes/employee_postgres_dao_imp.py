from data_access_layer.abstract_classes.employee_dao import EmployeeDAO
from entities.employee import Employee
from utils.database_connection import connection


class EmployeePostgresDAO(EmployeeDAO):
    def get_employee_by_username(self, user_name: str) -> Employee:
        sql = 'select * from "python_reimbursement".employee where user_name = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [user_name])
        employee_record = cursor.fetchone()
        employee = Employee(*employee_record)
        return employee

    def get_all_employees(self):
        pass
