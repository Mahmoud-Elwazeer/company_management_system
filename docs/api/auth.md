# Authentication

## 1. Log In

- **Endpoint**: `POST /api/method/login`
- **Description**: Authenticates a user and returns a session cookie.
- **Request Body**:
    
    ```json
    {
        "usr": "admin@gmail.com",
        "pwd": "User@123"
    }
    ```

## Log Out

- **Endpoint**: `POST /api/method/logout`
- **Description**: Logs out the current user and invalidates the session cookie.
- **Headers**:
    - `Accept: application/json`
    - `Content-Type: application/json`