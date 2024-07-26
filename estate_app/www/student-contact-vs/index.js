// // student-details.js

// function saveStudentDetails() {
//     var student_name = document.getElementById('student_name').value;
//     var email = document.getElementById('email').value;
//     var phone = document.getElementById('phone').value;

//     // Ensure frappe object is defined
//     if (typeof frappe !== 'undefined') {
//         frappe.call({
//             method: 'estate_app.api_file.contact_create.create_student_contact_details',
//             args: {
//                 student_name: student_name,
//                 email: email,
//                 phone: phone
//             },
//             callback: function(response) {
//                 if (response && response.message === "success") {
//                     alert('Student details saved successfully!');
//                 } else {
//                     alert('Failed to save student details.');
//                 }
//             }
//         });
//     } else {
//         console.error('Frappe is not loaded.');
//         alert('Error: Frappe is not loaded.');
//     }
// }

function saveStudentDetails() {
    var registerNumber = document.getElementById('register_number').value;
    var studentName = document.getElementById('student_name').value;
    var email = document.getElementById('email').value;
    var phone = document.getElementById('phone').value;

    frappe.call({
        method: 'estate_app.api_files.contact_create.save_student_contact',
        args: {
            register_number: registerNumber,
            student_name: studentName,
            email: email,
            mobile_number: phone
        },
        callback: function(response) {
            if (response.message === 'success') {
                frappe.msgprint('Student contact details saved successfully.');
            } else {
                console.log(response.message)
                frappe.msgprint('Failed to save student contact details.');
            }
        }
    });
}
