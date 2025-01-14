# Copyright (c) 2025, Mahmoud Elwazeer and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from company_management_system.company_management_system.utils.validations import validate_department_belongs_to_company

class Employee(Document):
	def validate(self):
		self.calculate_days_employed()
		self.update_department_number_of_employees()
		self.update_company_number_of_employees()
		validate_department_belongs_to_company(self.department, self.company)

	def calculate_days_employed(self):
		if self.hired_on:
			hired_date = datetime.strptime(self.hired_on, '%Y-%m-%d')
			today = datetime.now()
			self.days_employed = (today - hired_date).days

	def update_department_number_of_employees(self):
		if self.department:
			dept = frappe.get_doc("Department", self.department)
			employees = frappe.get_all("Employee", filters={"department": self.department})
			if dept.number_of_employees != len(employees):
				dept.number_of_employees = len(employees)
				dept.save()

	def update_company_number_of_employees(self):
		if self.company:
			comp = frappe.get_doc("Company", self.company)
			employees = frappe.get_all("Employee", filters={'company': self.company})
			if comp.number_of_employees != len(employees):
				comp.number_of_employees = len(employees)
				comp.save()

