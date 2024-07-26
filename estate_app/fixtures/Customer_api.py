import frappe

@frappe.whitelist(allow_guest=True)
def get_doctype_data():
    data = frappe.db.get_all("Lead")
    return data