import frappe

def global_error_handler(func):
    """
    A decorator to handle errors globally for any function.
    Logs the error and raises a user-friendly validation error.
    """
    def wrapper(*args, **kwargs):
        try:
            # Call the original function
            return func(*args, **kwargs)
        except Exception as e:
            # Log the error
            frappe.log_error(
                title=f" Exception Error",
                message=str(e)
            )
            # Raise a user-friendly validation error
            frappe.throw(f"An error occurred: {str(e)}")
    return wrapper
