class Category:
    def __init__(self, category_name: str):
        self.category_name = category_name

    def __str__(self):
        return f'category name: {self.category_name}'

    def make_category_dictionary(self):
        return {
            "categoryName": self.category_name
        }

    
