# Copyright (c) 2025, Mahmoud Elwazeer and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from company_management_system.company_management_system.utils.errorHandler import global_error_handler

class PerformanceReview(Document):
	def validate(self):
		"""
        Validate the document before saving.
        """
		self.prevent_update_employee_name()
		self.prevent_update_review_date()
		self.is_review_date_valid()
		self.prevent_update_feedback()

	@global_error_handler
	def prevent_update_employee_name(self):
		"""
        Prevent updates to the employee_name field if the document is not in the 'Draft' state.
        """
		if not self.is_new() and self.has_value_changed("employee_name"):
			frappe.throw("You cannot update the Employee Name after the document is submitted.")

	@global_error_handler
	def prevent_update_review_date(self):
		"""
		Prevent updates to the review_date field unless the document is in the 'Review Scheduled' or 'Pending Review' states.
		"""
		if not self.is_new() and self.has_value_changed("review_date"):
			if self.workflow_state not in ["Review Scheduled", "Pending Review"] \
				or self.status not in ["Review Scheduled", "Pending Review"]:
				frappe.throw("You cannot update the Review Date unless the document is in 'Review Scheduled' or 'Pending Review' state.")

	@global_error_handler
	def prevent_update_feedback(self):
		"""
        Prevent updates to the feedback field after Review Approved
        """
		if self.has_value_changed("feedback") and (self.workflow_state == "Review Approved" \
									or self.status == "Review Approved"):
			frappe.throw("Prevent updates to the feedback field after Review Approved")

	@global_error_handler
	def is_review_date_valid(self):
		"""
		Custom method to check if review_date is valid for workflow transition.
		"""
		if not self.review_date:
			return False
		
		review_date_time = datetime.strptime(str(self.review_date), '%Y-%m-%d')
		today = datetime.now()

		if review_date_time < today:
			frappe.throw("Review Date must be in the future.")

