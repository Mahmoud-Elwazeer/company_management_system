# Copyright (c) 2025, Mahmoud Elwazeer and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase
from datetime import datetime, timedelta


class TestEmployee(FrappeTestCase):
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

	def tearDown(self):
		"""
		Clean up test data after each test case.
		"""
		# Delete the test employee and related documents
		frappe.db.delete("Employee", {"company": self.company.name})
		self.department.delete()
		self.company.delete()

	def test_create_employee(self):
		"""
		Test creating a new employee.
		"""
		# Create a new employee
		employee = frappe.get_doc({
			"doctype": "Employee",
			"employee_name": "Mahmoud ELwazeer",
			"company": self.company.name,
			"department": self.department.name,
			"email_address": "test@gmail.com",
			"mobile_number": "1234567890",
			"designation": "Software Engineer",
			"hired_on": "2025-01-01"
		}).insert()

		# Check if the employee was created successfully
		self.assertEqual(employee.employee_name, "Mahmoud ELwazeer")
		self.assertEqual(employee.company, self.company.name)
		self.assertEqual(employee.department, self.department.name)
		self.assertEqual(employee.email_address, "test@gmail.com")
		self.assertEqual(employee.mobile_number, "1234567890")
		self.assertEqual(employee.designation, "Software Engineer")
		self.assertEqual(employee.hired_on, "2025-01-01")


	def test_required_fields(self):
		"""
		Test that required fields are enforced.
		"""
        # Try to create an employee without required fields
		with self.assertRaises(frappe.ValidationError):
			employee = frappe.get_doc({
				"doctype": "Employee",
				"employee_name": "Mahmoud ELwazeer"
			}).insert()

		# Try to create an employee without a company
		with self.assertRaises(frappe.ValidationError):
			employee = frappe.get_doc({
				"doctype": "Employee",
				"employee_name": "Mahmoud ELwazeer",
				"department": self.department.name,
				"email_address": "test@gmail.com",
				"mobile_number": "1234567890",
				"designation": "Software Engineer",
				"hired_on": "2025-01-01"
			}).insert()

		# Try to create an employee without a department
		with self.assertRaises(frappe.ValidationError):
			employee = frappe.get_doc({
				"doctype": "Employee",
				"employee_name": "Mahmoud ELwazeer",
				"company": self.company.name,
				"email_address": "test@gmail.com",
				"mobile_number": "1234567890",
				"designation": "Software Engineer",
				"hired_on": "2025-01-01"
			}).insert()

		# Try to create an employee without an email address
		with self.assertRaises(frappe.ValidationError):
			employee = frappe.get_doc({
				"doctype": "Employee",
				"employee_name": "Mahmoud ELwazeer",
				"company": self.company.name,
				"department": self.department.name,
				"mobile_number": "1234567890",
				"designation": "Software Engineer",
				"hired_on": "2025-01-01"
			}).insert()

		# Try to create an employee without a mobile number
		with self.assertRaises(frappe.ValidationError):
			employee = frappe.get_doc({
				"doctype": "Employee",
				"employee_name": "Mahmoud ELwazeer",
				"company": self.company.name,
				"department": self.department.name,
				"email_address": "test@gmail.com",
				"designation": "Software Engineer",
				"hired_on": "2025-01-01"
			}).insert()

		# Try to create an employee without a designation
		with self.assertRaises(frappe.ValidationError):
			employee = frappe.get_doc({
				"doctype": "Employee",
				"employee_name": "Mahmoud ELwazeer",
				"company": self.company.name,
				"department": self.department.name,
				"email_address": "test@gmail.com",
				"mobile_number": "1234567890",
				"hired_on": "2025-01-01"
			}).insert()

	def test_days_employed_calculation(self):
		"""
		Test that the `days_employed` field is calculated correctly.
		"""
		# Create a new employee with a hire date in the past
		hire_date = datetime.now() - timedelta(days=10)
		employee = frappe.get_doc({
			"doctype": "Employee",
			"employee_name": "Jane Doe",
			"company": self.company.name,
			"department": self.department.name,
			"email_address": "jane.doe@example.com",
			"mobile_number": "0987654321",
			"designation": "Product Manager",
			"hired_on": hire_date.strftime("%Y-%m-%d")
		}).insert()

		# Check if the `days_employed` field is calculated correctly
		expected_days_employed = (datetime.now() - hire_date).days
		self.assertEqual(employee.days_employed, expected_days_employed)


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

		# Try to create an employee with a department that does not belong to the company
		with self.assertRaises(frappe.ValidationError):
			employee = frappe.get_doc({
				"doctype": "Employee",
				"employee_name": "Mahmoud ELwazeer",
				"company": self.company.name,
				"department": other_department.name,
				"email_address": "test@gmail.com",
				"mobile_number": "1234567890",
				"designation": "Software Engineer",
				"hired_on": "2025-01-01"
			}).insert()

		# Clean up
		other_department.delete()
		other_company.delete()


	def test_update_department_number_of_employees(self):
			"""
			Test that the `number_of_employees` field in the department is updated correctly.
			"""
			# Create a new employee
			employee = frappe.get_doc({
				"doctype": "Employee",
				"employee_name": "Mahmoud ELwazeer",
				"company": self.company.name,
				"department": self.department.name,
				"email_address": "test@gmail.com",
				"mobile_number": "1234567890",
				"designation": "Software Engineer",
				"hired_on": "2025-01-01"
			}).insert()

			# Reload the department to check if the number of employees was updated
			self.department.reload()
			self.assertEqual(self.department.number_of_employees, 1)

			# Delete the employee
			employee.delete()

			# Reload the department to check if the number of employees was updated
			self.department.reload()
			self.assertEqual(self.department.number_of_employees, 0)


	def test_update_company_number_of_employees(self):
		"""
		Test that the `number_of_employees` field in the company is updated correctly.
		"""
		# Create a new employee
		employee = frappe.get_doc({
			"doctype": "Employee",
			"employee_name": "Mahmoud ELwazeer",
			"company": self.company.name,
			"department": self.department.name,
			"email_address": "test@gmail.com",
			"mobile_number": "1234567890",
			"designation": "Software Engineer",
			"hired_on": "2025-01-01"
		}).insert()

		# Reload the company to check if the number of employees was updated
		self.company.reload()
		self.assertEqual(self.company.number_of_employees, 1)

		# Delete the employee
		employee.delete()

		# Reload the company to check if the number of employees was updated
		self.company.reload()
		self.assertEqual(self.company.number_of_employees, 0)

	def test_check_permissions(self):
		"""
		Test that the permission checks work correctly.
		"""
		# Create a new employee
		employee = frappe.get_doc({
			"doctype": "Employee",
			"employee_name": "Mahmoud ELwazeer",
			"company": self.company.name,
			"department": self.department.name,
			"email_address": "test@gmail.com",
			"mobile_number": "1234567890",
			"designation": "Software Engineer",
			"hired_on": "2025-01-01"
		}).insert()

		# Simulate a user with no permissions
		frappe.set_user("Guest")
		with self.assertRaises(frappe.ValidationError):
			employee.reload()

		# Reset the user
		frappe.set_user("Administrator")