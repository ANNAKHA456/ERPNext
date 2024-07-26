// // Copyright (c) 2024, Anna and contributors
// // For license information, please see license.txt

// frappe.query_reports["Student Rep"] = {
// 	"filters": [
// 		{
//             "fieldname": "register_number",
//             "label": __("Register Number"),
//             "fieldtype": "Data",
//       
//             "reqd": 0,
//             "hidden": 0
//         },
//         {
//             "fieldname": "name1",
//             "label": __("Name"),
//             "fieldtype": "Data",
//             "options": "",
//            
//             "reqd": 0,
//             "hidden": 0
//         },
//         {
//             "fieldname": "date_of_birth",
//             "label": __("Date of Birth"),
//             "fieldtype": "Date",
//             "options": "",
//            
//             "reqd": 0,
//             "hidden": 0
//         },
//         {
//             "fieldname": "gender",
//             "label": __("Gender"),
//             "fieldtype": "Select",
//             "options": " \nMale\nFemale\nOther",
//           
//             "reqd": 0,
//             "hidden": 0
//         },
//         {
//             "fieldname": "status",
//             "label": __("Status"),
//             "fieldtype": "Select",
//             "options": " \nOpen\nCompleted",
//             
//             "reqd": 0,
//             "hidden": 0
//         },
//         {
//             "fieldname": "email",
//             "label": __("Email"),
//             "fieldtype": "Data",
//             "options": "",
//            
//             "reqd": 0,
//             "hidden": 0
//         },
//         {
//             "fieldname": "phone_number",
//             "label": __("Phone Number"),
//             "fieldtype": "Data",
//             "options": "",
//           
//             "reqd": 0,
//             "hidden": 0
//         },
//         {
//             "fieldname": "department",
//             "label": __("Department"),
//             "fieldtype": "",
//             "options": "",
//            
//             "reqd": 0,
//             "hidden": 0
//         },
//         {
//             "fieldname": "course",
//             "label": __("Course"),
//             "fieldtype": "",
//            
//             "reqd": 0,
//             "hidden": 0
//         },
//     ]

	
// };
frappe.query_reports["Student Rep"] = {
	"filters": [
		{
			"label": "Register Number",
				"fieldname": "register_number",
				  "fieldtype": "Link",
			"options":'Student',
				   "width": 200,
			"reqd": 0
			},
		{
			"label": "Name",
        		"fieldname": "name1",
          		"fieldtype": "Data",
			"options":'',
           		"width": 200,
			"reqd": 0
        	},
			{
				"label": "Course",
					"fieldname": "course",
					  "fieldtype": "Data",
				"options":'',
					   "width": 200,
				"reqd": 0
				},
				{
					"label": "Department",
						"fieldname": "department",
						  "fieldtype": "Data",
					"options":'',
						   "width": 200,
					"reqd": 0
					},
					{
						"label": "Subject Code",
							"fieldname": "subject_code",
							  "fieldtype": "Link",
						"options":'Subcode',
							   "width": 200,
						"reqd": 0
						},
				{
					"label": "Gender",
							"fieldname": "gender",
							  "fieldtype": "Select",
						"options":' \nFemale\nMale\nOthers',
							   "width": 200,
						"reqd": 0
				},
				{
					"label": "Date Of Birth",
							"fieldname": "date_of_birth",
							  "fieldtype": "Date",
						"options":'',
							   "width": 200,
						"reqd": 0
				},
				{
					"label": "Total Marks Obtained",
							"fieldname": "mark_obtained",
							  "fieldtype": "Float",
						"options":'',
							   "width": 200,
						"reqd": 0
				},
				{
					"label": "Grand Total",
							"fieldname": "maximum_marks",
							  "fieldtype": "Float",
						"options":'',
							   "width": 200,
						"reqd": 0
				}
			
	],
	//"get_chart_data": "apps/estate_app/estate_app/estate_plan/report/student_rep/student_rep.get_chart_data"
}