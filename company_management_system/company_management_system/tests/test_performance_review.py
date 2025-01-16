import frappe
from frappe.tests.utils import FrappeTestCase
from datetime import datetime, timedelta

class TestPerformanceReview(FrappeTestCase):
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
            "hired_on": "2030-01-01"
        }).insert()

    def tearDown(self):
        """
        Clean up test data after each test case.
        """
        # Delete the test performance review and related documents
        frappe.db.delete("Performance Review", {"employee_name": self.employee.name})
        self.employee.delete()
        self.department.delete()
        self.company.delete()

    def test_create_performance_review(self):
        """
        Test creating a new performance review.
        """
        # Create a new performance review
        performance_review = frappe.get_doc({
            "doctype": "Performance Review",
            "employee_name": self.employee.name
        }).insert()

        # Check if the performance review was created successfully
        self.assertEqual(performance_review.employee_name, self.employee.name)
        self.assertEqual(performance_review.status, "Pending Review")

    def test_prevent_update_employee_name(self):
        """
        Test that the employee_name field cannot be updated after the document is submitted.
        """
        # Create a new performance review
        performance_review = frappe.get_doc({
            "doctype": "Performance Review",
            "employee_name": self.employee.name,
            "review_date": "2030-01-01",
            "status": "Pending Review"
        }).insert()

        # Submit the document
        performance_review.submit()

        # Try to update the employee_name field
        with self.assertRaises(frappe.ValidationError):
            performance_review.employee_name = "Jane Doe"
            performance_review.save()

    def test_prevent_update_review_date(self):
        """
        Test that the review_date field cannot be updated unless the document is in the 'Review Scheduled' or 'Pending Review' states.
        """
        # Create a new performance review
        performance_review = frappe.get_doc({
            "doctype": "Performance Review",
            "employee_name": self.employee.name,
            "review_date": "2030-01-01",
            "status": "Pending Review"
        }).insert()

        # Transition to "Review Scheduled"
        performance_review.status = "Review Scheduled"
        performance_review.save()

        # Try to update the review_date field
        performance_review.review_date = "2030-01-02"
        performance_review.save()
        self.assertEqual(performance_review.review_date, "2030-01-02")

        # Transition to "Feedback Provided"
        performance_review.status = "Feedback Provided"
        performance_review.save()

        # Try to update the review_date field
        with self.assertRaises(frappe.ValidationError):
            performance_review.review_date = "2030-01-03"
            performance_review.save()


    def test_workflow_transitions(self):
        """
        Test transitioning through workflow states.
        """
        # Create a new performance review
        performance_review = frappe.get_doc({
            "doctype": "Performance Review",
            "employee_name": self.employee.name,
            "review_date": "2030-08-20",
            "status": "Pending Review"
        }).insert()

        # Transition to "Review Scheduled"
        performance_review.status = "Review Scheduled"
        performance_review.save()
        self.assertEqual(performance_review.status, "Review Scheduled")

        # Transition to "Feedback Provided"
        performance_review.status = "Feedback Provided"
        performance_review.save()
        self.assertEqual(performance_review.status, "Feedback Provided")

        # Transition to "Under Approval"
        performance_review.status = "Under Approval"
        performance_review.save()
        self.assertEqual(performance_review.status, "Under Approval")

        # Transition to "Review Approved"
        performance_review.status = "Review Approved"
        performance_review.save()
        self.assertEqual(performance_review.status, "Review Approved")

    def test_prevent_update_feedback(self):
        """
        Test that the feedback field cannot be updated after the document is in the 'Review Approved' state.
        """
        # Create a new performance review
        performance_review = frappe.get_doc({
            "doctype": "Performance Review",
            "employee_name": self.employee.name,
            "review_date": "2030-01-01",
            "status": "Pending Review",
            "feedback": "Initial feedback"
        }).insert()

        # Transition to "Review Approved"
        performance_review.status = "Review Approved"
        performance_review.save()

        # Try to update the feedback field
        with self.assertRaises(frappe.ValidationError):
            performance_review.feedback = "Updated feedback"
            performance_review.save()

    def test_is_review_date_valid(self):
        """
        Test that the review_date field must be in the future.
        """
        # Create a new performance review with a past review date
        with self.assertRaises(frappe.ValidationError):
            performance_review = frappe.get_doc({
                "doctype": "Performance Review",
                "employee_name": self.employee.name,
                "review_date": "2020-01-01",
                "status": "Pending Review"
            }).insert()

        # Create a new performance review with a future review date
        future_date = (datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d")
        performance_review = frappe.get_doc({
            "doctype": "Performance Review",
            "employee_name": self.employee.name,
            "review_date": future_date,
            "status": "Pending Review"
        }).insert()

        # Check if the performance review was created successfully
        self.assertEqual(performance_review.review_date, future_date)
