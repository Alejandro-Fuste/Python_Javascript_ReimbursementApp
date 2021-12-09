-- Create users
insert into company_user values (default, 'Luke', 'Skywalker', 'Manager', 'Master Jedi', 'TheRealChosenOne');
insert into company_user values (default, 'Leia', 'Organa', 'Manager', 'Princess Leia', 'PrincessLeiaJedi');
insert into company_user values (default, 'Rey', 'Skywalker', 'Employee', 'NinjaCatGirl', 'JakkuJedi1');

--Create reimbursements

insert into reimbursement values (default, 'Leia', 'Organa', 20.00, 'Travel gas', '12-9-2021', 'pending', null, null, 1)
insert into reimbursement values (default, 'Luke', 'Skywalker', 100.00, 'Food', '12-8-2021', 'pending', null, null, 3)