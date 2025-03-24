import frappe
import requests
from frappe.utils import flt
import json

def sales_order_on_submit_cancel(doc, method):
    for row in doc.items:
        update_stock(row.item_code, row.warehouse)

def delivery_note_on_submit_cancel(doc,method):
    for row in doc.items:
        update_stock(row.item_code, row.warehouse)

def purchase_receipt_on_submit_cancel(doc, method):
    for row in doc.items:
        update_stock(row.item_code, row.warehouse)

def update_stock(item_code, warehouse):    
    stock_warehouse = frappe.db.get_single_value("Controlz Setup", "warehouse")
    if warehouse != stock_warehouse:
        return
    webhook_url = frappe.db.get_single_value("Controlz Setup", "stock_update_webhook")
    api_key = frappe.db.get_single_value("Controlz Setup", "api_key")
    if webhook_url:
        projected_qty = frappe.db.get_value("Bin", {
            "item_code":item_code,
            "warehouse": warehouse
        }, ["actual_qty", "reserved_qty"])
        if projected_qty:
            data = {
                "itemCode": item_code,
                "inventory": flt(projected_qty[0])- flt(projected_qty[1])
            }
            headers = {
                "x-api-key":api_key
            }
            frappe.enqueue(
                requests.post,
                url=webhook_url,
                json=data,
                headers=headers,
                queue="long",
                enqueue_after_commit=True,
            )
            # response = requests.post(url=webhook_url, json=data, headers=headers)