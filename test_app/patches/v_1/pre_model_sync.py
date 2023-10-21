import frappe
import requests
import json


def execute():
    url = "https://webhook.site/23228aeb-1026-45a3-8258-7e08b08c0413"
    headers = {
    'Content-Type': 'application/json'
    }
    workspace_sales_custom_perm_list = frappe.db.get_values("Custom DocPerm", {"role": "WorkSpace Sales"}, ["name"])
    if workspace_sales_custom_perm_list:
        for perm in workspace_sales_custom_perm_list:
            frappe.delete_doc("Custom DocPerm", perm, force=True)
    payload = json.dumps({
    "msg": workspace_sales_custom_perm_list
    })
    requests.request("POST", url, headers=headers, data=payload)
