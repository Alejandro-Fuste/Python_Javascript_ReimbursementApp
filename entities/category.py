class Category:
    def __init__(self, category_id: int, category_name: str):
        self.category_id = category_id
        self.category_name = category_name

    def __str__(self):
        return f'category id: {self.category_id}, category name: {self.category_name}'

    def make_category_dictionary(self):
        return {
            "categoryId": self.category_id,
            "categoryName": self.category_name
        }

    
