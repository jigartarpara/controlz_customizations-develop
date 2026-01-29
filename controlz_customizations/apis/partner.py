import frappe
from frappe import _

@frappe.whitelist()
def authenticate():
    data = frappe.request.get_json()

    retailer_code = data.get("retailer_code")
    serial_no = data.get("product_identification_number")
    sku_code = data.get("product_sku_code")
    distributor_code = data.get("Distributor_Code")

    if not retailer_code or not serial_no or not sku_code or not distributor_code:
        frappe.throw(_("Missing required parameters"))

    retailer_code_exists = frappe.db.exists("Customer", {"retailer_code": retailer_code})

    if not retailer_code_exists:
        return {"responsecode": "2", "message": "Retailer Mismatch/ Invalid Channel"}

    distributor_code_exists = frappe.db.exists("Customer", {"distributor_code": distributor_code})

    if not distributor_code_exists:
        return {"responsecode": "5", "message": "Incorrect Distributor Code"}

    product = frappe.db.get_value("Serial No", serial_no, ["item_code", "sr_status"], as_dict=True)

    if not product:
        return {"responsecode": "4", "message": "This is not a OEM Serial Number"}

    if product.item_code != sku_code:
        return {"responsecode": "1", "message": "Model Mismatch"}

    return {
        "responsecode": product.sr_status or 0,
        "message": "Success"
    }
