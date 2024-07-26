// Copyright (c) 2024, Anna and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Extra Curricular", {
// 	refresh(frm) {

// 	},
// });
// frappe.ui.form.on('Extra Curricular', {
//     refresh: function(frm) {
//         // Add a custom button to fetch student details
//         frm.add_custom_button(__('Get Items From'), function() {
//             // Show a dialog to enter criteria
//             frappe.prompt([
//                 {fieldname: 'registration_number', label: 'Registration Number', fieldtype: 'Data'},
//                 {fieldname: 'name', label: 'Name', fieldtype: 'Data'},
//                 {fieldname: 'gender', label: 'Gender', fieldtype: 'Select', options: ['', 'Male', 'Female']},
//             ], function(values){
//                 frappe.call({
//                     method: 'get_student_details',
//                     args: {
//                         registration_number: values.registration_number,
//                         name: values.name,
//                         gender: values.gender
//                     },
//                     callback: function(r) {
//                         if (r.message) {
//                             frm.set_value('student_name', r.message.student_name);
//                             frm.set_value('gender', r.message.gender);
//                             frm.set_value('registration_number', r.message.registration_number);
//                             frappe.msgprint('Student details fetched successfully');
//                         } else {
//                             frappe.msgprint('No matching student found');
//                         }
//                     }
//                 });
//             }, 'Enter Criteria');
//         });
//     }
// });
