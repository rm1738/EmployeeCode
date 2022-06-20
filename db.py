import sqlite3

conn = sqlite3.connect("Employees.sqlite")

cursor = conn.cursor()
sql_query = """ CREATE TABLE employee (
    id integer PRIMARY KEY,
    empID integer NOT NULL,
    name text NOT NULL,
    department text NOT NULL,
    salary float NOT NULL
)"""
cursor.execute(sql_query)


