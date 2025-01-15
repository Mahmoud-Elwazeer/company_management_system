# Copyright (c) 2025, Mahmoud Elwazeer and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from company_management_system.company_management_system.utils.validations import validate_department_belongs_to_company, check_auth
from company_management_system.company_management_system.utils.errorHandler import global_error_handler

class Project(Document):
	@global_error_handler
	def validate(self):
		"""
		Use this method to throw any validation errors and prevent the document from saving
		"""
		self.update_company_number_of_projects()
		self.update_department_number_of_projects()
		validate_department_belongs_to_company(self.department, self.company)
		self.validate_assigned_employees()

	@global_error_handler
	def validate_assigned_employees(self):
		"""
		Validate that all assigned employees belong to the same company and department as the project.
		"""
		if self.company and self.department and self.assigned_employees:
			for assigned_employee in self.assigned_employees:
				employee = frappe.get_doc('Employee', assigned_employee.employee_name)
				if employee.company != self.company:
					frappe.log_error(
						title="Company Validation Failed",
						message=f"Employee '{employee.employee_name}' does not belong to company '{self.company}'."
					)
					frappe.throw(
						f"Employee '{employee.employee_name}' does not belong to the company '{self.company}'. "
						"Please assign employees from the same company."
					)
				if employee.department != self.department:
					frappe.log_error(
						title="Department Validation Failed",
						message=f"Employee '{employee.employee_name}' does not belong to department '{self.department}'."
					)
					frappe.throw(
						f"Employee '{employee.employee_name}' does not belong to the department '{self.department}'. "
						"Please assign employees from the same department."
					)

	@global_error_handler
	def update_company_number_of_projects(self):
		"""
		Update the number of projects for the company linked to thess projects only if it has changed.
		"""
		if self.company:
			comp = frappe.get_doc('Company', self.company)
			projects = frappe.get_all('Project', filters={'company': self.company})
			if comp.number_of_projects != len(projects):
				comp.number_of_projects = len(projects)
				comp.save()


	@global_error_handler
	def update_department_number_of_projects(self):
		"""
		Update the number of projects for the department linked to thess projects only if it has changed.
		"""
		if self.department:
			dept = frappe.get_doc('Department', self.department)
			projects = frappe.get_all(
				"Project",
				filters={
					"department": self.department,
					"company": self.company  # Add company filter
					})
			if dept.number_of_projects != len(projects):
				dept.number_of_projects = len(projects)
				dept.save()

	def check_permissions(self):
		allowed_roles = ["Admin", "Manager", "Administrator", "System Manager"]
		allowed_users = []
		for emp in self.assigned_employees:
			employee = frappe.get_doc("Employee", emp.employee_name)
			allowed_users.append(employee.email_address)

		check_auth(self, allowed_roles=allowed_roles, allowed_users=allowed_users, value_return=None)

	def load_from_db(self):
		"""
		Used to call call GET /api/resource/Project/<project-name>
		"""
		super().load_from_db()
		self.check_permissions()


