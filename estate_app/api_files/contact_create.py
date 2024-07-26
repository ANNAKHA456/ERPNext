import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def save_student_contact(register_number, student_name, email,mobile_number ):
    try:
        doc = frappe.get_doc({
            'doctype': 'Student Contact Details',
            'register_number': register_number,
            'student_name': student_name,
            'email': email,
            'mobile_number': mobile_number
        })
        doc.insert()
        frappe.db.commit()
        return 'success'
    except Exception as e:
        frappe.log_error(f'Error saving student contact details: {str(e)}')
        return 'failed'
