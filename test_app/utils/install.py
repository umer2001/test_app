
import os
import json
from enum import Enum

import frappe


def file_exists(path):
	return os.path.isfile(path)

class DocType(Enum):
	ROLES = "roles"
	ROLE_PROFILES = "role_profile"
	CUSTOM_DOC_PERM = "custom_docperm"

def add_data(doctype: DocType):
	file_path = f"../apps/test_app/data/{doctype.value}.json"
	if file_exists(file_path):
		with open(file_path, "r") as json_file:
			doctype_data = json.load(json_file)
			for name in doctype_data:
				if type(doctype_data[name]) == list:
					for doc in doctype_data[name]:
						frappe.get_doc(doc).insert(ignore_if_duplicate=True)
				else:
					frappe.get_doc(doctype_data[name]).insert(ignore_if_duplicate=True)

def remove_data(doctype: DocType):
	with open(f"../apps/test_app/data/{doctype.value}.json", "r") as json_file:
		doctype_data = json.load(json_file)
		for name in doctype_data:
			frappe.delete_doc(doctype_data[name]["doctype"], doctype_data[name]["name"], True)
		

def after_install():
	add_data(DocType.ROLES)
	add_data(DocType.CUSTOM_DOC_PERM)
	add_data(DocType.ROLE_PROFILES)