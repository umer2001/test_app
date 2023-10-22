
import os
import json
from enum import Enum

import frappe


def file_exists(path):
	return os.path.isfile(path)

def remove_data():
	file_path = f"../apps/test_app/test_app/data/{doctype.value}.json"
	if file_exists(file_path):
		with open(f"../apps/test_app/data/{doctype.value}.json", "r") as json_file:
			doctype_data = json.load(json_file)
			for doctype_name in doctype_data:
				for name in doctype_data[doctype_name]:
					frappe.delete_doc(doctype_name, name, True)

def before_migrate():
	remove_data()