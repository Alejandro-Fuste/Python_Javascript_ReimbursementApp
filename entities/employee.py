class Employee:
    def __init__(self, employee_id: int, first_name: str, last_name: str, company_role: str, user_name: str,
                 user_password: str):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.company_role = company_role
        self.user_name = user_name
        self.user_password = user_password

    def __str__(self):
        return f'employee id:{self.employee_id}, first name: {self.first_name}, last name: {self.last_name}, ' \
               f'company role: {self.company_role}, user name: {self.user_name}, password: {self.user_password}'

    def make_company_user_dictionary(self):
        return {
            "employeeId": self.employee_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "companyRole": self.company_role,
            "userName": self.user_name,
            "userPassword": self.user_password
        }

