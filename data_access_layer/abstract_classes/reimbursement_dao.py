from abc import ABC, abstractmethod
from typing import List

from entities.reimbursement import Reimbursement


class ReimbursementDAO(ABC):
    @abstractmethod
    def create_new_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    def get_all_reimbursement_requests(self) -> List[Reimbursement]:
        pass

    def update_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        pass
