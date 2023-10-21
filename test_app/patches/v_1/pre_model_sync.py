import frappe
import requests
import json


def execute():
    url = "https://webhook.site/23228aeb-1026-45a3-8258-7e08b08c0413"
    payload = json.dumps({
    "msg": "Hello"
    })
    headers = {
    'Content-Type': 'application/json'
    }
    requests.request("POST", url, headers=headers, data=payload)
    workspace_sales_custom_perm_list = frappe.db.get_value("Custom DocPerm", {"role": "WorkSpace Sales"}, "name")
    if workspace_sales_custom_perm_list:
        for perm in workspace_sales_custom_perm_list:
            frappe.delete_doc("Custom DocPerm", perm, force=True)
