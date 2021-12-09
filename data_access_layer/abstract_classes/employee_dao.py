from abc import ABC, abstractmethod
from typing import List
from entities.employee import Employee


class EmployeeDAO(ABC):
    @abstractmethod
    def get_all_reimbursements(self) -> List[Employee]:
        pass
