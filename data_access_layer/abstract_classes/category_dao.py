from abc import ABC, abstractmethod
from typing import List

from entities.category import Category


class CategoryDao(ABC):
    @abstractmethod
    def get_all_categories(self) -> List[Category]:
        pass
