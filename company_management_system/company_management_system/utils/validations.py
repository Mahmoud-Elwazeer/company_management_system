import frappe
from .errorHandler import global_error_handler

@global_error_handler
def validate_department_belongs_to_company(department, company):
    """
    Validate that the selected department belongs to the selected company.

    Args:
        department (str): The name of the department.
        company (str): The name of the company.

    Raises:
        frappe.ValidationError: If the department does not belong to the company.
    """
    if department and company:
        # Fetch the department document
        department_doc = frappe.get_doc('Department', department)
        
        # Check if the department belongs to the selected company
        if department_doc.company != company:
            frappe.log_error(
                title="Department Validation Failed",
                message=f"The department '{department}' does not belong to the company '{company}'."
            )
            frappe.throw(
                f"The department '{department}' does not belong to the company '{company}'. "
                "Please add a valid department for the selected company."
            )


@global_error_handler
def check_auth(doc, allowed_roles=None, allowed_users=None, value_return=None):
    """
    Check if the user is authorized to access the document based on the provided rules.

    Args:
        doc: The document being accessed.
        allowed_roles (list): List of roles that have full access.
        allowed_users (list): List of users who are allowed to access the document.
        value_return: Value to return if the user is authorized.

    Raises:
        frappe.ValidationError: If the user is not authorized.
    """
    # Allow access if the user has one of the allowed roles
    if allowed_roles and any(role in frappe.get_roles() for role in allowed_roles):
        return value_return

    # Allow access if the user is in the list of allowed users
    if allowed_users and frappe.session.user in allowed_users:
        return value_return
    

    # Log the unauthorized access attempt
    frappe.log_error(
        title="Authorization Failed",
        message=f"User {frappe.session.user} attempted to access {doc.doctype} {doc.name} without permission."
    )

    # Raise a validation error
    frappe.throw("You do not have permission to access this document.")