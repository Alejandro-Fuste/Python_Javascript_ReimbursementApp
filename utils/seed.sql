-- Create employees
insert into employee values (default, 'Rey', 'Skywalker', 'Employee', 'NinjaCatGirl', 'JakkuJedi1');
insert into employee values (default, 'Ben', 'Solo', 'Employee', 'KyloRen', 'KyloRenIsJacked');
insert into employee values (default, 'Admiral', 'Ackbar', 'Employee', 'AdmiralAckbar', 'ItsATrap');

-- Create managers
insert into manager values (default, 'Luke', 'Skywalker', 'Manager', 'Master Jedi', 'TheRealChosenOne');

-- Create categories
insert into category values (default, 'Gas');
insert into category values (default, 'Car');
insert into category values (default, 'Hotel');
insert into category values (default, 'Food');
insert into category values (default, 'Education');
insert into category values (default, 'Other');

--Create reimbursements
insert into reimbursement values (default, 20.00, 'Gas', 'Travel gas', '12-20-2021', 'pending', null, null, 1, 1);
insert into reimbursement values (default, 2000.00, 'Hotel', 'Hotel stay', '12-15-2021', 'approved', '12-10-2021', 'Reimbursement was approved', 1, 1);
insert into reimbursement values (default, 1000.00, 'Other', 'Training supplies', '11-15-2021', 'approved', '11-25-2021', 'Reimbursement was approved', 1, 1);
insert into reimbursement values (default, 500.00, 'Other', 'Training clothes', '11-15-2021', 'approved', '11-25-2021', 'Reimbursement was approved', 1, 1);
insert into reimbursement values (default, 1000.00, 'Education', 'Jedi training books', '11-5-2021', 'approved', '11-15-2021', 'Reimbursement was approved', 1, 1);
insert into reimbursement values (default, 56.78, 'Food', 'Food', '10-27-2021', 'approved', '11/2/21', 'Reimbursement was approved', 1, 1);
insert into reimbursement values (default, 3000.00, 'Education', 'Dark side books', '9-9-2021', 'rejected', '9-11-2021', 'The books are not part of the approved reading list.', 2, 1);
insert into reimbursement values (default, 200.00, 'Car', 'Travel to dark side convention', '8-9-2021', 'rejected', '8-11-2021', 'Dark side convention, really?!', 2, 1);
insert into reimbursement values (default, 3000.00, 'Other', 'Trap detection supplies', '7-9-2021', 'approved', '7-12-2021', 'Reimbursement was approved', 3, 1);

-- Read category (get all categories)
select * from category

-- Read employee (get employee by username)
select * from employee where user_name = 'NinjaCatGirl'

-- Read manager (get manager by username)
select * from manager where user_name = 'Master Jedi'
select * from manager

-- Read reimbursements (get all reimbursements)
select * from reimbursement

-- Read Reimbursements (get reimbursements by employee_id)
select * from reimbursement where employee_id = 1;

-- Update Reimbursement (update reimbursement request)
update reimbursement set status = 'accepted', decision_date = '12-13-2021', reason = 'Your requested was approved' where reimbursement_id = 1;

-- Read Reimbursements (gets for stats)
	-- total reimbursements
select sum(reimbursement_amount) from reimbursement where status = 'approved';
	-- total reimbursement by employee
select sum(reimbursement_amount) from reimbursement where employee_id = 1;
	-- total by month
select sum(reimbursement_amount) from reimbursement where decision_date >= '12-1-2021' and decision_date <= '12-31-2021';
	-- total by category
select sum(reimbursement_amount) from reimbursement where category = 'Gas';
	-- top five amounts
select * from reimbursement where status = 'approved' order by reimbursement_amount desc limit 5;


