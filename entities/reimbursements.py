from datetime import datetime


class Reimbursements:
    def __init__(self, reimbursement_id: int, reimbursement_amount: float, reimbursement_reason: str,
                 reimbursement_date: datetime, status: str, reject_reason: str, accepted_date: datetime,
                 employee_id: int, manager_id: int):
        self.reimbursement_id = reimbursement_id
        self.reimbursement_amount = reimbursement_amount
        self.reimbursement_reason = reimbursement_reason
        self.reimbursement_date = reimbursement_date
        self.status = status
        self.accepted_date = accepted_date
        self.reject_reason = reject_reason
        self.employee_id = employee_id
        self.manager_id = manager_id

    def __str__(self):
        return f'reimbursement id: {self.reimbursement_id},\nreimbursement amount: {self.reimbursement_amount},\n' \
               f'reimbursement reason:{self.reimbursement_reason},\nstatus: {self.status},\nrejectReason: ' \
               f'{self.reject_reason},\naccepted date: {self.accepted_date},\nemployee ID: {self.employee_id},\n' \
               f'manager ID: {self.manager_id}'

    def make_reimbursement_dictionary(self):
        return {
            "reimbursementId": self.reimbursement_id,
            "reimbursementAmount": self.reimbursement_amount,
            "reimbursementReason": self.reimbursement_reason,
            "status": self.status,
            "rejectReason": self.reject_reason,
            "acceptedDate": self.accepted_date,
            "employeeID": self.employee_id,
            "managerID": self.manager_id
        }