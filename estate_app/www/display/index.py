import frappe
def get_context(context):
    context.name="anna"
    print(f"\n\n{frappe.form_dict}")
    return context