from data_access_layer.implementation_classes.category_postgres_dao_imp import CategoryPostgresDao
from entities.category import Category

category_dao = CategoryPostgresDao()


def test_get_all_categories():
    categories = category_dao.get_all_categories()
    assert len(categories) > 2
