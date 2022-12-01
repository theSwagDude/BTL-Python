CREATE DATABASE BTLPython;

USE BTLPython;

CREATE TABLE LWorks(
    Grade INT NOT NULL,
    Id INT NOT NULL,
    Name CHAR(50) NOT NULL,
    Year INT NOT NULL,
    Category CHAR(50) NOT NULL,
    Author_Name CHAR(50) NOT NULL,
    Author_Birth INT NOT NULL,
    Author_Death INT NOT NULL,
    Author_Home CHAR(50) NOT NULL
)