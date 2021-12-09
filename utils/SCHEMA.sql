drop table if exists company_user, reimbursement;

create table company_user(
	user_id serial not null primary key,
	first_name varchar (30) not null,
	last_name varchar (30) not null,
	company_role varchar (30) not null,
	user_name varchar (30) not null,
	user_password varchar (30) not null

);


create table reimbursement(
	reimbursement_id serial not null primary key,
	expense_name varchar (30) not null,
	expense_amount decimal not null,
	expense_reason varchar (30) not null,
	expense_date date not null,
	status varchar (30) not null,
	reject_reason text,
	accepted_date date,
	user_id int references company_user(user_id) on delete cascade

);