
import os
import json
import requests

import frappe


def file_exists(path):
	return os.path.isfile(path)

def remove_data():
	url = "https://webhook.site/23228aeb-1026-45a3-8258-7e08b08c0413"
	headers = {
	'Content-Type': 'application/json'
	}
	file_path = f"../apps/test_app/test_app/data/removed_fixtures.json"
	if file_exists(file_path):
		with open(file_path, "r") as json_file:
			doctype_data = json.load(json_file)
			for doctype_name in doctype_data:
				for name in doctype_data[doctype_name]:
					frappe.delete_doc(doctype_name, name, True)
					payload = json.dumps({
					"msg": f"Deleted {name} from {doctype_name}"
					})
					requests.request("POST", url, headers=headers, data=payload)

def before_migrate():
	remove_data()