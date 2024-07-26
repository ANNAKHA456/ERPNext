# # # # Copyright (c) 2024, Anna and contributors
# # # # For license information, please see license.txt

# # # # import frappe


# # # # def execute(filters=None):
# # # # 	columns, data = [], []
# # # # 	return columns, data
# # import frappe
# # # @frappe.whitelist()
# # def execute(filters=None):
# #     frappe.throw("Hi")
# #     columns = [
# #         {"label": "Student Name", "fieldname": "name1", "fieldtype": "Data"},
# #         {"label": "Status", "fieldname": "status", "fieldtype": "Data"},
# #         {"label": "Register Number", "fieldname": "register_number", "fieldtype": "Data"},
# #         {"label": "Gender", "fieldname": "gender", "fieldtype": "Data"},
# #         {"label": "Email", "fieldname": "email", "fieldtype": "Data"},
# #         {"label": "Phone Number", "fieldname": "phone_number", "fieldtype": "Data"},
# #         {"label": "Department", "fieldname": "department", "fieldtype": "Data"},
# #         {"label": "Course", "fieldname": "course", "fieldtype": "Data"},
# #         {"label": "Date of Birth", "fieldname": "date_of_birth", "fieldtype": "Date"},
# #         {"label": "Subject Code", "fieldname": "subject_code", "fieldtype": "Data"},
# #         {"label": "Subject Name", "fieldname": "subject_name", "fieldtype": "Data"},
# #         {"label": "Total Mark", "fieldname": "total_mark", "fieldtype": "Data"},
# #         {"label": "Percentage", "fieldname": "percentage", "fieldtype": "Data"}
# #     ]

# #     data = []

# #     student_filters = {}
# #     if filters:
# #         if filters.get("register_number"):
# #             student_filters["register_number"] = filters.get("register_number")
# #         if filters.get("name1"):
# #             student_filters["name1"] = filters.get("name1")
# #         if filters.get("gender"):
# #             student_filters["gender"] = filters.get("gender")
# #         if filters.get("email"):
# #             student_filters["email"] = filters.get("email")
# #         if filters.get("phone_number"):
# #             student_filters["phone_number"] = filters.get("phone_number")
# #         if filters.get("department"):
# #             student_filters["department"] = filters.get("department")
# #         if filters.get("course"):
# #             student_filters["course"] = filters.get("course")

# #     students = frappe.get_all("Student", filters=student_filters, fields=["*"])
# #     frappe.throw(students)
# #     for student in students:
# #         marks = frappe.get_all("Marks", filters={"parent": student.name}, fields=["*"])
# #         for mark in marks:
# #             row = {
# #                 "name1": student.name1,
# #                 "status": student.status,
# #                 "register_number": student.register_number,
# #                 "gender": student.gender,
# #                 "email": student.email,
# #                 "phone_number": student.phone_number,
# #                 "department": student.department,
# #                 "course": student.course,
# #                 "date_of_birth": student.date_of_birth,
# #                 "subject_code": mark.subject_code,
# #                 "subject_name": mark.subject_name,
# #                 "total_mark": mark.total_mark,
# #                 "percentage": mark.percentage
# #             }
# #             data.append(row)

# #     return columns, data

# # import frappe
# # from frappe import _


# # def execute(filters=None):
# #     columns, data = get_columns(), get_data(filters)
# #     return columns, data


# # def get_columns():
# #     return [
# #         {"label": _("Student Name"), "fieldname": "name1", "fieldtype": "Data"},
# #         {"label": _("Status"), "fieldname": "status", "fieldtype": "Data"},
# #         {"label": _("Register Number"), "fieldname": "register_number", "fieldtype": "Data"},
# #         {"label": _("Gender"), "fieldname": "gender", "fieldtype": "Data"},
# #         {"label": _("Phone Number"),"fieldname": "phone_number","fieldtype": "Data"},
# # {
# #     "label": _("Department"),
# #     "fieldname": "department",
# #     "fieldtype": "Data"
# # },
# # {
# #     "label": _("Course"),
# #     "fieldname": "course",
# #     "fieldtype": "Data"
# # },
# # {
# #     "label": _("Date of Birth"),
# #     "fieldname": "date_of_birth",
# #     "fieldtype": "Date"
# # }
        
        
# #     ]


# # def get_data(filters=None):
# #     data = []
# #     student_filters = {}

# #     if filters:
# #         if filters.get("register_number"):
# #             student_filters["register_number"] = filters.get("register_number")
# #         if filters.get("name1"):
# #             student_filters["name1"] = filters.get("name1")
# #         if filters.get("gender"):
# #             student_filters["gender"] = filters.get("gender")
# #         if filters.get("email"):
# #             student_filters["email"] = filters.get("email")
# #         if filters.get("phone_number"):
# #             student_filters["phone_number"] = filters.get("phone_number")
# #         if filters.get("department"):
# #             student_filters["department"] = filters.get("department")
# #         if filters.get("course"):
# #             student_filters["course"] = filters.get("course")

# #     students = frappe.get_all("Student", filters=student_filters, fields=["name1", "status", "register_number", "gender"])

# #     for student in students:
# #         data.append(student)

# #     return data
# import frappe
# from frappe import _

# def execute(filters=None):
#     columns, data = get_columns(), get_data(filters)
#     return columns, data

# def get_columns():
#     return [
#         {"label": _("Student Name"), "fieldname": "name1", "fieldtype": "Data"},
#         {"label": _("Status"), "fieldname": "status", "fieldtype": "Data"},
#         {"label": _("Register Number"), "fieldname": "register_number", "fieldtype": "Data"},
#         {"label": _("Gender"), "fieldname": "gender", "fieldtype": "Data"},
#         {"label": _("Phone Number"), "fieldname": "phone_number", "fieldtype": "Data"},
#         {"label": _("Department"), "fieldname": "department", "fieldtype": "Data"},
#         {"label": _("Course"), "fieldname": "course", "fieldtype": "Data"},
#         {"label": _("Date of Birth"), "fieldname": "date_of_birth", "fieldtype": "Date"},
#         {"label": _("Subject Code"), "fieldname": "subject_code", "fieldtype": "Data"},
#         {"label": _("Subject Name"), "fieldname": "subject_name", "fieldtype": "Data"},
#         {"label": _("Marks Obtained"), "fieldname": "marks_obtained", "fieldtype": "Float"},
#         {"label": _("Total Marks"), "fieldname": "total_marks", "fieldtype": "Float"},
#         {"label": _("Percentage"), "fieldname": "percentage", "fieldtype": "Percent"},
#         {"label": _("Total Marks Obtained"), "fieldname": "total_marks_obtained", "fieldtype": "Float"},
#         {"label": _("Total Marks Available"), "fieldname": "total_marks_available", "fieldtype": "Float"},
#     ]

# # def get_data(filters=None):
# #     data = []
# #     student_filters = {}

# #     if filters:
# #         if filters.get("register_number"):
# #             student_filters["register_number"] = filters.get("register_number")
# #         if filters.get("name1"):
# #             student_filters["name1"] = filters.get("name1")
# #         if filters.get("gender"):
# #             student_filters["gender"] = filters.get("gender")
# #         if filters.get("email"):
# #             student_filters["email"] = filters.get("email")
# #         if filters.get("phone_number"):
# #             student_filters["phone_number"] = filters.get("phone_number")
# #         if filters.get("department"):
# #             student_filters["department"] = filters.get("department")
# #         if filters.get("course"):
# #             student_filters["course"] = filters.get("course")

# #     students = frappe.get_all("Student", filters=student_filters, fields=["name1", "status", "register_number", "gender", "phone_number", "department", "course", "date_of_birth"])

# #     for student in students:
# #         # Fetch marks for the student
# #         marks = frappe.get_all("Mark", filters={"parent": student["register_number"]}, fields=["subject_code", "subject_name", "mark_obtained", "maximum_marks", "percentage"])
        
# #         student_details_added = False

# #         if marks:
# #             for mark in marks:
# #                 mark_data = {
# #                     "subject_code": mark["subject_code"],
# #                     "subject_name": mark["subject_name"],
# #                     "marks_obtained": mark["mark_obtained"],
# #                     "total_marks": mark["maximum_marks"],
# #                     "percentage": mark["percentage"]
# #                 }

# #                 if not student_details_added:
# #                     student_data = student.copy()
# #                     student_data.update(mark_data)
# #                     data.append(student_data)
# #                     student_details_added = True
# #                 else:
# #                     # Append only the marks information
# #                     empty_student_data = {
# #                         "name1": "",
# #                         "status": "",
# #                         "register_number": "",
# #                         "gender": "",
# #                         "phone_number": "",
# #                         "department": "",
# #                         "course": "",
# #                         "date_of_birth": "",
# #                     }
# #                     empty_student_data.update(mark_data)
# #                     data.append(empty_student_data)
# #         else:
# #             # No marks found, append student details with empty mark fields
# #             student_data = {
# #                 "name1": student["name1"],
# #                 "status": student["status"],
# #                 "register_number": student["register_number"],
# #                 "gender": student["gender"],
# #                 "phone_number": student["phone_number"],
# #                 "department": student["department"],
# #                 "course": student["course"],
# #                 "date_of_birth": student["date_of_birth"],
# #                 "subject_code": None,
# #                 "subject_name": None,
# #                 "marks_obtained": None,
# #                 "total_marks": None,
# #                 "percentage": None
# #             }
# #             data.append(student_data)

# #     return data
# def get_data(filters=None):
#     data = []
#     student_filters = {}

#     if filters:
#         if filters.get("register_number"):
#             student_filters["register_number"] = filters.get("register_number")
#         if filters.get("name1"):
#             student_filters["name1"] = filters.get("name1")
#         if filters.get("gender"):
#             student_filters["gender"] = filters.get("gender")
#         if filters.get("email"):
#             student_filters["email"] = filters.get("email")
#         if filters.get("phone_number"):
#             student_filters["phone_number"] = filters.get("phone_number")
#         if filters.get("department"):
#             student_filters["department"] = filters.get("department")
#         if filters.get("course"):
#             student_filters["course"] = filters.get("course")

#     students = frappe.get_all("Student", filters=student_filters, fields=["name1", "status", "register_number", "gender", "phone_number", "department", "course", "date_of_birth"])

#     for student in students:
#         # Fetch marks for the student
#         marks = frappe.get_all("Mark", filters={"parent": student["register_number"]}, fields=["subject_code", "subject_name", "mark_obtained", "maximum_marks", "percentage"])
        
#         student_details_added = False
#         total_marks_obtained = 0
#         total_marks_available = 0

#         if marks:
#             for mark in marks:
#                 total_marks_obtained += mark["mark_obtained"]
#                 total_marks_available += mark["maximum_marks"]
#                 mark_data = {
#                     "subject_code": mark["subject_code"],
#                     "subject_name": mark["subject_name"],
#                     "marks_obtained": mark["mark_obtained"],
#                     "total_marks": mark["maximum_marks"],
#                     "percentage": mark["percentage"]
#                 }

#                 if not student_details_added:
#                     student_data = student.copy()
#                     student_data.update(mark_data)
#                     data.append(student_data)
#                     student_details_added = True
#                 else:
#                     # Append only the marks information
#                     empty_student_data = {
#                         "name1": "",
#                         "status": "",
#                         "register_number": "",
#                         "gender": "",
#                         "phone_number": "",
#                         "department": "",
#                         "course": "",
#                         "date_of_birth": "",
#                     }
#                     empty_student_data.update(mark_data)
#                     data.append(empty_student_data)
#         else:
#             # No marks found, append student details with empty mark fields
#             student_data = {
#                 "name1": student["name1"],
#                 "status": student["status"],
#                 "register_number": student["register_number"],
#                 "gender": student["gender"],
#                 "phone_number": student["phone_number"],
#                 "department": student["department"],
#                 "course": student["course"],
#                 "date_of_birth": student["date_of_birth"],
#                 "subject_code": None,
#                 "subject_name": None,
#                 "marks_obtained": None,
#                 "total_marks": None,
#                 "percentage": None
#             }
#             data.append(student_data)

#         # Add total marks data to the student's first entry
#         if student_details_added:
#             data[-len(marks) if marks else 1]["total_marks_obtained"] = total_marks_obtained
#             data[-len(marks) if marks else 1]["total_marks_available"] = total_marks_available

#     return data

# def get_chart_data():
#     chart_data = {
#         "data": {
#             "labels": [],
#             "datasets": [
#                 {
#                     "name": _("Total Marks Obtained"),
#                     "values": []
#                 },
#                 {
#                     "name": _("Total Marks Available"),
#                     "values": []
#                 }
#             ]
#         },
#         "type": "bar",  # or "line", "pie", etc.
#         "height": 300
#     }
    
#     students = frappe.get_all("Student", fields=["register_number", "name1"])
    
#     for student in students:
#         total_marks_obtained = 0
#         total_marks_available = 0
        
#         marks = frappe.get_all("Mark", filters={"parent": student["register_number"]}, fields=["marks_obtained", "total_marks"])
        
#         for mark in marks:
#             total_marks_obtained += mark["marks_obtained"]
#             total_marks_available += mark["total_marks"]
        
#         chart_data["data"]["labels"].append(student["name1"])
#         chart_data["data"]["datasets"][0]["values"].append(total_marks_obtained)
#         chart_data["data"]["datasets"][1]["values"].append(total_marks_available)
    
#     return chart_data

# import frappe
# from frappe import _

# def execute(filters=None):
#     columns, data = get_columns(), get_data(filters)
#     chart = get_chart_data()
#     return columns, data, None, chart

# def get_columns():
#     return [
#         {"label": _("Student Name"), "fieldname": "name1", "fieldtype": "Data"},
#         {"label": _("Status"), "fieldname": "status", "fieldtype": "Data"},
#         {"label": _("Register Number"), "fieldname": "register_number", "fieldtype": "Data"},
#         {"label": _("Gender"), "fieldname": "gender", "fieldtype": "Data"},
#         {"label": _("Phone Number"), "fieldname": "phone_number", "fieldtype": "Data"},
#         {"label": _("Department"), "fieldname": "department", "fieldtype": "Data"},
#         {"label": _("Course"), "fieldname": "course", "fieldtype": "Data"},
#         {"label": _("Date of Birth"), "fieldname": "date_of_birth", "fieldtype": "Date"},
#         {"label": _("Subject Code"), "fieldname": "subject_code", "fieldtype": "Data"},
#         {"label": _("Subject Name"), "fieldname": "subject_name", "fieldtype": "Data"},
#         {"label": _("Marks Obtained"), "fieldname": "mark_obtained", "fieldtype": "Float"},
#         {"label": _("Total Marks"), "fieldname": "maximum_marks", "fieldtype": "Float"},
#         {"label": _("Percentage"), "fieldname": "percentage", "fieldtype": "Percent"},
#         {"label": _("Total Marks Obtained"), "fieldname": "total_marks_obtained", "fieldtype": "Float"},
#         {"label": _("Total Marks Available"), "fieldname": "total_marks_available", "fieldtype": "Float"},
#     ]

# def get_data(filters=None):
#     data = []
#     student_filters = {}

#     if filters:
#         if filters.get("register_number"):
#             student_filters["register_number"] = filters.get("register_number")
#         if filters.get("name1"):
#             student_filters["name1"] = filters.get("name1")
#         if filters.get("gender"):
#             student_filters["gender"] = filters.get("gender")
#         if filters.get("email"):
#             student_filters["email"] = filters.get("email")
#         if filters.get("phone_number"):
#             student_filters["phone_number"] = filters.get("phone_number")
#         if filters.get("department"):
#             student_filters["department"] = filters.get("department")
#         if filters.get("course"):
#             student_filters["course"] = filters.get("course")
#     #"name1", "status", "register_number", "gender", "phone_number", "department", "course", "date_of_birth"  subject_code", "subject_name", "mark_obtained", "maximum_marks", "percentage
#     students = frappe.get_all("Student", filters=student_filters, fields=["*"])

#     for student in students:
#         # Fetch marks for the student
#         marks = frappe.get_all("Mark", filters={"parent": student.name}, fields=["*"])
        
#         student_details_added = False
#         total_marks_obtained = 0
#         total_marks_available = 0

#         if marks:
#             for mark in marks:
#                 total_marks_obtained += mark["mark_obtained"]
#                 total_marks_available += mark["maximum_marks"]
#                 mark_data = {
#                     "subject_code": mark["subject_code"],
#                     "subject_name": mark["subject_name"],
#                     "mark_obtained": mark["mark_obtained"],
#                     "maximum_marks": mark["maximum_marks"],
#                     "percentage": mark["percentage"]
#                 }

#                 if not student_details_added:
#                     student_data = student.copy()
#                     student_data.update(mark_data)
#                     data.append(student_data)
#                     student_details_added = True
#                 else:
#                     # Append only the marks information
#                     empty_student_data = {
#                         "name1": "",
#                         "status": "",
#                         "register_number": "",
#                         "gender": "",
#                         "phone_number": "",
#                         "department": "",
#                         "course": "",
#                         "date_of_birth": "",
#                     }
#                     empty_student_data.update(mark_data)
#                     data.append(empty_student_data)
#         else:
#             # No marks found, append student details with empty mark fields
#             student_data = {
#                 "name1": student["name1"],
#                 "status": student["status"],
#                 "register_number": student["register_number"],
#                 "gender": student["gender"],
#                 "phone_number": student["phone_number"],
#                 "department": student["department"],
#                 "course": student["course"],
#                 "date_of_birth": student["date_of_birth"],
#                 "subject_code": None,
#                 "subject_name": None,
#                 "mark_obtained": None,
#                 "maximum_marks": None,
#                 "percentage": None
#             }
#             data.append(student_data)

#         # Add total marks data to the student's first entry
#         if student_details_added:
#             data[-len(marks) if marks else 1]["total_marks_obtained"] = total_marks_obtained
#             data[-len(marks) if marks else 1]["total_marks_available"] = total_marks_available

#     return data

# def get_chart_data():
#     chart_data = {
#         "data": {
#             "labels": [],
#             "datasets": [
#                 {
#                     "name": _("Total Marks Obtained"),
#                     "values": []
#                 },
#                 {
#                     "name": _("Total Marks Available"),
#                     "values": []
#                 }
#             ]
#         },
#         "type": "bar",  # or "line", "pie", etc.
#         "height": 300
#     }
    
#     students = frappe.get_all("Student", fields=["register_number", "name1"])
    
#     for student in students:
#         total_marks_obtained = 0
#         total_marks_available = 0
        
#         marks = frappe.get_all("Mark", filters={"parent": student.name}, fields=["mark_obtained", "maximum_marks"])
        
#         for mark in marks:
#             total_marks_obtained += mark["mark_obtained"]
#             total_marks_available += mark["maximum_marks"]
        
#         chart_data["data"]["labels"].append(student["name1"])
#         chart_data["data"]["datasets"][0]["values"].append(total_marks_obtained)
#         chart_data["data"]["datasets"][1]["values"].append(total_marks_available)
    
#     return chart_data

import frappe
from frappe import _

def execute(filters=None):
    columns, data = get_columns(), get_data(filters)
    chart = get_chart_data(filters)
    return columns, data, None, chart

def get_columns():
    return [
        {"label": _("Student Name"), "fieldname": "name1", "fieldtype": "Data"},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data"},
        {"label": _("Register Number"), "fieldname": "register_number", "fieldtype": "Data"},
        {"label": _("Gender"), "fieldname": "gender", "fieldtype": "Data"},
        {"label": _("Phone Number"), "fieldname": "phone_number", "fieldtype": "Data"},
        {"label": _("Department"), "fieldname": "department", "fieldtype": "Data"},
        {"label": _("Course"), "fieldname": "course", "fieldtype": "Data"},
        {"label": _("Date of Birth"), "fieldname": "date_of_birth", "fieldtype": "Date"},
        {"label": _("Subject Code"), "fieldname": "subject_code", "fieldtype": "Data"},
        {"label": _("Subject Name"), "fieldname": "subject_name", "fieldtype": "Data"},
        {"label": _("Marks Obtained"), "fieldname": "mark_obtained", "fieldtype": "Float"},
        {"label": _("Total Marks"), "fieldname": "maximum_marks", "fieldtype": "Float"},
        {"label": _("Percentage"), "fieldname": "percentage", "fieldtype": "Percent"},
        {"label": _("Total Marks Obtained"), "fieldname": "total_marks_obtained", "fieldtype": "Float"},
        {"label": _("Total Marks Available"), "fieldname": "total_marks_available", "fieldtype": "Float"},
    ]

def get_data(filters=None):
    data = []
    student_filters = {}

    # Apply all filters to the student_filters dictionary
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
            student_filters["phone_number"] = ["like", f"%{filters.get('phone_number')}%"]
        if filters.get("department"):
            student_filters["department"] = ["like", f"%{filters.get('department')}%"]
        if filters.get("course"):
            student_filters["course"] = ["like", f"%{filters.get('course')}%"]
        if filters.get("date_of_birth"):
            student_filters["date_of_birth"] = ["=", filters.get("date_of_birth")]

    # Fetch students based on the filters
    students = frappe.get_all("Student", filters=student_filters, fields=["*"])

    for student in students:
        # Fetch marks for each student based on the student name
        marks = frappe.get_all("Mark", filters={"parent": student.name}, fields=["*"])

        student_details_added = False
        total_marks_obtained = 0
        total_marks_available = 0

        if marks:
            for mark in marks:
                total_marks_obtained += mark["mark_obtained"]
                total_marks_available += mark["maximum_marks"]
                mark_data = {
                    "subject_code": mark["subject_code"],
                    "subject_name": mark["subject_name"],
                    "mark_obtained": mark["mark_obtained"],
                    "maximum_marks": mark["maximum_marks"],
                    "percentage": mark["percentage"]
                }

                if not student_details_added:
                    student_data = student.copy()
                    student_data.update(mark_data)
                    data.append(student_data)
                    student_details_added = True
                else:
                    empty_student_data = {
                        "name1": "",
                        "status": "",
                        "register_number": "",
                        "gender": "",
                        "phone_number": "",
                        "department": "",
                        "course": "",
                        "date_of_birth": "",
                    }
                    empty_student_data.update(mark_data)
                    data.append(empty_student_data)
        else:
            student_data = {
                "name1": student["name1"],
                "status": student["status"],
                "register_number": student["register_number"],
                "gender": student["gender"],
                "phone_number": student["phone_number"],
                "department": student["department"],
                "course": student["course"],
                "date_of_birth": student["date_of_birth"],
                "subject_code": None,
                "subject_name": None,
                "mark_obtained": None,
                "maximum_marks": None,
                "percentage": None
            }
            data.append(student_data)

        if student_details_added:
            data[-len(marks) if marks else 1]["total_marks_obtained"] = total_marks_obtained
            data[-len(marks) if marks else 1]["total_marks_available"] = total_marks_available

    return data

def get_chart_data(filters=None):
    chart_data = {
        "data": {
            "labels": [],
            "datasets": [
                {
                    "name": _("Total Marks Obtained"),
                    "values": []
                },
                {
                    "name": _("Total Marks Available"),
                    "values": []
                }
            ]
        },
        "type": "bar",
        "height": 300
    }

    student_filters = {}

    # Apply all filters to the student_filters dictionary
    if filters:
        if filters.get("register_number"):
            student_filters["register_number"] = filters.get("register_number")
        if filters.get("name1"):
            student_filters["name1"] = filters.get("name1")
        if filters.get("gender"):
            student_filters["gender"] = filters.get("gender")
        if filters.get("email"):
            student_filters["email"] = filters.get("email")
        if filters.get("phone_number"):
            student_filters["phone_number"] = filters.get("phone_number")
        if filters.get("department"):
            student_filters["department"] = filters.get("department")
        if filters.get("course"):
            student_filters["course"] = filters.get("course")

    # Fetch students based on the filters
    students = frappe.get_all("Student", filters=student_filters, fields=["register_number", "name1"])

    for student in students:
        total_marks_obtained = 0
        total_marks_available = 0

        # Fetch marks for each student based on the student register number
        marks = frappe.get_all("Mark", filters={"parent": student["register_number"]}, fields=["mark_obtained", "maximum_marks"])

        for mark in marks:
            total_marks_obtained += mark["mark_obtained"]
            total_marks_available += mark["maximum_marks"]

        chart_data["data"]["labels"].append(student["name1"])
        chart_data["data"]["datasets"][0]["values"].append(total_marks_obtained)
        chart_data["data"]["datasets"][1]["values"].append(total_marks_available)

    return chart_data
