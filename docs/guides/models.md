# Data Models

## User
- **Username**: Unique identifier for the user.
- **Email Address**: Used for login.
- **Role**: Defines the user's role (Admin, Manager, Employee).

## Company
- **Company Name**: Name of the company.
- **Number of Departments**: Auto-calculated field.
- **Number of Employees**: Auto-calculated field.
- **Number of Projects**: Auto-calculated field.

## Department
- **Company**: The company the department belongs to.
- **Department Name**: Name of the department.
- **Number of Employees**: Auto-calculated field.
- **Number of Projects**: Auto-calculated field.

## Employee
- **Company**: The company the employee belongs to.
- **Department**: The department the employee belongs to.
- **Employee Name**: Name of the employee.
- **Email Address**: Contact email for the employee.
- **Mobile Number**: Contact number for the employee.
- **Address**: Address of the employee (optional)..
- **Designation**: Job title of the employee.
- **Hired On**: Date the employee was hired (optional).
- **Days Employed**: Auto-calculated field based on the hire date.

## Project
- **Company**: The company the project belongs to.
- **Department**: The department the project belongs to.
- **Project Name**: Name of the project.
- **Description**: Description of the project (optional).
- **Start Date**: Start date of the project.
- **End Date**: End date of the project (optional)..
- **Assigned Employees**: List of employees assigned to the project.

## Performance Review
- **Employee Name**: The employee being reviewed.
- **Review Date**: Date of the review.
- **Feedback**: Feedback provided during the review.
- **Status**: Current status of the review (e.g., Pending Review, Review Scheduled, etc.).