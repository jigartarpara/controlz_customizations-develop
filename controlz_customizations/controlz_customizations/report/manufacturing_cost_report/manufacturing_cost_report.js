// Copyright (c) 2025, Controlz Customizations and contributors
// For license information, please see license.txt

frappe.query_reports["Manufacturing Cost Report"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": "From",
			"fieldtype": "Date"
		},
		{
			"fieldname": "to_date",
			"label": "To",
			"fieldtype": "Date"
		}
	]
};
