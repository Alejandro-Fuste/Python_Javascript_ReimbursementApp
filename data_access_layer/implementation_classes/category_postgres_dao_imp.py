from typing import List

from data_access_layer.abstract_classes.category_dao import CategoryDao
from entities.category import Category
from utils.database_connection import connection


class CategoryPostgresDao(CategoryDao):

    def get_all_categories(self) -> List[Category]:
        sql = 'select * from "python_reimbursement".category'
        cursor = connection.cursor()
        cursor.execute(sql)
        category_records = cursor.fetchall()
        category_list = []
        for category in category_records:
            category_list.append(Category(*category))
        return category_list
