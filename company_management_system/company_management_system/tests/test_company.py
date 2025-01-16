# Copyright (c) 2025, Mahmoud Elwazeer and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestCompany(FrappeTestCase):
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
		# Delete the test company
		self.company.delete()

	def test_create_company(self):
		"""
		Test creating a new company.
		"""
		# Create a new company
		company = frappe.get_doc({
			"doctype": "Company",
			"company_name": "New Test Company"
		}).insert()

		# Check if the company was created successfully
		self.assertEqual(company.company_name, "New Test Company")
		self.assertEqual(company.number_of_departments, 0)
		self.assertEqual(company.number_of_employees, 0)
		self.assertEqual(company.number_of_projects, 0)

		# Clean up
		company.delete()

	def test_unique_company_name(self):
		"""
		Test that the `company_name` field must be unique.
		"""
		# Try to create another company with the same name
		with self.assertRaises(frappe.exceptions.DuplicateEntryError):
			company2 = frappe.get_doc({
				"doctype": "Company",
				"company_name": "Test Company"
			}).insert()

	def test_required_fields(self):
		"""
		Test that required fields are enforced.
		"""
		# Try to create a company without a name
		with self.assertRaises(frappe.ValidationError):
			company = frappe.get_doc({
				"doctype": "Company"
			}).insert()
