# Logging


## Logging Configuration
- **Log Level**: Set to `INFO` by default. Can be changed to `DEBUG` for more detailed logs.
- **Log File**: Logs are stored in `logs/frappe.log`.

## Error Handling
- **Global Error Handler**: All errors are caught and logged using a global error handler.
- **Sensitive Information**: Logs do not expose sensitive information like passwords.
