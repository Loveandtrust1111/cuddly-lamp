"""Common utilities for the application."""
from datetime import datetime


def get_timestamp():
    """Get current timestamp in ISO format.
    
    Returns:
        str: Current timestamp in ISO 8601 format.
    """
    return datetime.now().isoformat()


def validate_min_length(value, min_length, field_name):
    """Validate that a value meets minimum length requirement.
    
    Args:
        value: The value to validate.
        min_length: Minimum required length.
        field_name: Name of the field for error messages.
        
    Raises:
        ValueError: If value is None, empty, or shorter than min_length.
    """
    if not value or len(str(value)) < min_length:
        raise ValueError(f"{field_name} must be at least {min_length} characters long")


def validate_positive_number(value, field_name):
    """Validate that a numeric value is positive.
    
    Args:
        value: The value to validate.
        field_name: Name of the field for error messages.
        
    Raises:
        ValueError: If value is None or not greater than 0.
    """
    if not value or value <= 0:
        raise ValueError(f"{field_name} must be greater than 0")


def validate_email(email):
    """Validate email address format.
    
    Args:
        email: Email address to validate.
        
    Raises:
        ValueError: If email is invalid.
    """
    if not email or '@' not in email:
        raise ValueError("Invalid email address")
