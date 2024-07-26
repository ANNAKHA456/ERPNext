import frappe
from frappe import _

@frappe.whitelist()
def create_teacher(teacher_id, name, designation):
    """
    Create a new Teacher record.
    """
    try:
        doc = frappe.get_doc({
            "doctype": "Teacher Details New",
            "teacher_id": teacher_id,
            "name1": name,
            "designation": designation
        })
        doc.insert()
        return {"status": "success", "message": _("Teacher created successfully"), "data": doc}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@frappe.whitelist()
def read_all_teachers():
    """
    Read all Teacher records.
    """
    try:
        teachers = frappe.get_all("Teacher Details New", fields=["teacher_id", "name1", "designation"])
        return {"status": "success", "data": teachers}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@frappe.whitelist()
def update_teacher(teacher_id, name):
    """
    Update a Teacher record.
    """
    try:
        doc = frappe.get_doc("Teacher Details New", teacher_id)
        print(doc)
        doc.name1 = name
        doc.designation = doc.designation
        doc.save()
        return {"status": "success", "message": _("Teacher updated successfully"), "data": doc}
    except frappe.DoesNotExistError:
        return {"status": "error", "message": _("Teacher not found")}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@frappe.whitelist()
def delete_teacher(teacher_id):
    """
    Delete a Teacher record.
    """
    try:
        frappe.delete_doc("Teacher Details New", teacher_id)
        return {"status": "success", "message": _("Teacher deleted successfully")}
    except frappe.DoesNotExistError:
        return {"status": "error", "message": _("Teacher not found")}
    except Exception as e:
        return {"status": "error", "message": str(e)}
