# import frappe

# def get_next_approver(current_approver_email):
#     # Define the hierarchy with emails
#     hierarchy = ['ashaeapen05@gmail.com', 'neha@acubeapp.com', 'annakhamaria98@gmail.com']
    
#     # Find the current approver index
#     try:
#         current_index = hierarchy.index(current_approver_email)
#     except ValueError:
#         # If the current approver is not found in the hierarchy, return None
#         frappe.log_error(f"Current approver {current_approver_email} not found in hierarchy")
#         return None
    
#     # Check the next approvers in the hierarchy
#     for next_index in range(current_index + 1, len(hierarchy)):
#         next_approver = hierarchy[next_index]
#         user_status = frappe.db.get_value('User', {'email': next_approver}, 'enabled')
#         if user_status:
#             return next_approver
    
#     # If no enabled approver is found, return None
#     return None

# @frappe.whitelist()
# def approve(doc, method):
#     frappe.log_error("Approve function called")
#     current_user_email = frappe.session.user
#     current_user_enabled = frappe.db.get_value('User', {'email': current_user_email}, 'enabled')
#     frappe.log_error(f"Current user: {current_user_email}, Enabled: {current_user_enabled}")
    
#     if current_user_enabled:
#         doc.workflow_state = f'Approved by {current_user_email}'
#         doc.save()
#         frappe.msgprint(f"Document approved by {current_user_email}")
#     else:
#         next_approver = get_next_approver(current_user_email)
        
#         if next_approver:
#             frappe.log_error(f"Next approver: {next_approver}")
#             frappe.msgprint(f"Approval request sent to {next_approver}")
#             # Notify the next approver
#             frappe.sendmail(recipients=next_approver, subject='Document Approval', message='Please review and approve the document.')
#         else:
#             frappe.throw('No next approver found or all next approvers are disabled.')

import frappe

def get_next_approver(current_approver_email):
    # Define the hierarchy with emails
    hierarchy = ['ashaeapen05@gmail.com', 'neha@acubeapp.com', 'annakhamaria98@gmail.com']
    
    # Find the current approver index
    try:
        current_index = hierarchy.index(current_approver_email)
    except ValueError:
        # If the current approver is not found in the hierarchy, return None
        frappe.log_error(f"Current approver {current_approver_email} not found in hierarchy")
        return None
    
    # Check the next approvers in the hierarchy
    for next_index in range(current_index + 1, len(hierarchy)):
        next_approver = hierarchy[next_index]
        user_status = frappe.db.get_value('User', {'email': next_approver}, 'enabled')
        if user_status:
            return next_approver
    
    # If no enabled approver is found, return None
    return None

@frappe.whitelist()
def approve(doc, method):
    frappe.log_error("Approve function called")
    current_user_email = frappe.session.user
    current_user_enabled = frappe.db.get_value('User', {'email': current_user_email}, 'enabled')
    frappe.log_error(f"Current user: {current_user_email}, Enabled: {current_user_enabled}")
    
    if not current_user_enabled:
        frappe.throw(f"Current user {current_user_email} is not enabled.")
    
    doc.workflow_state = f'Approved by {current_user_email}'
    doc.save()
    frappe.msgprint(f"Document approved by {current_user_email}")
    
    next_approver = get_next_approver(current_user_email)
    
    if next_approver:
        frappe.log_error(f"Next approver: {next_approver}")
        frappe.msgprint(f"Approval request sent to {next_approver}")
        # Notify the next approver
        #frappe.sendmail(recipients=next_approver, subject='Document Approval', message='Please review and approve the document.')
    else:
        frappe.msgprint('No next approver found or all next approvers are disabled.')
