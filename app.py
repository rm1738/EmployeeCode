from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)


def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("emp.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn


@app.route("/emp", methods=["GET", "POST"])
def employees():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM employee")
        Employees = [
            dict(id=row[0], empID=row[1], deptID=row[2], locID=row[3], name=row[4], salary=row[5], email=row[6])
            for row in cursor.fetchall()
        ]
        if Employees is not None:
            return jsonify(Employees)

    if request.method == "POST":
        new_empID = request.form["empID"]
        new_name = request.form["name"]
        new_departmentID = request.form["deptID"]
        new_salary = request.form["salary"]
        new_email = request.form["email"]
        new_locationID = request.form["locID"]
        sql = """INSERT INTO employee (empID, deptID, locID,name,salary,email)
                         VALUES (?, ?,?,?,?,?)"""
        cursor = cursor.execute(sql, (new_empID, new_name, new_departmentID, new_salary, new_email, new_locationID))
        conn.commit()
        return f"Employee added successfully", 201

    @app.route("/emp/<int:id>", methods=["GET", "PUT", "DELETE"])
    def single_employee(id):
        connE = db_connection()
        cursorEMP = connE.cursor()
        employee = None
        if request.method == "GET":
            cursorEMP.execute("SELECT * FROM employee WHERE id=?", (id,))
            rows = cursorEMP.fetchall()
            for r in rows:
                employee = r
            if employee is not None:
                return jsonify(employee), 200
            else:
                return "Something wrong", 404

            if request.method == "PUT":
                sql_B = """UPDATE employee
                        SET  empID=?,
                            deptID=?,
                             locID=?,
                             name=?,
                             salary=?,
                             email=? 
                        WHERE id=? """

            emp_id = request.form["empID"]
            name = request.form["name"]
            deptID = request.form["deptID"]
            salary = request.form["salary"]
            locID = request.form["locID"]
            email = request.form["email"]

            updated_employee = {
                "id": id,
                "empID": emp_id,
                "name": name,
                "salary": salary,
                "deptID": deptID,
                "locID": locID
            }

            connE.execute(sql_B, (emp_id, name, locID, salary, id, deptID))
            conn.commit()
            return jsonify(updated_employee)

    @app.route("/dep", methods=["GET", "POST"])
    def department():
        connA = db_connection()
        cursorA = connA.cursor()

        if request.method == "GET":
            cursorA = connA.execute("SELECT * FROM department")
            Departments = [
                dict(id=row[0], deptID=row[1], name=row[2])
                for row in cursorA.fetchall()
            ]
            if Departments is not None:
                return jsonify(Departments)

        if request.method == "POST":
            new_deptID = request.form["deptID"]
            new_Name = request.form["name"]
            sqlA = """INSERT INTO department (deptID, name)
                                 VALUES (?, ?)"""
            cursor_A = cursorA.execute(sql, (new_deptID, new_Name))
            connA.commit()
            return f"department added successfully", 201

        @app.route("/dep/<int:id>", methods=["GET", "PUT", "DELETE"])
        def single_department(id):
            connE = db_connection()
            cursorEMP = connE.cursor()
            department = None
            if request.method == "GET":
                cursorEMP.execute("SELECT * FROM department WHERE id=?", (id,))
                rows = cursorEMP.fetchall()
                for r in rows:
                    department = r
                if department is not None:
                    return jsonify(department), 200
                else:
                    return "Something wrong", 404

                if request.method == "PUT":
                    sql_C = """UPDATE employee
                               SET  deptID=?,
                                   name=?
                               WHERE id=? """

                deptName = request.form["name"]
                deptID = request.form["deptID"]

                updated_department = {
                    "name": name,
                    "deptID": deptID
                }

                connE.execute(sql_C, (name, deptID))
                conn.commit()
                return jsonify(updated_department)

        @app.route("/loc", methods=["GET", "POST"])
        def location():
            connB = db_connection()
            cursorB = connB.cursor()

            if request.method == "GET":
                cursorB = connB.execute("SELECT * FROM location")
                Locations = [
                    dict(id=row[0], locID=row[1], name=row[2])
                    for row in cursorB.fetchall()
                ]
                if Locations is not None:
                    return jsonify(Locations)

            if request.method == "POST":
                new_locID = request.form["locID"]
                new_locName = request.form["name"]
                sqlB = """INSERT INTO department (locID, name)
                                     VALUES (?, ?)"""
                cursorB = cursorB.execute(sql, (new_locID, new_locName))
                connB.commit()
                return f"Location added successfully", 201

            @app.route("/loc/<int:id>", methods=["GET", "PUT", "DELETE"])
            def single_location(id):
                connE = db_connection()
                cursorEMP = connE.cursor()
                location = None
                if request.method == "GET":
                    cursorEMP.execute("SELECT * FROM department WHERE id=?", (id,))
                    rows = cursorEMP.fetchall()
                    for r in rows:
                        location = r
                    if location is not None:
                        return jsonify(location), 200
                    else:
                        return "Something wrong", 404

                    if request.method == "PUT":
                        sql_C = """UPDATE location
                                           SET  locID=?,
                                               name=?
                                           WHERE id=? """

                    locName = request.form["name"]
                    locID = request.form["locID"]

                    updated_location = {
                        "name": name,
                        "locID": locID
                    }

                    connE.execute(sql_C, (name, locID))
                    conn.commit()
                    return jsonify(updated_location)

       






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
