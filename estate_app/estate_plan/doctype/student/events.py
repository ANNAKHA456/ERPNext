import frappe

@frappe.whitelist()
def fetch_student_data(student_id):
    try:
        # Fetch student data
        student = frappe.get_doc("Student", student_id)
        
        # Prepare data for Personal Details of Students
        personal_details_data = {
            "register_number": student.register_number,
            "student_name": student.name1,
            "mobile_number": student.phone_number,
            "date_of_birth": student.date_of_birth,
        }
        
        return personal_details_data
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "fetch_student_data Error")
        return frappe.throw(str(e))
