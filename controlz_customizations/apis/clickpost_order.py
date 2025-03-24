import frappe
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def make_clickpost_doc_from_sales_order_to_customer(source_name,target_doc=None):
    def set_missing_values(source, target):
        so = frappe.get_doc("Sales Order", source_name)
        target.sales_order = so.name
        target.pickup_type = "To Customer"
        
        address = frappe.get_doc("Address", so.shipping_address_name)
        customer = frappe.get_doc("Customer", so.customer)
        address_att = [address.address_line1, address.address_line2, address.city, address.state, address.pincode,]
        target.pickup_address = " ".join([data  for data in address_att if data])
        target.pickup_state = address.state
        target.pickup_city = address.city
        target.pickup_pincode = address.pincode
        target.pickup_email = customer.cu_email
        target.pickup_phone = customer.cu_mobile_number

    doclist = get_mapped_doc("Sales Order", source_name,
    {
        "Sales Order": {
            "doctype": "Clickpost Order",
            "field_map": {
            }
        },

    }, target_doc,set_missing_values)

    return doclist