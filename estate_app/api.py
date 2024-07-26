import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_logged_user():
    print("hi")
    return frappe.session.user
