# # In /home/anakha/frappe-bench03/apps/estate_app/estate_app/tasks.py

# import frappe
# from frappe.core.doctype.communication.email import make
# import logging

# def send_weekly_email():
#     logging.info("Starting send_weekly_email function.")
#     students = frappe.get_all("Student", fields=["email", "name1"])
#     logging.info(f"Found {len(students)} students.")
    
#     for student in students:
#         logging.info(f"Processing student: {student.name1}, Email: {student.email}")
#         if student.email:
#             subject = "Wishing You a Joyful Holiday!"
#             message = f"Dear {student.name1},<br><br>Wishing you a joyful holiday!<br><br>Best Regards,<br>Your School"
#             send_email(student.email, subject, message)

# def send_email(recipient, subject, message):
#     try:
#         logging.info(f"Sending email to: {recipient}")
#         make(
#             recipients=recipient,
#             subject=subject,
#             content=message,
#             communication_medium="Email",
#             send_email=True
#         )
#         logging.info("Email sent successfully.")
#     except Exception as e:
#         logging.error(f"Failed to send email to {recipient}: {e}")


import frappe
# from frappe.core.doctype.communication.email import make
import logging
def send_notifications():
    msg = "Your message here"
    print("Entering the function")
    # logging.basicConfig(level=logging.DEBUG, filename='/home/frappe/frappe-bench03/logs/send_notifications.log')
    logging.debug("send_notifications function started.")
    
    try:
        # Fetch all student email addresses
        students = frappe.get_all('Student', fields=["name1",'email'])
        print(f"Getting emails {students[0]}")
        logging.debug(f"Found {len(students)} students.")
        
        for student in students:
            print("inside for")
            if student.email:
                # make(subject="Email Subject",
                #      content=msg,
                #      recipients=student.email,
                #      send_email=True,
                #      sender="annakhaprojects@gmail.com")
                frappe.sendmail(
                    recipients=[student.email],
                    subject="Weekly email notification",
                    message="Have a great day",
                    reference_doctype="Student",
                    reference_name=student.name1,
                    now=True 
                )
                print(f"Email sent to {student.email}")
        
        print("Emails sent successfully to all students")
    except Exception as e:
        frappe.msgprint(f"Could not send emails: {e}")
        logging.error(f"Error: {e}")
