drop table if exists employee, manager, reimbursement;

create table employee(
	employee_id serial not null primary key,
	first_name varchar (30) not null,
	last_name varchar (30) not null,
	company_role varchar (30) not null,
	user_name varchar (30) not null,
	user_password varchar (30) not null

);

create table manager(
	manager_id serial not null primary key,
	first_name varchar (30) not null,
	last_name varchar (30) not null,
	company_role varchar (30) not null,
	user_name varchar (30) not null,
	user_password varchar (30) not null
)


create table reimbursement(
	reimbursement_id serial not null primary key,
	reimbursement_amount decimal not null,
	reimbursement_reason text not null,
	reimbursement_date date not null,
	status varchar (30) not null,
	accepted_date date,
	reason text,
	employee_id int references employee(employee_id) on delete cascade,
	manager_id int references manager(manager_id) on delete cascade

);