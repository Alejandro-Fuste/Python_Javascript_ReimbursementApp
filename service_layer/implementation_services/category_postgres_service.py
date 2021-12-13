from data_access_layer.implementation_classes.category_postgres_dao_imp import CategoryPostgresDao
from entities.category import Category
from service_layer.abstract_services.category_service import CategoryService
from typing import List


class CategoryPostgresServiceImp(CategoryService):
    def __init__(self, category_dao: CategoryPostgresDao):
        self.category_dao = category_dao

    def service_get_all_categories(self) -> List[Category]:
        return self.category_dao.get_all_categories()
