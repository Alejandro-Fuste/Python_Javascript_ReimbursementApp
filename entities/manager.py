class Manager:
    def __init__(self, manager_id: int, first_name: str, last_name: str, company_role: str, user_name: str,
                 user_password: str):
        self.manager_id = manager_id
        self.first_name = first_name
        self.last_name = last_name
        self.company_role = company_role
        self.user_name = user_name
        self.user_password = user_password

    def __str__(self):
        return f'manager id:{self.manager_id}, first name: {self.first_name}, last name: {self.last_name}, ' \
               f'company role: {self.company_role}, user name: {self.user_name}, password: {self.user_password}, '

    def make_manager_dictionary(self):
        return {
            "managerId": self.manager_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "companyRole": self.company_role,
            "userName": self.user_name,
            "userPassword": self.user_password
        }

    def return_manager_credentials(self):
        return {
            "managerId": self.manager_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "companyRole": self.company_role,
        }


# new_manager = Manager(1, 'Rey', 'Skywalker', 'Employee', 'NinjaCatGirl',
#                       'JakkuJedi1')
#
# print(new_manager)
# print(new_manager.make_manager_dictionary())
# print(new_manager.return_manager_credentials())
