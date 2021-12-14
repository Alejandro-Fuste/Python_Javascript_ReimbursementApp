class Reimbursement:
    def __init__(self, reimbursement_id: int, reimbursement_amount: float, category: str, reimbursement_reason: str,
                 reimbursement_date: str, status: str, decision_date: str, reason: str, employee_id: int,
                 manager_id: int):
        self.reimbursement_id = reimbursement_id
        self.reimbursement_amount = reimbursement_amount
        self.category = category
        self.reimbursement_reason = reimbursement_reason
        self.reimbursement_date = reimbursement_date
        self.status = status
        self.decision_date = decision_date
        self.reason = reason
        self.employee_id = employee_id
        self.manager_id = manager_id

    def __str__(self):
        return f'reimbursement id: {self.reimbursement_id},\nreimbursement amount: {self.reimbursement_amount},\n' \
               f'category: {self.category}\nreimbursement reason:{self.reimbursement_reason},\n' \
               f'reimbursement date: {self.reimbursement_date},\nstatus: {self.status},\n' \
               f'decision date: {self.decision_date},\nreason: {self.reason},\nemployee ID: {self.employee_id}\n' \
               f'manager ID: {self.manager_id}'

    def make_reimbursement_dictionary(self):
        return {
            "reimbursementId": self.reimbursement_id,
            "reimbursementAmount": self.reimbursement_amount,
            "category": self.category,
            "reimbursementReason": self.reimbursement_reason,
            "reimbursementDate": self.reimbursement_date,
            "status": self.status,
            "decisionDate": self.decision_date,
            "reason": self.reason,
            "employeeId": self.employee_id,
            "managerId": self.manager_id,
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
