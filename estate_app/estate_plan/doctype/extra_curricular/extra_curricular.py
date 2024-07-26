# Copyright (c) 2024, Anna and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ExtraCurricular(Document):
	pass


'''@frappe.whitelist()
def get_student_details(registration_number=None, name=None, gender=None):
    filters = {}
    if registration_number:
        filters["register_name"] = registration_number
    if name:
        filters["name1"] = name
    if gender:
        filters["gender"] = gender

    # Fetch student details based on the provided criteria
    student = frappe.get_value("Student", filters, ["name1 as student_name", "gender", "register_name as registration_number"], as_dict=True)
    
    return student'''
