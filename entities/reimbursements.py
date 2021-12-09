from datetime import datetime


class Reimbursements:
    def __init__(self, reimbursement_id: int, manager_first_name: str, manager_last_name: str,
                 reimbursement_amount: float, reimbursement_reason: str, reimbursement_date: datetime, status: str,
                 reject_reason: str, accepted_date: datetime, user_id: int):
        self.reimbursement_id = reimbursement_id
        self.manager_first_name = manager_first_name
        self.manager_last_name = manager_last_name
        self.reimbursement_amount = reimbursement_amount
        self.reimbursement_reason = reimbursement_reason
        self.reimbursement_date = reimbursement_date
        self.status = status
        self.reject_reason = reject_reason
        self.accepted_date = accepted_date
        self.user_id = user_id

    def __str__(self):
        return f'reimbursement id: {self.reimbursement_id},\nmanager first name: {self.manager_first_name},\n' \
               f'manager last name: {self.manager_last_name},\nreimbursement amount: {self.reimbursement_amount},\n' \
               f'reimbursement reason: {self.reimbursement_reason}, status: {self.status},\n' \
               f'rejectReason: {self.reject_reason},\naccepted date: {self.accepted_date},\nuser ID: {self.user_id}'

    def make_reimbursement_dictionary(self):
        return {
            "reimbursementId": self.reimbursement_id,
            "managerFirstName": self.manager_first_name,
            "managerLastName": self.manager_last_name,
            "reimbursementAmount": self.reimbursement_amount,
            "reimbursementReason": self.reimbursement_reason,
            "status": self.status,
            "rejectReason": self.reject_reason,
            "acceptedDate": self.accepted_date,
            "userID": self.user_id
        }


new_reimburse = Reimbursements(1, 'Leia', 'Organa', 20.00, 'Travel gas', datetime(2021, 12, 9), 'pending', 'null',
                               datetime(2021, 1, 1), 1)
print(new_reimburse)
print(new_reimburse.make_reimbursement_dictionary())