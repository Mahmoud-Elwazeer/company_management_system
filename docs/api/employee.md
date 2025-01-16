# Employee Management

## Get Employees

- **Endpoint**: `GET /api/resource/Employee`
- **Description**: Retrieves a list of all employees name.
- **Permission**: Only accessible by Administrator & users with roles Admin & Manager & Employee (All Roles)

## Get Employee by Name

- **Endpoint**: `GET /api/resource/Employee/Mahmoud Elwazeer-001`
- **Description**: Retrieves details of a specific employee by their name.
- **Permission**: Only accessible by Administrator & users with roles Admin & Manager or Employee (but only for their own profile).

## Add New Employee

- **Endpoint**: `POST /api/resource/Employee`
- **Description**: Creates a new employee.
- **Permission**: Only accessible by Administrator & users with roles Admin & Manager 
- **Request Body**:
    ```json
    {
        "company": "BrainWise",
        "department": "Backend",
        "employee_name": "Mahmoud Elwazeer",
        "email_address": "test@gmail.com",
        "mobile_number": "+201021489200",
        "designation": "Junior Backend Engineer"
    }
    ```

## Update Employee by Name

- **Endpoint**: `PUT /api/resource/Employee/Mahmoud Elwazeer`
- **Description**: Updates details of a specific employee by their name.
- **Permission**: Only accessible by Administrator & users with roles Admin & Manager 
- **Request Body**:
    ```json
    {
        "hired_on": "2025-02-01"
    }
    ```

### Delete Employee by Name

- **Endpoint**: `DELETE /api/resource/Employee/Mahmoud Elwazeer`
- **Description**: Deletes a specific employee by their name.
- **Permission**: Only accessible by Administrator & users with role Admin 