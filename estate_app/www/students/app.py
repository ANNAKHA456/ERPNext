# from flask import Flask, jsonify
# import frappe

# app = Flask(__name__)

# # Initialize Frappe
# def init_frappe():
#     frappe.init(site="demo01.com:8003")  # Your site name
#     frappe.connect()

# @app.route('/api/student', methods=['GET'])
# def get_students():
#     try:
#         init_frappe()
        
#         # Get all student documents
#         students = frappe.get_all('Student', fields=['*'])  # Fetch all fields

#         # You can process the data further if needed
#         student_data = []
#         for student in students:
#             # Fetch marks (assuming 'Marks' is a child table linked to 'Student')
#             marks = frappe.get_all('Marks', filters={'parent': student.name}, fields=['*'])
#             student['marks'] = marks
#             student_data.append(student)

#         return jsonify(student_data), 200
    
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    
#     finally:
#         frappe.destroy()

# if __name__ == '__main__':
#     app.run(debug=True)
import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_index_html():
    return frappe.render_template("students")
