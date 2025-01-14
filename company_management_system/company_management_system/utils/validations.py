import frappe

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
                "Please select a valid department for the selected company."
            )