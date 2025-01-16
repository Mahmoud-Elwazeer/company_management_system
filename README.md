# Company Management System

<div align="center">
  <h3 align="center">Company Management System</h3>
  <p align="center">
    A system for managing companies, departments, employees, and projects with a workflow for employee performance reviews.
    <br />
    <a href="https://github.com/loaywaleed/company-management-systems/issues">Report Bug</a>
    ·
    <a href="https://github.com/loaywaleed/company-management-systems/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#features">Features</a></li>
    <li><a href="#documentation">Documentation</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#running-tests">Tests</a></li>
    <li><a href="#approach">Approach</a></li>
    <li><a href="#project-requirements-checklist">Checklist</a></li>
  </ol>
</details>

---

## About The Project

The **Company Management System** is a backend application designed to manage companies, departments, employees, and projects. It includes a workflow for handling employee performance reviews and implements role-based access control to ensure secure data handling.

### Built With

- **Python**
- **Frappe Framework**

---

## Features

- **User Management**: Create and read users with different roles (Admin, Manager, Employee).
- **Company Management**: Manage company records, including departments, employees, and projects.
- **Department Management**: Manage departments within companies.
- **Employee Management**: Manage employee records, including their roles, departments, and projects.
- **Project Management**: Manage projects and assign employees to them.
- **Performance Review Workflow**: A structured workflow for managing employee performance reviews.
- **Role-Based Access Control**: Secure access to features based on user roles (Admin, Manager, Employee).
- **RESTful API**: A well-documented API for interacting with the system.

---

## Documentation

For detailed documentation, refer to the following:

- **[API Documentation](docs/api/README.md)**: Detailed documentation for all API endpoints.
- **[Guides](docs/guides/README.md)**: Explanations of data models, workflows, security, testing, and logging.
- [**Demo**](docs/imgs/README.md)
---

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites
- Python 3.x
- Frappe Framework
- MySQL or MariaDB

### Installation

1. **Set up Frappe Bench** (if you don't have one):
   ```bash
   bench init frappe-bench --frappe-branch version-15
   ```

2. **Get the App**:
   
   ```
   bench get-app company_management_system https://github.com/Mahmoud-Elwazeer/company_management_system.git
   ```
   
3. **Create a New Site** (if you don't have one):
   
   ```
   bench new-site <site_name>
   ```
   
4. **Run Migrate Command**:
   
   ```
   bench migrate
   ```
   
5. **Install the App**:
   
   ```
   bench --site <site_name> install-app company_management_system
   ```
   
6. **Set the Site as Default**:
   
   ```
   bench use <site_name>
   ```
   
7. **( OR ) Add to hosts**

   ```
   bench --site <site_name> add-to-hosts
   ```

8. **Export Fixtures** (for workflows and scheduled tasks):
   
   ```
   bench export-fixtures
   ```
   
9. **Run the App**:
   ```
   bench start
   ```

### Running Tests
```
bench --site <site_name> set-config allow_tests true
bench --site <site_name> run-tests --app company_management_system
```

## Approach

**Why did I choose Frappe?**
* I have used ERPNext before so I am familiar with Frappe. When I read that it's an advantage, I decided to go for it to better maximize my chances.

### 1. **Modular Design**

- Creating doctypes for each model (e.g., `Company`, `Department`, `Employee`, `Project`, `Performance Review`) to ensure separation of concerns.
- Each module is responsible for its own data and logic, making the system easier to maintain and extend.

### 2. **Role-Based Access Control (RBAC)**

- The system implements **RBAC** to ensure that only authorized users can access or modify data.
- Three primary roles are supported:
    - **Admin**: Full access to all features.
    - **Manager**: Can manage employees, projects, and performance reviews within their department.
    - **Employee**: Limited access to their own profile and assigned projects.

### 3. **Workflow for Performance Reviews**

- A structured workflow was implemented for managing employee performance reviews.
- The workflow includes the following stages:
    - **Pending Review**
    - **Review Scheduled**
    - **Feedback Provided**
    - **Under Approval**
    - **Review Approved**
    - **Review Rejected**
- Transitions between stages are controlled based on user roles and conditions (e.g., feedback must be provided before submission for approval).

### 4. **Data Validation and Integrity**

- Extensive validation logic was implemented to ensure data integrity:
    - **Employee**: Ensures that the department belongs to the same company as the employee.
    - **Project**: Ensures that assigned employees belong to the same company and department as the project.
    - **Performance Review**: Prevents updates to certain fields (e.g., `employee_name`, `feedback`) after specific stages in the workflow.

### 5. **Auto-Calculated Fields**

- Fields like `number_of_departments`, `number_of_employees`, and `days_employed` are auto-calculated to reduce manual input and ensure accuracy.
- These fields are updated automatically when related records are created, updated, or deleted.

### 6. **RESTful API**

- A **RESTful API** was developed to allow external systems to interact with the application.
- The API follows REST conventions and uses appropriate HTTP methods (`GET`, `POST`, `PUT`, `DELETE`).
- Detailed API documentation is provided in the [API Documentation](docs/api/README.md).

### 7. **Error Handling and Logging**

- A global error handler was implemented to catch and log errors consistently across the application.
- Logs are stored in `logs/frappe.log` and are designed to be detailed enough for troubleshooting without exposing sensitive information.

### 8. **Testing**

- **Unit Tests**: Validate individual components and functions.
- **Integration Tests**: Ensure that different parts of the application work together correctly.

### 9. **Security**

- **Authentication**: Session-based authentication is used to secure the application.
- **Data Protection**: Inputs are validated to prevent SQL injection and other attacks.
- **Permissions**: Custom DocPerms ensure that only authorized users can access or modify data.

### 10. **Documentation**

- Comprehensive documentation was created to help users and developers understand and use the system.
- Documentation is divided into two main sections:
    - **API Documentation**: Detailed information about all API endpoints.
    - **Guides**: Explanations of data models, workflows, security, testing, and logging.

## **Project Requirements Checklist**

**1. Data Models**

**User Accounts**

- [x]  Username, Email Address (Login ID), Role

**Company**

- [x]  Company Name
- [x]  Auto-calculated fields: Departments count, Employees count, Projects count

**Department**

- [x]  Company (Select), Department Name
- [x]  Auto-calculated fields: Employees count, Projects count

**Employee**

- [x]  Basic Info: Name, Email, Mobile, Address
- [x]  Company & Department (Select fields)
- [x]  Position & Employment Details: Designation, Hire Date, Days Employed (auto-calculated)

**Project**

- [x]  Basic Info: Name, Description, Start/End Dates
- [x]  Relations: Company, Department, Assigned Employees (Multi-Select)

**2. Employee Performance Review Cycle Workflow**

**Stages**

- [x]  Pending Review
- [x]  Review Scheduled
- [x]  Feedback Provided
- [x]  Under Approval
- [x]  Review Approved
- [x]  Review Rejected

**Stage Transitions**

- [x]  Pending Review → Review Scheduled (when review date confirmed)
- [x]  Review Scheduled → Feedback Provided (when feedback recorded)
- [x]  Feedback Provided → Under Approval (when submitted for review)
- [x]  Under Approval → Review Approved (when approved by manager)
- [x]  Under Approval → Review Rejected (when rejected by manager)
- [x]  Review Rejected → Feedback Provided (when feedback updated)



**3. Security & Permissions**

**Role-Based Access Control**

- [x]  Implement different access levels (Admin, Manager, Employee)
- [x]  Restrict data viewing and editing to authorized personnel
- [x]  Implement secure authentication mechanism

**4. API Implementation**

[**Auth Endpoints**](./docs/api/auth.md.md)

- [x]  Log In.
- [x]  Log Out


[**User Endpoints**](./docs/api/user.md)

- [x]  Create a new user (Admin only).
- [x]  GET List all users (Admin only)
- [x]  GET Retrieve single user (Admin only)

[**Company Endpoints**](./docs/api/company.md)

- [x]  POST Create new company (Admin only).
- [x]  GET List all companies (Admin & Manager)
- [x]  GET Retrieve single company (Admin & Manager)
- [x]  DELETE Delete company (Admin only).
- [x]  PUT Update company (Admin only)

[**Department Endpoints**](./docs/api/department.md)

- [x]  POST Create new department (Admin only).
- [x]  GET List all departments (Admin & Manager)
- [x]  GET Retrieve single department (Admin & Manager)
- [x]  DELETE Delete department (Admin only).
- [x]  PUT Update department (Admin only)

[**Employee Endpoints**](./docs/api/employee.md)

- [x]  POST Create new employee (Admin & Manager)
- [x]  GET List all employees (Admin & Manager)
- [x]  GET Retrieve single employee (Admin & Manager) (Employee for their own profile)
- [x]  DELETE Delete employee (Admin Only)
- [x]  PUT Update employee (both partial and full update) (Admin & Manager)

[**Project Endpoints (Bonus)**](./docs/api/project.md)

- [x]  POST Create new project (Admin & Manager)
- [x]  GET List all projects (Admin & Manager)
- [x]  GET Retrieve single project (Admin & Manager) (Employee for their assigned projects)
- [x]  PUT Update project (Admin & Manager)
- [x]  DELETE Delete project (Admin Only)

- Assumption: Projects can only be assigned to employees who belong to the same company and department.

- Consideration: If an employee is reassigned to a different department, their project assignments are validated to ensure consistency.

[**Performance Reviews Endpoints**](./docs/api/project.md)

- [x]  POST Create new Performance Review (Admin & Manager)
- [x]  GET List all Performance Review (Admin & Manager)
- [x]  GET Retrieve single Performance Review (Admin & Manager) (Employee for their assigned projects)
- [x]  PUT Update Performance Review (Admin & Manager)
- [x]  DELETE Delete Performance Review (Admin Only)
- [x]  POST Handle Action Request (Admin & Manager depend on action)


**API Requirements**

- [x]  Implement secure data handling
- [x]  Follow RESTful conventions
- [x]  Create  [API Documentation](docs/api/README.md)
- [x]  Document endpoints
- [x]  Document parameters
- [x]  Document expected responses (not all)

**5. Testing**

- [x]  Unit Tests (Implement unit tests for individual components.)
- [x]  Integration Tests (Implement integration tests to ensure different parts of the application work together.)

**6. Logging**

- [x]  Implement logging to track application behavior and capture errors.


