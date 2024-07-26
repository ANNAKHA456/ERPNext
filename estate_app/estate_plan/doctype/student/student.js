// frappe.ui.form.on('Student', {
// 	refresh(frm) {
// 		var dob = frm.doc.date_of_birth;
//         if (dob) {
//             var today = frappe.datetime.now_date();
//             var age = frappe.datetime.get_diff(today, dob) / 365.25;
            
//             if (dob > today) {
//                 frappe.msgprint(('Date of Birth cannot be in the future'));
//                 frappe.validated = false;
//             } else if (age > 120) {
//                 frappe.msgprint(('Date of Birth indicates an age greater than 120 years'));
//                 frappe.validated = false;
//             }
            
//         }
//         var email = frm.doc.email;
//         if (email) {
//             // Regular expression for basic email validation
//             var email_pattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
//             if (!email_pattern.test(email)) {
//                 frappe.msgprint(('Please enter a valid email address'));
//                 frappe.validated = false;
//             }
//         }
//         var phone = frm.doc.phone_number;
//         if (phone) {
//             // Regular expression for basic phone number validation
//             var phone_pattern = /^[0-9]{10}$/; // Adjust the regex pattern according to your requirements
//             if (!phone_pattern.test(phone)) {
//                 frappe.msgprint(('Please enter a valid phone number with 10 digits'));
//                 frappe.validated = false;
//             }
//         }
// 	}
// })
frappe.ui.form.on('Student', {
    // refresh: function(frm) {
    //     if (!frm.doc.__islocal) {
    //         frm.add_custom_button(__('Add Personal Details'), function() {
    //             // Call server-side method to create or update personal details
    //             frappe.call({
    //                 method: 'estate_app.estate_plan.doctype.student.add_personal_details',
    //                 args: {
    //                     student_id: frm.doc.name1,
    //                     register_no: frm.doc.register_no
    //                 },
    //                 callback: function(r) {
    //                     if (r.message) {
    //                         frappe.msgprint(r.message);
    //                         frm.reload_doc();
    //                     }
    //                 }
    //             });
    //         });
    //     }
    // },
    gender: function(frm) {
        // Check if a gender is selected
        if (frm.doc.gender) {
            // Display an alert
            frappe.msgprint(`Gender is selected as ${frm.doc.gender}`);
        }
    },
    validate: function(frm) {
        let error_messages = [];
        validate_dob(frm, error_messages);
        validate_phone(frm, error_messages);
        validate_email(frm, error_messages);

        if (error_messages.length > 0) {
            frappe.throw(error_messages.join('<br>'));
        }
    }
});

function validate_dob(frm, error_messages) {
    if (frm.doc.date_of_birth) {
        let today = frappe.datetime.get_today();
        if (frm.doc.date_of_birth >=today) {
            error_messages.push("Date of Birth cannot be in the future or today");
        }

        let dob = new Date(frm.doc.date_of_birth);
        let age = (new Date() - dob) / (365.25 * 24 * 60 * 60 * 1000);
        if (age > 120) {
            error_messages.push("Date of Birth indicates an age greater than 120 years");
        }
    }
}

function validate_phone(frm, error_messages) {
    if (frm.doc.phone_number) {
        let phone_pattern = /^[0-9]{10}$/;  // Adjust the regex pattern according to your requirements
        if (!phone_pattern.test(frm.doc.phone_number)) {
            error_messages.push("Please enter a valid phone number with 10 digits");
        }
    }
}

function validate_email(frm, error_messages) {
    if (frm.doc.email) {
        let email_pattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!email_pattern.test(frm.doc.email)) {
            error_messages.push("Please enter a valid email address");
        }
    }
}





// frappe.ui.form.on('Student', {
//     // refresh: function(frm) {
//     //     if (!frm.doc.__islocal) {
//     //         frm.add_custom_button(__('Add Personal Details'), function() {
//     //             frappe.call({
//     //                 method: 'estate_app.estate_plan.doctype.student.student.add_personal_details',
//     //                 args: {
//     //                     register_no: frm.doc.register_number
//     //                 },
//     //                 callback: function(r) {
//     //                     if (r.message) {
//     //                         frappe.msgprint(r.message, function() {
//     //                             // After the message is displayed, refresh the form
//     //                             if(r.docname){
//     //                                 console.log(r.docname)
//     //                             frappe.set_route("Form","Personal Details Of Students", r.message.docname);}
//     //                             else{
//     //                             frm.reload_doc();}
//     //                         });
//     //                     }
//     //                 }
//     //             });
//     //         });
//     //     }
//     // },
//     validate: function(frm) {
//         let error_messages = [];
//         validate_dob(frm, error_messages);
//         validate_phone(frm, error_messages);
//         validate_email(frm, error_messages);

//         if (error_messages.length > 0) {
//             frappe.throw(error_messages.join('<br>'));
//         }
//     }
// });

// function validate_dob(frm, error_messages) {
//     if (frm.doc.date_of_birth) {
//         let today = frappe.datetime.get_today();
//         if (frm.doc.date_of_birth >= today) {
//             error_messages.push("Date of Birth cannot be in the future or today");
//         }

//         let dob = new Date(frm.doc.date_of_birth);
//         let age = (new Date() - dob) / (365.25 * 24 * 60 * 60 * 1000);
//         if (age > 120) {
//             error_messages.push("Date of Birth indicates an age greater than 120 years");
//         }
//     }
// }

// function validate_phone(frm, error_messages) {
//     if (frm.doc.phone_number) {
//         let phone_pattern = /^[0-9]{10}$/;
//         if (!phone_pattern.test(frm.doc.phone_number)) {
//             error_messages.push("Please enter a valid phone number with 10 digits");
//         }
//     }
// }

// function validate_email(frm, error_messages) {
//     if (frm.doc.email) {
//         let email_pattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
//         if (!email_pattern.test(frm.doc.email)) {
//             error_messages.push("Please enter a valid email address");
//         }
//     }
// }
// frappe.ui.form.on('Student', {
//     validate: function(frm) {
//         let error_messages = [];
//         validate_dob(frm, error_messages);
//         validate_phone(frm, error_messages);
//         validate_email(frm, error_messages);

//         if (error_messages.length > 0) {
//             frappe.msgprint({
//                 title: __('Validation Error'),
//                 message: error_messages.join('<br>'),
//                 indicator: 'red',
//                 primary_action: {
//                     label: __('Enter Correct Email'),
//                     action: function() {
//                         prompt_correct_email(frm);
//                     }
//                 }
//             });
//             // Return false to prevent saving the form if validation fails
//             frappe.validated = false;
//         }
//     }
// });

// function validate_dob(frm, error_messages) {
//     if (frm.doc.date_of_birth) {
//         let today = frappe.datetime.get_today();
//         if (frm.doc.date_of_birth >= today) {
//             error_messages.push("Date of Birth cannot be in the future or today");
//         }

//         let dob = new Date(frm.doc.date_of_birth);
//         let age = (new Date() - dob) / (365.25 * 24 * 60 * 60 * 1000);
//         if (age > 120) {
//             error_messages.push("Date of Birth indicates an age greater than 120 years");
//         }
//     }
// }

// function validate_phone(frm, error_messages) {
//     if (frm.doc.phone_number) {
//         let phone_pattern = /^[0-9]{10}$/;
//         if (!phone_pattern.test(frm.doc.phone_number)) {
//             error_messages.push("Please enter a valid phone number with 10 digits");
//         }
//     }
// }

// function validate_email(frm, error_messages) {
//     if (frm.doc.email) {
//         let email_pattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
//         if (!email_pattern.test(frm.doc.email)) {
//             error_messages.push("Please enter a valid email address");
//         }
//     }
// }

// function prompt_correct_email(frm) {
//     frappe.prompt([
//         {
//             fieldname: 'correct_email',
//             fieldtype: 'Data',
//             label: 'Enter Correct Email',
//             reqd: true,
//             description: 'Please enter a valid email address'
//         }
//     ], function(values) {
//         // Update the email field with the correct email entered by the user
//         frm.set_value('email', values.correct_email);
//         frm.save();  // Optionally save the form after updating the email
//     }, __('Enter Correct Email'), __('Update'));
// }
// frappe.ui.form.on('Student', {
//     refresh: function(frm) {
//         frm.add_custom_button(__('Fetch Personal Details using API'), function() {
//             frappe.call({
//                 method: 'estate_app.estate_plan.doctype.student.events.fetch_student_data',
//                 args: {
//                     student_id: frm.doc.name
//                 },
//                 callback: function(r) {
//                     if (r.message) {
//                         frappe.msgprint(__('Personal Details of Student created: {0}', [r.message]));
//                     }
//                 }
//             });
//         });
//     }
// });
