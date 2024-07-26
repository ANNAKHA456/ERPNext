# # Copyright (c) 2024, Anna and contributors
# # For license information, please see license.txt

# # import frappe
# """from frappe.model.document import Document
# import frappe
# import re
# from frappe.utils import today, date_diff

# class Student(Document):
#     def validate(self):
#         self.validate_date_of_birth()
#         self.validate_phone_number()
#         self.validate_email()

#     def validate_date_of_birth(self):
#         if self.date_of_birth:
#             if self.date_of_birth > today():
#                 frappe.throw(("Date of Birth cannot be in the future"))
#             if date_diff(today(), self.date_of_birth) / 365.25 > 120:
#                 frappe.throw(("Date of Birth indicates an age greater than 120 years"))

#     def validate_phone_number(self):
#         if self.phone_number:
#             phone_pattern = r'^[0-9]{10}$'  # Adjust the regex pattern according to your requirements
#             if not re.match(phone_pattern, self.phone_number):
#                 frappe.throw(("Please enter a valid phone number with 10 digits"))

#     def validate_email(self):
#         if self.email:
#             email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#             if not re.match(email_pattern, self.email):
#                 frappe.throw(("Please enter a valid email address"))"""

from frappe.model.document import Document
import frappe
import re
from frappe.utils import today, date_diff

class Student(Document):
    def validate(self):
        error_messages = []
        # self.validate_date_of_birth(error_messages)
        self.validate_phone_number(error_messages)
        self.validate_email(error_messages)

        if error_messages:
            error_message_str = "<br>".join(error_messages)
            frappe.throw(error_message_str)

    def after_insert(self):
        self.send_welcome_email()

    def after_save(self):
        self.check_completion_status()

    def validate_date_of_birth(self, error_messages):
        if self.date_of_birth:
            if self.date_of_birth > today():
                error_messages.append("Date of Birth cannot be in the future or today from Python")
            if date_diff(today(), self.date_of_birth) / 365.25 > 120:
                error_messages.append("Date of Birth indicates an age greater than 120 years")

    def validate_phone_number(self, error_messages):
        if self.phone_number:
            phone_pattern = r'^[0-9]{10}$'  # Adjust the regex pattern according to your requirements
            if not re.match(phone_pattern, self.phone_number):
                error_messages.append("Please enter a valid phone number with 10 digits")

    def validate_gender(self):
        if self.gender:
            frappe.msgprint(f"Gender selected from python: {self.gender}")

    def validate_email(self, error_messages):
        if self.email:
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, self.email):
                error_messages.append("Please enter a valid email address")

    def send_welcome_email(self):
        if not self.email:
            frappe.msgprint("Email not provided for the student.")
            return

        subject = "Welcome to Our Institute"
        message = f"""
        Dear {self.name1},

        Welcome to our institute! Your registration number is {self.register_number}.

        Best Regards,
        The Institute Team
        """

        try:
            frappe.sendmail(
                recipients=[self.email],
                subject=subject,
                message=message,
                now=True
            )
            frappe.msgprint(f"Email sent to {self.email}")
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Email Sending Failed")
            frappe.throw(f"An error occurred while sending the email: {str(e)}")

    def check_completion_status(self):
        required_fields = [
            'register_number',
            'name',
            'date_of_birth',
            'gender',
            'email',
            'phone_number',
            'department',
            'course',
            'marks'
        ]

        all_fields_filled = True

        for field in required_fields:
            if not getattr(self, field):
                all_fields_filled = False

        if all_fields_filled:
            self.status = 'Completed'
        else:
            self.status = 'Saved'
        self.save()

# @frappe.whitelist()
# def add_personal_details(register_no):
#     # Check if personal details document exists for this student
#     personal_details = frappe.get_all('Personal Details Of Students', filters={'register_number': register_no}, limit=1)
    
#     if not personal_details:
#         # Create a new Personal Details document
#         personal_details_doc = frappe.new_doc("Personal Details Of Students")
#         #personal_details_doc.student = student_id
#         personal_details_doc.register_number = register_no
#         personal_details_doc.insert()
        
#         return {"message": "New personal details added.", "docname": personal_details_doc.register_number}
#     else:
#         # Update existing Personal Details
#         personal_details_doc = frappe.get_doc("Personal Details Of Students", personal_details[0].name)
#         personal_details_doc.register_number = register_no
#         personal_details_doc.save()
        
#         return {"message":"Update Existing","docname":personal_details_doc.name}
