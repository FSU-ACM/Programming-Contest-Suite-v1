## Create Tables Document for reference.
## Hayden Rogers
## 4/7/2019

CREATE TABLE Account (
	AccountID int,
	Role varchar(255),
	FirstName varchar(255),
	LastName varchar(255),
	FsuCardNum varchar(255),
	Password varchar(255),
	Email varchar(255),
	CourseID int,
	TeamID int,
	PRIMARY KEY (AccountID),
	FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
)

CREATE TABLE Course (
	CourseID int,
	CourseName varchar(255),
	FacultyID int,
	PRIMARY KEY (CourseID),
	FOREIGN KEY (FacultyID) REFERENCES Faculty(FacultyID)
)

CREATE TABLE Faculty (
	FacultyID int,
	FirstName varchar(255),
	LastName varchar(255),
	Email varchar(255),
	PRIMARY KEY (FacultyID)
)

CREATE TABLE Team (
	TeamID int,
	TeamName varchar(255),
	Division varchar(255),
	TeamPassword varchar (255),
	PRIMARY KEY (TeamID)
)

CREATE TABLE Admin (
	AdminID int,
	FirstName varchar(255)
	LastName varchar(255)
	PRIMARY KEY (AdminID)
)