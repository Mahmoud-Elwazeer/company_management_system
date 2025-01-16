# Copyright (c) 2025, Mahmoud Elwazeer and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase

class TestDepartment(FrappeTestCase):
	def setUp(self):
		"""
		Set up test data before each test case.
		"""
		# Create a test company
		self.company = frappe.get_doc({
			"doctype": "Company",
			"company_name": "Test Company"
		}).insert()

	def tearDown(self):
		"""
		Clean up test data after each test case.
		"""
		# Delete the test company and all related departments
		frappe.db.delete("Department", {"company": self.company.name})
		self.company.delete()

	def test_create_department(self):
		"""
		Test creating a new department and updating the company's number of departments.
		"""
		# Create a new department
		department = frappe.get_doc({
			"doctype": "Department",
			"department_name": "Test Department",
			"company": self.company.name
		}).insert()

		# Check if the department was created successfully
		self.assertEqual(department.name, f"{self.company.name}-Test Department")
		self.assertEqual(department.company, self.company.name)

		# Reload the company to check if the number of departments was updated
		self.company.reload()
		self.assertEqual(self.company.number_of_departments, 1)

	def test_update_company_number_of_departments(self):
		"""
		Test updating the number of departments when a new department is added.
		"""
		# Create a new department
		department = frappe.get_doc({
			"doctype": "Department",
			"department_name": "Test Department",
			"company": self.company.name
		}).insert()

		# Reload the company to check if the number of departments was updated
		self.company.reload()
		self.assertEqual(self.company.number_of_departments, 1)

		# Create another department
		department2 = frappe.get_doc({
			"doctype": "Department",
			"department_name": "Test Department 2",
			"company": self.company.name
		}).insert()

		# Reload the company to check if the number of departments was updated
		self.company.reload()
		self.assertEqual(self.company.number_of_departments, 2)

	def test_delete_department(self):
		"""
		Test deleting a department and updating the company's number of departments.
		"""
		# Create a new department
		department = frappe.get_doc({
			"doctype": "Department",
			"department_name": "Test Department",
			"company": self.company.name
		}).insert()

		# Reload the company to check if the number of departments was updated
		self.company.reload()
		self.assertEqual(self.company.number_of_departments, 1)

		# Delete the department
		department.delete()

		# Reload the company to check if the number of departments was updated
		self.company.reload()
		self.assertEqual(self.company.number_of_departments, 0)

	def test_unique_department_name(self):
		"""
		Test that department names must be unique.
		"""
		# Create a new department
		department = frappe.get_doc({
			"doctype": "Department",
			"department_name": "Test Department",
			"company": self.company.name
		}).insert()

		# Try to create another department with the same name
		with self.assertRaises(frappe.exceptions.DuplicateEntryError):
			department2 = frappe.get_doc({
				"doctype": "Department",
				"department_name": "Test Department",
				"company": self.company.name
			}).insert()

	def test_required_fields(self):
		"""
		Test that required fields are enforced.
		"""
		# Try to create a department without a company
		with self.assertRaises(frappe.ValidationError):
			department = frappe.get_doc({
				"doctype": "Department",
				"department_name": "Test Department"
			}).insert()

		# Try to create a department without a department name
		with self.assertRaises(frappe.ValidationError):
			department = frappe.get_doc({
				"doctype": "Department",
				"company": self.company.name
			}).insert()