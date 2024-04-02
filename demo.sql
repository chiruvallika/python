USE company_details; 

create database companies_data;
use companies_data;

CREATE TABLE accounts (
    acc_id INT IDENTITY(1,1) PRIMARY KEY,
    acc_name NVARCHAR(255) not null,
    acc_date DATE default getdate(),
);

create table designations(
	des_id int identity(1,1) primary key,
	designation nvarchar(255) not null,
);

create table account_employee_details(
	emp_id int identity(1,1) primary key,
	acc_id int foreign key references accounts(acc_id),
	des_id int foreign key references designations(des_id),
	emp_name nvarchar(255) not null,
	mobile_number nvarchar(20) not null,
);


select acc.acc_name,emp.emp_name,emp.mobile,des.designation from 
account_employee_details emp join accounts acc on acc.acc_id = emp.acc_id 
join designations des on des.des_id = emp.des_id;



insert into account_employee_details values(1,2,'sravya','9502336298');

select acc.acc_name,emp.emp_name,emp.mobile_number,des.designation from 
account_employee emp join accounts acc on acc.acc_id = emp.acc_id 
join designation des on des.des_id = emp.des_id;