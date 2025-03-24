from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
import frappe

def setup_custom_fields():
	custom_fields = {
		"Stock Entry": [
			dict(fieldname='production_planning_record',
				label='Production Planning Record',
				fieldtype='Link',
				options='Production Planning Record',
				insert_after='stock_entry_type',
				read_only=True
			),
		],
		"Item": [
			dict(fieldname='part_warehouse',
				label='Part Warehouse',
				fieldtype='Link',
				options='Warehouse',
				insert_after='stock_uom'
			),
		],
		"Material Request": [
			dict(fieldname='production_stock_planning',
				label='Production Stock Planning',
				fieldtype='Link',
				options='Production Stock Planning',
				insert_after='material_request_type',
				read_only=True
			),
		],
		"Material Request Item": [
			dict(fieldname='parts_for',
				label='Parts For',
				fieldtype='Link',
				options='Item',
				insert_after='item_name',
				# read_only=True
			),
		],
		"Item Group": [
			dict(fieldname='item_group_percentage',
				label='Item Group Percentage',
				fieldtype='Table',
				options='Item Group Percentage',
				insert_after='item_group_defaults',
				# read_only=True
			),
		],
	}
	try:
		create_custom_fields(custom_fields)
		frappe.db.commit()
	except:
		print("Exception while createing customfield")