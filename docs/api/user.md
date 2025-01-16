# User Management

## Create User

- **Endpoint**: `POST /api/resource/User`
- **Description**: Creates a new user. 
- **Permission**: Only accessible by Administrator & users with role Admin
- **Request Body**:
    ```json
    {
        "email": "test16@gmail.com",
        "first_name": "Mahmoud",
        "last_name": "Elwazeer",
        "username": "Mahnoud.Elwazeer",
        "new_password": "User@123",
        "roles": [
            {
                "role": "Employee"
            }
        ]
    }
    ```
    

## Get All Users


- **Endpoint**: `GET /api/resource/User`
- **Description**: Retrieves a list of all users.
- **Permission**: Only accessible by Administrator & users with roles Admin & Manager

## Get User by Name

- **Endpoint**: `GET /api/resource/User/admin@gmail.com`
- **Description**: Retrieves details of a specific user by their email.
- **Permission**: Only accessible by Administrator & users with roles Admin & Manager