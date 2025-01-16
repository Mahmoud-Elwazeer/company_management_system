# Department Management

## Get Departments

- **Endpoint**: `GET /api/resource/Department
- **Description**: Retrieves a list of departments with option filtered by company.
- **params**:  ```filters```
- **Permission**: Only accessible by Administrator & users with roles Admin and Manager

## Get Department by Name

- **Endpoint**: `GET /api/resource/Department/Test`
- **Description**: Retrieves details of a specific department by its name.
- **Permission**: Only accessible by Administrator & users with roles Admin and Manager

## Add Department
- **Endpoint**: `POST /api/resource/Department`
- **Description**: Creates a new department.
- **Permission**: Only accessible by Administrator & users with role Admin
- **Request Body**:
    ```json
    {
        "company": "BrainWise",
        "department_name": "Test"
    }
    ```

## Delete Department

- **Endpoint**: `DELETE /api/resource/Department/Backend`
- **Description**: Deletes a specific department by its name.
- **Permission**: Only accessible by Administrator & users with roles Admin