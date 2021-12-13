from typing import List

from data_access_layer.abstract_classes.manager_dao import ManagerDAO
from entities.manager import Manager
from utils.database_connection import connection


class ManagerPostgresDAO(ManagerDAO):
    def get_manager_by_username(self, user_name: str) -> Manager:
        sql = 'select * from "python_reimbursement".manager where user_name = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [user_name])
        manager_record = cursor.fetchone()
        manager = Manager(*manager_record)
        return manager

    def get_all_managers(self) -> List[Manager]:
        sql = 'select * from "python_reimbursement".manager'
        cursor = connection.cursor()
        cursor.execute(sql)
        manager_records = cursor.fetchall()
        manager_list = []
        for manager in manager_records:
            manager_list.append(Manager(*manager))
        return manager_list

