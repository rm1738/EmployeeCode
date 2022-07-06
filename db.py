import sqlite3

conn = sqlite3.connect("emp.sqlite")

cursor = conn.cursor()
table = """ CREATE TABLE employee (
    id integer PRIMARY KEY,
    empID integer NOT NULL,
    deptID integer NOT NULL, 
    locID integer NOT NULL,
    name text NOT NULL,
    salary float NOT NULL,
    email text NOT NULL
)"""


tableB = """ CREATE TABLE department (
    id integer PRIMARY KEY,
    deptID integer NOT NULL
    name text NOT NULL
)"""


tableC = """ CREATE TABLE location (
    id integer PRIMARY KEY,
    locID integer NOT NULL,
    name text NOT NULL
)"""
cursor.execute(table)
cursor.execute(tableB)
cursor.execute(tableC)
