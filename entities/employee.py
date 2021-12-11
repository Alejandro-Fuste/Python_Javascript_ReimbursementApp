from typing import List


class Employee:
    def __init__(self, employee_id: int, first_name: str, last_name: str, company_role: str, user_name: str,
                 user_password: str, reimbursements: List = []):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.company_role = company_role
        self.user_name = user_name
        self.user_password = user_password
        self.reimbursements = reimbursements

    def __str__(self):
        return f'employee id:{self.employee_id}, first name: {self.first_name}, last name: {self.last_name}, ' \
               f'company role: {self.company_role}, user name: {self.user_name}, password: {self.user_password}, ' \
               f'reimbursements: {self.reimbursements}'

    def make_company_user_dictionary(self):
        return {
            "employeeId": self.employee_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "companyRole": self.company_role,
            "userName": self.user_name,
            "userPassword": self.user_password,
            "reimbursements": self.reimbursements,
        }

# new_employee = Employee(1, 'Rey', 'Skywalker', 'Employee', 'NinjaCatGirl',
#                         'JakkuJedi1', [{'reimbursementId': 1, 'reimbursementAmount': 20.0, 'reimbursementReason':
#         'Travel gas', 'status': 'pending', 'rejectReason': 'null', 'acceptedDate': 'null', 'employeeID': 1,
#                                         'managerID': 1}, {'reimbursementId': 2, 'reimbursementAmount': 2000.0,
#                                                           'reimbursementReason': 'Hotel stay', 'status': 'rejected',
#                                                           'rejectReason': '12-5-2021', 'acceptedDate':
#                                                               'The amount of your reimbursement exceed your budget',
#                                                           'employeeID': 1, 'managerID': 1}])
# print(new_employee)
# print(new_employee.make_company_user_dictionary())
