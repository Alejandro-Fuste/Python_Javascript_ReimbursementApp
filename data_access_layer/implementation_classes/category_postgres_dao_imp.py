from typing import List

from data_access_layer.abstract_classes.category_dao import CategoryDao
from entities.category import Category
from utils.database_connection import connection


class CategoryPostgresDao(CategoryDao):

    def get_all_categories(self) -> List[Category]:
        pass
