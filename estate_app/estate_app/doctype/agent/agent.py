# Copyright (c) 2024, Anna and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AGENT(Document):
    def before_save(self):
        self.display_current_user_info()

    def display_current_user_info(self):
        current_user_email = frappe.session.user
        enabled_status = frappe.get_value("User", current_user_email, "enabled")
        frappe.msgprint(f"Current User Email: {current_user_email}, Enabled Status: {enabled_status}")
