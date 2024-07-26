# from flask import Flask, jsonify
# import mysql.connector

# app = Flask(__name__)

# # Database configuration
# db = mysql.connector.connect(
#     host="localhost",
#     user="_ad2c083e62d4265d",
#     password="XquVkAuLuuCrbClA",
#     database="_ad2c083e62d4265d"
# )

# @app.route('/api/student', methods=['GET'])
# def get_students():
#     try:
#         cursor = db.cursor(dictionary=True)
#         cursor.execute("SELECT * FROM students")
#         students = cursor.fetchall()
#         cursor.close()
#         return jsonify(students), 200
#     except mysql.connector.Error as err:
#         return jsonify({"error": str(err)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
# Filename: your_custom_app/api/student_api.py

import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_students():
    try:
        # Query to fetch student records from the database
        students = frappe.get_all("Student", fields=["register_number","name1", "date_of_birth", "gender", "email", "phone_number", "department", "course"])

        # Fetch marks (assuming marks is a child table)
        # for student in students:
        #     student["marks"] = frappe.get_all("Mark", filters={"parent": student.name}, fields=["subject_code", "subject_name"])

        return students

    except Exception as e:
        frappe.throw(_("Failed to fetch students: {0}").format(str(e)))
# @frappe.whitelist()
# def get_student_by_register_number(register_number):
#     # Fetch student details based on register number
#     student = frappe.get_doc('Student', {'register_number': register_number})
#     if student:
#         return student.as_dict()
#     else:
#         frappe.throw(_('Student not found'), frappe.DoesNotExistError)
