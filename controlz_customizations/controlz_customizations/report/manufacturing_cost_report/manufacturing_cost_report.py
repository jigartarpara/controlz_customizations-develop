# Copyright (c) 2025, Controlz Customizations and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [
        {"label": "Stock Entry", "fieldname": "stock_entry", "fieldtype": "Link", "options": "Stock Entry", "width": 300},
        {"label": "Posting Date", "fieldname": "posting_date", "fieldtype": "Date", "width": 350},
        {"label": "FG Item", "fieldname": "fg_item", "fieldtype": "Link", "options": "Item", "width": 300},
        {"label": "FG Value", "fieldname": "fg_value", "fieldtype": "Float", "width": 180},
        {"label": "Part Value", "fieldname": "part_value", "fieldtype": "Float", "width": 180},
        {"label": "Scrap Value", "fieldname": "scrap_value", "fieldtype": "Float", "width": 180},
    ]
	data = get_data(filters)
	return columns, data

def get_data(filters):
	filters = {
		"docstatus": 1,
		"stock_entry_type": "Manufacture",
	}
	if filters.get("from_date"):
		filters["posting_date"] = [">=", filters["from_date"]]
	if filters.get("to_date"):
		filters["posting_date"] = ["<=", filters["to_date"]]
	data = frappe.get_all("Stock Entry",filters)
	final_output = []
	for row in data:
		stock_entry = frappe.get_doc("Stock Entry", row["name"])
		part_value = 0.0
		fg_item = ""
		fg_value = 0.0
		scrap_value = 0.0
		for item in stock_entry.items:
			if item.idx != 1:
				if item.is_finished_item:
					fg_item = item.item_code
					fg_value = item.basic_rate
				elif item.is_scrap_item:
					scrap_value = item.basic_rate
				else:
					part_value += item.basic_rate


		final_output.append({
			"stock_entry": stock_entry.name,
			"posting_date": stock_entry.posting_date,
			"fg_item": fg_item,
			"fg_value": fg_value,
			"part_value": part_value,
			"scrap_value": scrap_value
		})

	return final_output