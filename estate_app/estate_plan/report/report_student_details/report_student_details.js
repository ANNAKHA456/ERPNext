// Copyright (c) 2024, Anna and contributors
// For license information, please see license.txt

frappe.query_reports["Report Student Details"] = {
	"filters": [
		{
            "fieldname": "register_number",
            "label": __("Register Number"),
            "fieldtype": "Link",
            "options": "Student",
        },
        {
            "fieldname": "name1",
            "label": __("Name"),
            "fieldtype": "Data",
			"options":""
        },
        {
            "fieldname": "date_of_birth",
            "label": __("Date of Birth"),
            "fieldtype": "Date",
			"options":""
        },
        {
            "fieldname": "gender",
            "label": __("Gender"),
            "fieldtype": "Select",
            "options": " \nMale\nFemale\nOther"
        },
        {
            "fieldname": "status",
            "label": __("Status"),
            "fieldtype": "Select",
            "options": " \nOpen\nCompleted"
        },
        {
            "fieldname": "email",
            "label": __("Email"),
            "fieldtype": "Data",
            "options": "",
        },
        {
            "fieldname": "phone_number",
            "label": __("Phone Number"),
            "fieldtype": "Data",
            "options": "",
        },
        {
            "fieldname": "department",
            "label": __("Department"),
            "fieldtype": "",
			"options":""
        },
        {
            "fieldname": "course",
            "label": __("Course"),
            "fieldtype": "",
			"options":""
        },

	]
};
