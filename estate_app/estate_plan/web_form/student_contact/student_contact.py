# import frappe

# def get_context(context):
# 	# do your magic here
# 	pass
# In your custom app (e.g., estate_plan)

import frappe
from frappe import _

@frappe.whitelist()
def send_email_from_form(doc, subject, message):
    try:
        # Construct email parameters
        recipients = doc.get('email')
        
        # Send email using frappe's email utility
        frappe.sendmail(recipients=recipients, subject=subject, message=message)
        
        return 'success'
    except Exception as e:
        frappe.log_error(_('Failed to send email: {0}').format(str(e)))
        return 'failed'

def get_context(context):
    # Initialize an empty context dictionary
    context = {}

    # Populate the context dictionary with necessary data
    # Example:
    context['title'] = 'Student Contact Details'

    # Return the populated context dictionary
    return context
