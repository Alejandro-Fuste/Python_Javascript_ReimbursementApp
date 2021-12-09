from abc import ABC, abstractmethod
from entities.reimbursement import Reimbursement


class ReimbursementDAO(ABC):
    @abstractmethod
    def create_new_reimbursement_request(self, reimbursement: Reimbursement) -> Reimbursement:
        pass
