# Security and Permissions

## Role-Based Access Control (RBAC)
- **Admin**: Full access to all features, including user management, company management, and performance reviews.
- **Manager**: Can manage employees, projects, and performance reviews within their department.
- **Employee**: Limited access to their own profile and assigned projects.

## Authentication
- **Session-Based Authentication**: Users log in with their email and password, and a session cookie is used for subsequent requests.

## Data Protection
###  **Validation**:
* All inputs are validated to prevent SQL injection and other attacks.
*  **Additional Validation Steps**

| **Model** | **Validation** | **Purpose** |
| --- | --- | --- |
| **Employee** | `validate_department_belongs_to_company` | Ensures department belongs to the same company as the employee. |
| **Employee** | `calculate_days_employed` | Calculates days employed based on `hired_on` date. |
| **PerformanceReview** | `prevent_update_employee_name` | Prevents updating `employee_name` after submission. |
| **PerformanceReview** | `prevent_update_review_date` | Prevents updating `review_date` unless in specific states. |
| **PerformanceReview** | `is_review_date_valid` | Ensures `review_date` is in the future. |
| **PerformanceReview** | `prevent_update_feedback` | Prevents updating `feedback` after review is approved. |
| **Project** | `validate_assigned_employees` | Ensures assigned employees belong to the same company and department. |
| **Department** | `update_company_number_of_departments` | Updates the number of departments in the `Company` document. |


### **Permissions**: 
* Custom DocPerms ensure that only authorized users can access or modify data depend on their roles.