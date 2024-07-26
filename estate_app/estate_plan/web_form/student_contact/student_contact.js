// frappe.ready(function() {
//     // Bind events here if needed


// frappe.ui.form.on('Student Contact Details', {
//     // Triggered after the form is saved successfully
//     onload_post_render: function(frm) {
//         frm.add_custom_button('Send Email', function() {
//             sendEmail(frm);
//         });
//     }
// });

// function sendEmail(frm) {
//     // Replace with your email subject and content
//     var subject = 'New Student Contact Details';
//     var message = 'A new student contact details record has been created:\n\n' +
//                   'Name: ' + frm.doc.student_name + '\n' +
//                   'Email: ' + frm.doc.email + '\n';

//     frappe.call({
//         method: 'send_email_from_form', // Replace with your server-side method
//         args: {
//             doc: frm.doc,
//             subject: subject,
//             message: message
//         },
//         callback: function(response) {
//             if (response && response.message === 'success') {
//                 frappe.msgprint('Email sent successfully.');
//             } else {
//                 frappe.msgprint('Failed to send email.');
//             }
//         }
//     });
// }
// });


