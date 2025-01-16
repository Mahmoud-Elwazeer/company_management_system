# Project Management

## Get Projects

- **Endpoint**: `GET /api/resource/Project`
- **Description**: Retrieves a list of all projects name.
- **Permission**: Only accessible by Administrator & users with roles Admin & Manager & Employee (All Roles)

## Get Project by Name

- **Endpoint**: `GET /api/resource/Project/Frappe`
- **Description**: Retrieves details of a specific project by its name.
- **Permission**: Only accessible by Administrator & users with roles Admin & Manager or Employee (but only for their assigned projects).

## Add New Project

- **Endpoint**: `POST /api/resource/Project`
- **Description**: Creates a new project.
- **Permission**: Only accessible by Administrator & users with roles Admin & Manager
- **Request Body**:
    ```json
    {
        "company": "BrainWise",
        "department": "Backend",
        "project_name": "Test",
        "description": "Test",   // optional
        "start_date": "2025-01-14",
        "end_date": "2025-01-17",  // optional
        "assigned_employees": [
            {
                "employee_name": "Mahmoud Elwazeer-001"
            }
        ]
    }
    ```

## Update Project by Name

- **Endpoint**: `PUT /api/resource/Project/Test-0001`
- **Description**: Updates details of a specific project by its name.
- **Permission**: Only accessible by Administrator & users with roles Admin & Manager
- **Request Body**:
    ```json
    {
        "description": "Build a System for companies",
        "end_date": "2025-01-18"
    }
    ```


## Delete Project by Name

- **Endpoint**: `DELETE /api/resource/Project/Test-0001`
- **Description**: Deletes a specific project by its name.
- **Permission**: Only accessible by Administrator & users with role Admin