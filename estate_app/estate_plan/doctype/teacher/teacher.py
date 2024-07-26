# your_custom_app/your_custom_app/doctype/teacher/teacher.py

import frappe
from frappe.model.document import Document

class Teacher(Document):
    def validate(self):
        # Custom validation logic
        pass

# Define fields
def init(self):
    self.add_field("teacher_id", fieldtype="Int")
    self.add_field("name", fieldtype="Data")
    self.add_field("designation", fieldtype="Data")
    self.add_field("date_of_birth", fieldtype="Date")
