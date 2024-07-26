frappe.query_reports["Student Reports"] = {
	"filters": [
		{
			"label": "Register Number",
				"fieldname": "register_number",
				  "fieldtype": "Link",
			"options":"Student",
				   "width": 200,
			"reqd": 0
			},
		{
			"label": "Name",
        		"fieldname": "name1",
          		"fieldtype": "Data",
			"options":"",
           		"width": 200,
			"reqd": 0
        	},
			
	]
}