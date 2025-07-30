# Copyright (c) 2025, Controlz Customizations and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [
        {"label": "Work Oder", "fieldname": "workorder", "fieldtype": "Link", "options": "Work Order", "width": 300},
        {"label": "Item To Manufacture", "fieldname": "production_item", "fieldtype": "Link", "options": "Item", "width": 300},
        {"label": "Workstation", "fieldname": "workstation", "fieldtype": "Data", "width": 180},
        {"label": "Arrival Time", "fieldname": "arrival_time", "fieldtype": "Datetime", "width": 180},
        {"label": "Serial No", "fieldname": "serial_no", "fieldtype": "Float", "width": 300},
        
    ]
	data = get_data(filters)
	return columns, data

def get_data(filters):
	final_data = frappe.db.sql("""
		select 
			wo.name as workorder,
			wo.production_item as production_item,
			wim.workstation as workstation,
			wim.arrival_time as arrival_time,
			wim.serial_no as serial_no
		from 
			`tabWork Order` wo,
			`tabWorkstation Item Movement` wim
						
		where 
			wo.docstatus = 1
		and wo.creation >= %(from_date)s
		and wo.creation <= %(to_date)s
		group by wo.name,wim.workstation
		order by wo.creation desc
	""", {
		"from_date": filters.get("from_date"),
		"to_date": filters.get("to_date")
	}, as_dict=True)

	return final_data
