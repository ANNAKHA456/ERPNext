# import frappe

# def execute():
#     pass
        
#         filters = {}

#     query, params = get_query(filters)
#     data = frappe.db.sql(query, params, as_dict=True)
    
#     columns = [
#         {"fieldname": "register_number", "label": "Register Number", "fieldtype": "Link"},
#         {"fieldname": "name1", "label": "Name", "fieldtype": "Data"},
#         {"fieldname": "date_of_birth", "label": "Date of Birth", "fieldtype": "Date"},
#         {"fieldname": "gender", "label": "Gender", "fieldtype": "Data"},
#         {"fieldname": "status", "label": "Status", "fieldtype": "Select"},
#         {"fieldname": "email", "label": "Email", "fieldtype": "Data"},
#         {"fieldname": "phone_number", "label": "Phone Number", "fieldtype": "Data"},
#         {"fieldname": "department", "label": "Department", "fieldtype": "Data"},
#         {"fieldname": "course", "label": "Course", "fieldtype": "Data"},
#         {"fieldname": "marks", "label": "Marks", "fieldtype": "Table"},
#         {"fieldname": "amended_from", "label": "Amended From", "fieldtype": "Data"}
#     ]

#     return columns, data

# def get_query(filters):
#     conditions = []

#     if filters.get("register_number"):
#         conditions.append("register_number = %(register_number)s")
#     if filters.get("name1"):
#         conditions.append("name = %(name1)s")
#     if filters.get("date_of_birth"):
#         conditions.append("date_of_birth = %(date_of_birth)s")
#     if filters.get("gender"):
#         conditions.append("gender = %(gender)s")
#     if filters.get("status"):
#         conditions.append("status = %(status)s")
#     if filters.get("email"):
#         conditions.append("email = %(email)s")
#     if filters.get("phone_number"):
#         conditions.append("phone_number = %(phone_number)s")
#     if filters.get("department"):
#         conditions.append("department = %(department)s")
#     if filters.get("course"):
#         conditions.append("course = %(course)s")
#     if filters.get("marks"):
#         conditions.append("marks = %(marks)s")
#     if filters.get("amended_from"):
#         conditions.append("amended_from = %(amended_from)s")

#     where_clause = " AND ".join(conditions) if conditions else "1=1"

#     query = f"""
#         SELECT 
#             register_number,
#             name AS name1,
#             date_of_birth,
#             gender,
#             status,
#             email,
#             phone_number,
#             department,
#             course,
#             marks,
#             amended_from
#         FROM 
#             `tabStudent`
#         WHERE {where_clause}
#     """
    
#     return query, filters

# from __future__ import unicode_literals
# import frappe

# def execute(filters):
#     columns, data = get_columns(), get_data(filters)
#     return columns, data

# def get_columns():
#     return [
#         {"fieldname": "register_number", "label": "Register Number", "fieldtype": "Data", "width": 100},
#         {"fieldname": "name1", "label": "Name", "fieldtype": "Data", "width": 150},
#         {"fieldname": "date_of_birth", "label": "Date of Birth", "fieldtype": "Date", "width": 100},
#         {"fieldname": "gender", "label": "Gender", "fieldtype": "Data", "width": 100},
#         {"fieldname": "status", "label": "Status", "fieldtype": "Data", "width": 100},
#         {"fieldname": "email", "label": "Email", "fieldtype": "Data", "width": 150},
#         {"fieldname": "phone_number", "label": "Phone Number", "fieldtype": "Data", "width": 100},
#         {"fieldname": "department", "label": "Department", "fieldtype": "Data", "width": 150},
#         {"fieldname": "course", "label": "Course", "fieldtype": "Data", "width": 150},
#         {"fieldname": "marks", "label": "Marks", "fieldtype": "Data", "width": 100},
#         {"fieldname": "amended_from", "label": "Amended From", "fieldtype": "Data", "width": 100},
#     ]

# def get_data(filters):
#     conditions = ""
#     values = {}

#     if filters.get("register_number"):
#         conditions += " AND register_number = %(register_number)s"
#         values["register_number"] = filters["register_number"]
#     if filters.get("name1"):
#         conditions += " AND name1 LIKE %(name1)s"
#         values["name1"] = "%" + filters["name1"] + "%"
#     if filters.get("date_of_birth"):
#         conditions += " AND date_of_birth = %(date_of_birth)s"
#         values["date_of_birth"] = filters["date_of_birth"]
#     if filters.get("gender"):
#         conditions += " AND gender = %(gender)s"
#         values["gender"] = filters["gender"]
#     if filters.get("status"):
#         conditions += " AND status = %(status)s"
#         values["status"] = filters["status"]
#     if filters.get("email"):
#         conditions += " AND email LIKE %(email)s"
#         values["email"] = "%" + filters["email"] + "%"
#     if filters.get("phone_number"):
#         conditions += " AND phone_number LIKE %(phone_number)s"
#         values["phone_number"] = "%" + filters["phone_number"] + "%"
#     if filters.get("department"):
#         conditions += " AND department LIKE %(department)s"
#         values["department"] = "%" + filters["department"] + "%"
#     if filters.get("course"):
#         conditions += " AND course LIKE %(course)s"
#         values["course"] = "%" + filters["course"] + "%"
#     if filters.get("marks"):
#         conditions += " AND marks = %(marks)s"
#         values["marks"] = filters["marks"]
#     if filters.get("amended_from"):
#         conditions += " AND amended_from LIKE %(amended_from)s"
#         values["amended_from"] = "%" + filters["amended_from"] + "%"

#     query = """
#         SELECT 
#             register_number, name1, date_of_birth, gender, status, email, phone_number,
#             department, course, marks, amended_from
#         FROM 
#             `tabStudents`
#         WHERE
#             1 = 1
#             {conditions}
#     """.format(conditions=conditions)

#     data = frappe.db.sql(query, values, as_dict=True)
#     return data
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
        {"label": "Marks Obtained", "fieldname": "marks_obtained", "fieldtype": "Data"},
        {"label": "Total Mark", "fieldname": "total_mark", "fieldtype": "Data"},
        {"label": "Percentage", "fieldname": "percentage", "fieldtype": "Data"}
    ]

    data = []

    student_filters = {}
    row={}
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
                "subject_code": mark.subject_code,
                "subject_name": mark.subject_name,
                # "total_mark": mark.total_mark,
                # "percentage": mark.percentage
            }
        data.append(row)

    return columns, data
