# Performance Review Management

## Get Performance Reviews

- **Endpoint**: `GET /api/resource/Performance Review`
- **Description**: Retrieves a list of all performance reviews.
- **Permission**: Only accessible by Administrator & users with roles Admin & Manager

## Get Performance Review by Name

- **Endpoint**: `GET /api/resource/Performance Review/Mahmoud Elwazeer-001-001`
- **Description**: Retrieves details of a specific performance review by its name.
- **Permission**: Only accessible by Administrator & users with roles Admin & Manager

## Add New Performance Review

- **Endpoint**: `POST /api/resource/Performance Review`
- **Description**: Creates a new performance review.
- **Permission**: Only accessible by Administrator & users with roles Admin & Manager
- **Request Body**:
    ```json
    {
        "employee_name": "Mahmoud Elwazeer-003"
    }
    ```

## Update Performance Review by Name

- **Endpoint**: `PUT /api/resource/Performance Review/Mahmoud Elwazeer-001-001`
- **Description**: Updates details of a specific performance review by its name.
- **Permission**: Only accessible by Administrator & users with roles Admin & Manager
- **Request Body**:
    ```json
    {
        "review_date": "2025-02-20",
        "feedback": "feedback"
    }
    ```

## Delete Performance Review by Name

- **Endpoint**: `DELETE /api/resource/Performance Review/Mahmoud Elwazeer-001-001`
- **Description**: Deletes a specific performance review by its name.
- **Permission**: Only accessible by Administrator & users with role Admin.

## Handle Workflow Action Request

- **Endpoint**: `POST /api/method/frappe.model.workflow.apply_workflow`
- **Description**: Handles workflow actions for performance reviews.
- **Permissions**:
    - Actions (Confirm Review Date, Record Feedback, Submit for Approval ) available only for who have role Manager
    - Permission actions ( Approve Feedback, Reject Feedback, Update Feedback ) available only for who have role Admin
- **Request Body**:
    ```json
    {
        "action": "Approve Feedback",
        "doc": {
            "name": "Mahmoud Elwazeer-001-001",
            "doctype": "Performance Review"
        }
    }
    ```
- **Available Actions**:
    - Confirm Review Date
    - Record Feedback
    - Submit for Approval
    - Approve Feedback
    - Reject Feedback
    - Update Feedback

- **Notes for Troubleshooting:**
    - before action Confirm Review Date make sure review_date available for doc or update it if not available
    - before action Submit for Approval make sure feedback available for doc or update it if not available
