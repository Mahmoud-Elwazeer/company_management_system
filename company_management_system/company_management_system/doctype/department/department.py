# Copyright (c) 2025, Mahmoud Elwazeer and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from company_management_system.company_management_system.utils.errorHandler import global_error_handler

class Department(Document):
	@global_error_handler
	def after_insert(self):
		"""
		This method is called after the document is inserted into the database.
		"""
		self.update_company_number_of_departments()

	@global_error_handler
	def after_delete(self):
		"""
		This method is called when the document is deleted.
		"""
		self.update_company_number_of_departments()

	@global_error_handler
	def update_company_number_of_departments(self):
		"""
		Update the number of departments for the company linked only if it has changed.
		"""
		if self.company:
			comp = frappe.get_doc('Company', self.company)
			departments = frappe.get_all('Department', filters={'company': self.company})
			print(departments, len(departments))
			if comp.number_of_departments != len(departments):
				comp.number_of_departments = len(departments)
				comp.save()
