class Reimbursement:
    def __init__(self, reimbursement_id: int, reimbursement_amount: float, reimbursement_reason: str,
                 reimbursement_date: str, status: str, reject_reason: str, accepted_date: str, category: str,
                 employee_name: str, manager_name: str):
        self.reimbursement_id = reimbursement_id
        self.reimbursement_amount = reimbursement_amount
        self.reimbursement_reason = reimbursement_reason
        self.reimbursement_date = reimbursement_date
        self.status = status
        self.accepted_date = accepted_date
        self.reject_reason = reject_reason
        self.category = category
        self.employee_name = employee_name
        self.manager_name = manager_name

    def __str__(self):
        return f'reimbursement id: {self.reimbursement_id},\nreimbursement amount: {self.reimbursement_amount},\n' \
               f'reimbursement reason:{self.reimbursement_reason},\nstatus: {self.status},\nrejectReason: ' \
               f'{self.reject_reason},\naccepted date: {self.accepted_date},\ncategory: {self.category},\n' \
               f'employee ID: {self.employee_name},\nmanager ID: {self.manager_name}'

    def make_reimbursement_dictionary(self):
        return {
            "reimbursementId": self.reimbursement_id,
            "reimbursementAmount": self.reimbursement_amount,
            "reimbursementReason": self.reimbursement_reason,
            "status": self.status,
            "rejectReason": self.reject_reason,
            "acceptedDate": self.accepted_date,
            "category": self.category,
            "employeeName": self.employee_name,
            "managerName": self.manager_name
        }

#
# new_reim = Reimbursement(1, 20.00, 'Travel gas', '12-9-2021', 'pending', 'null', 'null', 1, 1)
# print(new_reim)
# print(new_reim.make_reimbursement_dictionary())
#
# new_reim_two = Reimbursement(2, 2000.00, 'Hotel stay', '11-15-2021', 'rejected', '12-5-2021',
#                              'The amount of your reimbursement exceed your budget', 1, 1)
# print(new_reim_two)
# print(new_reim_two.make_reimbursement_dictionary())
