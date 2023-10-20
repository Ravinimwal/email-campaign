create database if not exists email2_db;
use email2_db;


CREATE TABLE USER(
	name varchar(255),
    email varchar(255) UNIQUE PRIMARY KEY,
    isAdmin bool default False,
    password varchar(255)
);

CREATE TABLE Subscribers (
    email VARCHAR(255) UNIQUE PRIMARY KEY NOT NULL,
    first_name VARCHAR(50),
    isActive BOOLEAN DEFAULT TRUE
);
INSERT INTO USER(name,email,isAdmin,password)
		values	("mayank","m@g.com",1,"1234"),
				("test","test@g.com",0,"1234");


select * from Subscribers;
select * from USER;




