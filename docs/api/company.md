# Company Management

## Get Companies

- **Endpoint**: `GET /api/resource/Company`
- **Description**: Retrieves a list of all companies.
- **Permission**: Only accessible by Administrator & users with roles Admin and Manager

## Get Company by Name

- **Endpoint**: `GET /api/resource/Company/Test C`
- **Description**: Retrieves details of a specific company by its name.
- **Permission**: Only accessible by Administrator & users with roles Admin & Manager

## Create Company

- **Endpoint**: `POST /api/resource/Company`
- **Description**: Creates a new company. Only accessible by users with the Admin role.
- **Permission**: Only accessible by Administrator & users with role Admin
- **Request Body**:
    ```json
    {
        "company_name": "Test"
    }
    ```

## Delete Company

- **Endpoint**: `DELETE /api/resource/Company/Test`
- **Description**: Deletes a specific company by its name. Only accessible by users with the Admin role.
- **Permission**: Only accessible by Administrator & users with role Admin