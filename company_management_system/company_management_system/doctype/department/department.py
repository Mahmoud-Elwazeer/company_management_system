# Copyright (c) 2025, Mahmoud Elwazeer and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from company_management_system.company_management_system.utils.errorHandler import global_error_handler

class Department(Document):
	@global_error_handler
	def validate(self):
		"""
		Use this method to throw any validation errors and prevent the document from saving
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
			if comp.number_of_departments != len(departments):
				comp.number_of_departments = len(departments)
				comp.save()
