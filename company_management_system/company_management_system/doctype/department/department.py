# Copyright (c) 2025, Mahmoud Elwazeer and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Department(Document):
	def validate(self):
		self.update_company_number_of_departments()

	def update_company_number_of_departments(self):
		if self.company:
			comp = frappe.get_doc('Company', self.company)
			departments = frappe.get_all('Department', filters={'company': self.company})
			if comp.number_of_departments != len(departments):
				comp.number_of_departments = len(departments)
				comp.save()
