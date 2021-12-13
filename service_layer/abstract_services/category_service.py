from abc import ABC, abstractmethod
from typing import List

from entities.category import Category


class CategoryService(ABC):
    @abstractmethod
    def service_get_all_categories(self) -> List[Category]:
        pass
