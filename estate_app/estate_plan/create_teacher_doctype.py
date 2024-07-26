# import frappe

# def create_teacher_doctype():
#     # Connect to the Frappe site
#     frappe.init(site='demo01.com')  # Initialize Frappe with your site name
    
#     if not frappe.db.exists('DocType', 'Teacher'):
#         # Create a new DocType
#         doc = frappe.new_doc('DocType')
#         doc.name = 'Teacher'
#         doc.module = 'ESTATE PLAN'  # Replace with your module name if needed
#         doc.custom = 1  # Indicates that this is a custom DocType
#         doc.istable = 0  # Not a child table
#         doc.is_tree = 0  # Not a tree structure
        
#         # Add fields to the DocType
#         fields = [
#             {
#                 'fieldname': 'teacher_name',  # Use a different fieldname
#                 'label': 'Teacher Name',
#                 'fieldtype': 'Data',
#                 'reqd': 1,
#             },
#             {
#                 'fieldname': 'subject',
#                 'label': 'Subject',
#                 'fieldtype': 'Data',
#                 'reqd': 1,
#             },
#             {
#                 'fieldname': 'salary',
#                 'label': 'Salary',
#                 'fieldtype': 'Currency',
#                 'reqd': 1,
#             },
#             {
#                 'fieldname': 'designation',
#                 'label': 'Designation',
#                 'fieldtype': 'Data',
#                 'reqd': 1,
#             },
#         ]
        
#         # Set the autoname based on a field that uniquely identifies each document
#         #doc.autoname = 'field:teacher_name'
        
#         for field in fields:
#             doc.append('fields', field)
        
#         # Save the new DocType
#         doc.insert()
#         frappe.db.commit()
#         print('Teacher DocType created successfully')
#     else:
#         print('Teacher DocType already exists')

#     # Disconnect from the Frappe site
#     frappe.destroy()

# # Call the function to create the DocTypecreate_teacher_doctype()
