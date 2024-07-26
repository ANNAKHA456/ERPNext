# Copyright (c) 2024, Anna and contributors
# For license information, please see license.txt

# import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data

import frappe

def execute(filters=None):
    columns = [
        {"label": "Student Name", "fieldname": "name1", "fieldtype": "Data"},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data"},
        {"label": "Register Number", "fieldname": "register_number", "fieldtype": "Data"},
        {"label": "Gender", "fieldname": "gender", "fieldtype": "Data"},
        {"label": "Email", "fieldname": "email", "fieldtype": "Data"},
        {"label": "Phone Number", "fieldname": "phone_number", "fieldtype": "Data"},
        {"label": "Department", "fieldname": "department", "fieldtype": "Data"},
        {"label": "Course", "fieldname": "course", "fieldtype": "Data"},
        {"label": "Date of Birth", "fieldname": "date_of_birth", "fieldtype": "Date"},
        {"label": "Subject Code", "fieldname": "subject_code", "fieldtype": "Data"},
        {"label": "Subject Name", "fieldname": "subject_name", "fieldtype": "Data"},
        {"label": "Mark", "fieldname": "mark", "fieldtype": "Data"},
        {"label": "Total Mark", "fieldname": "total_mark", "fieldtype": "Data"},
        {"label": "Percentage", "fieldname": "percentage", "fieldtype": "Data"}
    ]

    data = []

    student_filters = {}
    if filters:
        if filters.get("register_number"):
            student_filters["register_number"] = filters.get("register_number")
        if filters.get("name1"):
            student_filters["name1"] = ["like", f"%{filters.get('name1')}%"]
        if filters.get("gender"):
            student_filters["gender"] = filters.get("gender")
        if filters.get("email"):
            student_filters["email"] = ["like", f"%{filters.get('email')}%"]
        if filters.get("phone_number"):
            student_filters["phone_number"] = filters.get("phone_number")
        if filters.get("department"):
            student_filters["department"] = filters.get("department")
        if filters.get("course"):
            student_filters["course"] = filters.get("course")
        if filters.get("date_of_birth"):
            student_filters["date_of_birth"] = filters.get("date_of_birth")

    students = frappe.get_all("Student", filters=student_filters, fields=["*"])

    for student in students:
        marks = frappe.get_all("Mark", filters={"parent": student.name}, fields=["*"])
        for mark in marks:
            row = {
                "name1": student.name1,
                "status": student.status,
                "register_number": student.register_number,
                "gender": student.gender,
                "email": student.email,
                "phone_number": student.phone_number,
                "department": student.department,
                "course": student.course,
                "date_of_birth": student.date_of_birth,
                # "subject_code": mark.subject_code,
                 "subject_name": mark.subject_name,
                # "mark": mark.mark,
                # "total_mark": mark.total_mark,
                # "percentage": mark.percentage
            }
            data.append(row)

    return columns, data