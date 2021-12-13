from typing import List

from data_access_layer.abstract_classes.reimbursement_dao import ReimbursementDAO
from entities.reimbursement import Reimbursement
from utils.database_connection import connection


class ReimbursementPostgresDAO(ReimbursementDAO):
    def create_new_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = 'insert into "python_reimbursement".reimbursement values (default, ' \
              '%s, %s, %s, %s, %s, %s, %s, %s, %s) returning reimbursement_id'
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.reimbursement_amount, reimbursement.category,
                             reimbursement.reimbursement_reason, reimbursement.reimbursement_date, reimbursement.status,
                             reimbursement.decision_date, reimbursement.reason, reimbursement.employee_id,
                             reimbursement.manager_id))
        connection.commit()
        reimbursement_id = cursor.fetchone()[0]
        reimbursement.reimbursement_id = reimbursement_id
        return reimbursement

    def get_all_reimbursement_requests(self) -> List[Reimbursement]:
        sql = 'select * from "python_reimbursement".reimbursement'
        cursor = connection.cursor()
        cursor.execute(sql)
        reimbursement_records = cursor.fetchall()
        reimbursement_list = []
        for reimbursement in reimbursement_records:
            reimbursement_list.append(Reimbursement(*reimbursement))
        return reimbursement_list

    def get_reimbursements_by_employee_id(self, employee_id: int) -> List[Reimbursement]:
        sql = 'select * from "python_reimbursement".reimbursement where employee_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        employee_reimbursements = cursor.fetchall()
        reimbursement_list = []
        for reimbursement in employee_reimbursements:
            reimbursement_list.append(Reimbursement(*reimbursement))
        return reimbursement_list

    def update_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = 'update "python_reimbursement".reimbursement set status = %s, decision_date = %s, reason = %s ' \
              'where reimbursement_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.status, reimbursement.decision_date, reimbursement.reason,
                             reimbursement.reimbursement_id))
        connection.commit()
        return reimbursement

    def get_total_reimbursements_amount(self) -> float:
        sql = 'select sum(reimbursement_amount) from "python_reimbursement".reimbursement where status = "approved"'
        cursor = connection.cursor()
        cursor.execute(sql)
        total_amount = cursor.fetchone()
        return int(total_amount)

    def get_total_reimbursements_amount_by_employee(self, employee_id: int) -> float:
        sql = 'select sum(reimbursement_amount) from "python_reimbursement".reimbursement where employee_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        total_amount = cursor.fetchone()
        return int(total_amount)

    def get_total_reimbursements_amount_by_month(self, begin_date: str, end_date: str) -> float:
        sql = 'select sum(reimbursement_amount) from "python_reimbursement".reimbursement where decision_date >= %s ' \
              'and decision_date <= %s'
        cursor = connection.cursor()
        cursor.execute(sql, (begin_date, end_date))
        total_amount = cursor.fetchone()
        return int(total_amount)

    def get_total_reimbursements_amount_by_category(self, category: str) -> float:
        sql = 'select sum(reimbursement_amount) from "python_reimbursement".reimbursement where category = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [category])
        total_amount = cursor.fetchone()
        return int(total_amount)

    def get_top_five_highest_amounts(self) -> List[Reimbursement]:
        sql = 'select * from "python_reimbursement".reimbursement where status = "approved" order by ' \
              'reimbursement_amount desc limit 5'
        cursor = connection.cursor()
        cursor.execute(sql)
        reimbursement_records = cursor.fetchall()
        reimbursement_list = []
        for reimbursement in reimbursement_records:
            reimbursement_list.append(Reimbursement(*reimbursement))
        return reimbursement_list
    

