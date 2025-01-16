# Copyright (c) 2025, Mahmoud Elwazeer and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from company_management_system.company_management_system.utils.validations import validate_department_belongs_to_company, check_auth
from company_management_system.company_management_system.utils.errorHandler import global_error_handler

class Employee(Document):
	@global_error_handler
	def validate(self):
		"""
		Use this method to throw any validation errors and prevent the document from saving
		"""
		self.calculate_days_employed()
		validate_department_belongs_to_company(self.department, self.company)

	@global_error_handler
	def after_insert(self):
		"""
		This method is called after the document is inserted into the database.
		"""
		self.update_department_number_of_employees()
		self.update_company_number_of_employees()

	@global_error_handler
	def after_delete(self):
		"""
		This method is called when the document is deleted.
		"""
		self.update_department_number_of_employees()
		self.update_company_number_of_employees()

	@global_error_handler
	def calculate_days_employed(self):
		"""
		Auto calculate days employed for employee who have hired
		"""
		if self.hired_on:
			hired_date = datetime.strptime(self.hired_on, '%Y-%m-%d')
			today = datetime.now()
			days = (today - hired_date).days
			if days > 0:
				self.days_employed = days
			else:
				self.days_employed = 0

	@global_error_handler
	def update_department_number_of_employees(self):
		"""
		Update the number of employees for each department for the company linked only if it has changed.
		"""
		if self.department:
			dept = frappe.get_doc("Department", self.department)
			employees = frappe.get_all(
				"Employee",
				filters={
					"department": self.department,
					"company": self.company  # Add company filter
					})
			if dept.number_of_employees != len(employees):
				dept.number_of_employees = len(employees)
				dept.save()

	@global_error_handler
	def update_company_number_of_employees(self):
		"""
		Update the number of employees ffor the company linked only if it has changed.
		"""
		if self.company:
			comp = frappe.get_doc("Company", self.company)
			employees = frappe.get_all("Employee", filters={'company': self.company})
			if comp.number_of_employees != len(employees):
				comp.number_of_employees = len(employees)
				comp.save()

	def check_permissions(self):
		"""
        Check permissions when loading additional data in the form view.
        """
		allowed_roles = ["Admin", "Manager", "Administrator", "System Manager"]
		allowed_users = [self.email_address]  # Allow the employee to access their own profile
		check_auth(self, allowed_roles=allowed_roles, allowed_users=allowed_users, value_return=None)

	def load_from_db(self):
		"""
		Used to load data from db
		"""
		super().load_from_db()
		self.check_permissions()

