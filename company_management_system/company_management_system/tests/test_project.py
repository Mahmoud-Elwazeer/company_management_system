# Copyright (c) 2025, Mahmoud Elwazeer and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase

class TestProject(FrappeTestCase):
	def setUp(self):
		"""
		Set up test data before each test case.
		"""
		# Create a test company
		self.company = frappe.get_doc({
			"doctype": "Company",
			"company_name": "Test Company"
		}).insert()

		# Create a test department
		self.department = frappe.get_doc({
			"doctype": "Department",
			"department_name": "Test Department",
			"company": self.company.name
		}).insert()

		# Create a test employee
		self.employee = frappe.get_doc({
			"doctype": "Employee",
			"employee_name": "John Doe",
			"company": self.company.name,
			"department": self.department.name,
			"email_address": "john.doe@example.com",
			"mobile_number": "1234567890",
			"designation": "Software Engineer",
			"hired_on": "2025-01-01"
		}).insert()

	def tearDown(self):
		"""
		Clean up test data after each test case.
		"""
		frappe.db.delete("Project", {"company": self.company.name})
		self.employee.delete()
		self.department.delete()
		self.company.delete()

	def test_create_project(self):
		"""
		Test creating a new project.
		"""
		# Create a new project
		project = frappe.get_doc({
			"doctype": "Project",
			"project_name": "Test Project",
			"company": self.company.name,
			"department": self.department.name,
			"start_date": "2025-01-01",
			"assigned_employees": [
				{
					"employee_name": self.employee.name
				}
			]
		}).insert()

		# Check if the project was created successfully
		self.assertEqual(project.project_name, "Test Project")
		self.assertEqual(project.company, self.company.name)
		self.assertEqual(project.department, self.department.name)
		self.assertEqual(project.start_date, "2025-01-01")
		self.assertEqual(len(project.assigned_employees), 1)
		self.assertEqual(project.assigned_employees[0].employee_name, self.employee.name)

		project.delete()


	def test_required_fields(self):
		"""
		Test that required fields are enforced.
		"""
		# Try to create a project without required fields
		with self.assertRaises(frappe.ValidationError):
			project = frappe.get_doc({
				"doctype": "Project"
			}).insert()

		# Try to create a project without a company
		with self.assertRaises(frappe.ValidationError):
			project = frappe.get_doc({
				"doctype": "Project",
				"project_name": "Test Project",
				"department": self.department.name,
				"start_date": "2025-01-01",
				"assigned_employees": [
					{
						"employee_name": self.employee.name
					}
				]
			}).insert()

		# Try to create a project without a department
		with self.assertRaises(frappe.ValidationError):
			project = frappe.get_doc({
				"doctype": "Project",
				"project_name": "Test Project",
				"company": self.company.name,
				"start_date": "2025-01-01",
				"assigned_employees": [
					{
						"employee_name": self.employee.name
					}
				]
			}).insert()

		# Try to create a project without a start date
		with self.assertRaises(frappe.ValidationError):
			project = frappe.get_doc({
				"doctype": "Project",
				"project_name": "Test Project",
				"company": self.company.name,
				"department": self.department.name,
				"assigned_employees": [
					{
						"employee_name": self.employee.name
					}
				]
			}).insert()

		# Try to create a project without assigned employees
		with self.assertRaises(frappe.ValidationError):
			project = frappe.get_doc({
				"doctype": "Project",
				"project_name": "Test Project",
				"company": self.company.name,
				"department": self.department.name,
				"start_date": "2025-01-01"
			}).insert()


	def test_validate_department_belongs_to_company(self):
		"""
		Test that the department belongs to the correct company.
		"""
		# Create a new department that does not belong to the test company
		other_company = frappe.get_doc({
			"doctype": "Company",
			"company_name": "Other Company"
		}).insert()

		other_department = frappe.get_doc({
			"doctype": "Department",
			"department_name": "Other Department",
			"company": other_company.name
		}).insert()

		# Try to create a project with a department that does not belong to the company
		with self.assertRaises(frappe.ValidationError):
			project = frappe.get_doc({
				"doctype": "Project",
				"project_name": "Test Project",
				"company": self.company.name,
				"department": other_department.name,
				"start_date": "2025-01-01",
				"assigned_employees": [
					{
						"employee_name": self.employee.name
					}
				]
			}).insert()

		# Clean up
		other_department.delete()
		other_company.delete()

	def test_validate_assigned_employees(self):
		"""
		Test that assigned employees belong to the correct company and department.
		"""
		# Create a new employee that does not belong to the test department
		other_department = frappe.get_doc({
			"doctype": "Department",
			"department_name": "Other Department",
			"company": self.company.name
		}).insert()

		other_employee = frappe.get_doc({
			"doctype": "Employee",
			"employee_name": "Jane Doe",
			"company": self.company.name,
			"department": other_department.name,
			"email_address": "jane.doe@example.com",
			"mobile_number": "0987654321",
			"designation": "Product Manager",
			"hired_on": "2025-01-01"
		}).insert()

		# Try to create a project with an employee that does not belong to the department
		with self.assertRaises(frappe.ValidationError):
			project = frappe.get_doc({
				"doctype": "Project",
				"project_name": "Test Project",
				"company": self.company.name,
				"department": self.department.name,
				"start_date": "2025-01-01",
				"assigned_employees": [
					{
						"employee_name": other_employee.name
					}
				]
			}).insert()

		# Clean up
		other_employee.delete()
		other_department.delete()


	def test_update_assigned_employees(self):
		"""
		Test that the `assigned_employees` field is updated correctly.
		"""
		# Create a new project
		project = frappe.get_doc({
			"doctype": "Project",
			"project_name": "Test Project",
			"company": self.company.name,
			"department": self.department.name,
			"start_date": "2025-01-01",
			"assigned_employees": [
				{
					"employee_name": self.employee.name
				}
			]
		}).insert()

		# Check if the assigned employees were added correctly
		self.assertEqual(len(project.assigned_employees), 1)
		self.assertEqual(project.assigned_employees[0].employee_name, self.employee.name)

		# Add another employee to the project
		employee2 = frappe.get_doc({
			"doctype": "Employee",
			"employee_name": "Jane Doe",
			"company": self.company.name,
			"department": self.department.name,
			"email_address": "test2@gmail.com",
			"mobile_number": "0987654321",
			"designation": "Product Manager",
			"hired_on": "2025-01-01"
		}).insert()

		project.append("assigned_employees", {
			"employee_name": employee2.name
		})
		project.save()

		# Check if the assigned employees were updated correctly
		self.assertEqual(len(project.assigned_employees), 2)
		self.assertEqual(project.assigned_employees[1].employee_name, employee2.name)

		# Clean up
		project.delete()
		employee2.delete()


	def test_update_company_number_of_projects(self):
		"""
		Test that the `number_of_projects` field in the company is updated correctly.
		"""
		# Create a new project
		project = frappe.get_doc({
			"doctype": "Project",
			"project_name": "Test Project",
			"company": self.company.name,
			"department": self.department.name,
			"start_date": "2025-01-01",
			"assigned_employees": [
				{
					"employee_name": self.employee.name
				}
			]
		}).insert()

		# Reload the company to check if the number of projects was updated
		self.company.reload()
		self.assertEqual(self.company.number_of_projects, 1)

		# Delete the project
		project.delete()

		# Reload the company to check if the number of projects was updated
		self.company.reload()
		self.assertEqual(self.company.number_of_projects, 0)


	def test_update_department_number_of_projects(self):
		"""
		Test that the `number_of_projects` field in the department is updated correctly.
		"""
		# Create a new project
		project = frappe.get_doc({
			"doctype": "Project",
			"project_name": "Test Project",
			"company": self.company.name,
			"department": self.department.name,
			"start_date": "2025-01-01",
			"assigned_employees": [
				{
					"employee_name": self.employee.name
				}
			]
		}).insert()

		# Reload the department to check if the number of projects was updated
		self.department.reload()
		self.assertEqual(self.department.number_of_projects, 1)

		# Delete the project
		project.delete()

		# Reload the department to check if the number of projects was updated
		self.department.reload()
		self.assertEqual(self.department.number_of_projects, 0)


	def test_check_permissions(self):
		"""
		Test that the permission checks work correctly.
		"""
		# Create a new project
		project = frappe.get_doc({
			"doctype": "Project",
			"project_name": "Test Project",
			"company": self.company.name,
			"department": self.department.name,
			"start_date": "2025-01-01",
			"assigned_employees": [
				{
					"employee_name": self.employee.name
				}
			]
		}).insert()

		# Simulate a user with no permissions
		frappe.set_user("Guest")
		with self.assertRaises(frappe.ValidationError):
			project.reload()

		# Reset the user
		frappe.set_user("Administrator")
		
		project.delete()
