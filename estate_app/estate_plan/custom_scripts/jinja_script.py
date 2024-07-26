import frappe

@frappe.whitelist()
def get_registration_number(student):
    frappe.logger().info(f"Fetching registration number for student: {student}")
    return student.get('register_number', 'Not Available')

@frappe.whitelist()
def get_department(student):
    frappe.logger().info(f"Fetching department for student: {student}")
    return student.get('department', 'Not Available')

@frappe.whitelist()
def get_course(student):
    frappe.logger().info(f"Fetching course for student: {student}")
    return student.get('course', 'Not Available')

@frappe.whitelist()
def get_dob(student):
    frappe.logger().info(f"Fetching date of birth for student: {student}")
    return student.get('date_of_birth', 'Not Available')
