# custom_app/www/student_profile.py

import frappe

def get_context(context):
    student_name = frappe.form_dict.name1
    # Fetch the student document using the student name
    student_doc = frappe.get_all('Student', filters={'register number': student_name}, fields=['*'])
    
    if student_doc:
        context.student = student_doc[0]
    else:
        frappe.throw(f'Student {student_name} not found', frappe.PageNotFoundError)
    
    return context
