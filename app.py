from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("Employees.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn


@app.route("/employees", methods=["GET", "POST"])
def employees():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM employee")
        employee = [
            dict(id=row[0], empID=row[1], name=row[2], department=row[3], salary=row[4])
            for row in cursor.fetchall()
        ]
        if employees is not None:
            return jsonify(employees)

    if request.method == "POST":
        new_empID = request.form["empID"]
        new_name = request.form["name"]
        new_department = request.form["department"]
        new_salary = request.form["salary"]
        sql = """INSERT INTO employee (empID, name, department, salary)
                         VALUES (?, ?, ?,?,?)"""
        cursor = cursor.execute(sql, (new_empID, new_name, new_department, new_salary))
        conn.commit()
        return f"Employee added successfully", 201


@app.route("/employee/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_employee(id):
    conn = db_connection()
    cursor = conn.cursor()
    employee = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM employee WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            employee = r
        if employee is not None:
            return jsonify(employee), 200
        else:
            return "Something wrong", 404

    if request.method == "PUT":
        sql = """UPDATE employee
                SET  empID=?,
                    name=?,
                     department=?,
                     salary=?
                WHERE id=? """

    emp_id = request.form["empID"]
    name = request.form["name"]
    department = request.form["department"]
    salary = request.form["salary"]

    updated_employee = {
        "id": id,
        "empID": emp_id,
        "name": name,
        "language": salary,
        "department": department,
    }

    conn.execute(sql, (id, emp_id, name, department,salary))
    conn.commit()
    return jsonify(updated_employee)

    if request.method == "DELETE":
        sql = """ DELETE FROM employee WHERE id=? """
        conn.execute(sql, (id,))
        conn.commit()
        return "The employee with id: {} has been deleted.".format(id), 200

    if __name__ == "__main__":
        app.run(debug=True)



