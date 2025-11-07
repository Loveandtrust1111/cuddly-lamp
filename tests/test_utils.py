"""Tests for utility functions."""
import unittest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.utils import (
    get_timestamp,
    validate_min_length,
    validate_positive_number,
    validate_email
)


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""
    
    def test_get_timestamp(self):
        """Test timestamp generation."""
        timestamp = get_timestamp()
        self.assertIsInstance(timestamp, str)
        self.assertIn('T', timestamp)  # ISO format contains 'T'
    
    def test_validate_min_length_valid(self):
        """Test validate_min_length with valid input."""
        # Should not raise exception
        validate_min_length("hello", 3, "Test field")
    
    def test_validate_min_length_too_short(self):
        """Test validate_min_length with too short input."""
        with self.assertRaises(ValueError) as context:
            validate_min_length("ab", 3, "Test field")
        self.assertIn("Test field must be at least 3 characters", str(context.exception))
    
    def test_validate_min_length_none(self):
        """Test validate_min_length with None."""
        with self.assertRaises(ValueError) as context:
            validate_min_length(None, 3, "Test field")
        self.assertIn("Test field must be at least 3 characters", str(context.exception))
    
    def test_validate_min_length_empty(self):
        """Test validate_min_length with empty string."""
        with self.assertRaises(ValueError) as context:
            validate_min_length("", 3, "Test field")
        self.assertIn("Test field must be at least 3 characters", str(context.exception))
    
    def test_validate_positive_number_valid(self):
        """Test validate_positive_number with valid input."""
        # Should not raise exception
        validate_positive_number(5, "Price")
        validate_positive_number(0.01, "Price")
    
    def test_validate_positive_number_zero(self):
        """Test validate_positive_number with zero."""
        with self.assertRaises(ValueError) as context:
            validate_positive_number(0, "Price")
        self.assertIn("Price must be greater than 0", str(context.exception))
    
    def test_validate_positive_number_negative(self):
        """Test validate_positive_number with negative number."""
        with self.assertRaises(ValueError) as context:
            validate_positive_number(-5, "Price")
        self.assertIn("Price must be greater than 0", str(context.exception))
    
    def test_validate_positive_number_none(self):
        """Test validate_positive_number with None."""
        with self.assertRaises(ValueError) as context:
            validate_positive_number(None, "Price")
        self.assertIn("Price must be greater than 0", str(context.exception))
    
    def test_validate_email_valid(self):
        """Test validate_email with valid email."""
        # Should not raise exception
        validate_email("test@example.com")
        validate_email("user@domain.co.uk")
    
    def test_validate_email_invalid(self):
        """Test validate_email with invalid email."""
        with self.assertRaises(ValueError) as context:
            validate_email("invalid-email")
        self.assertIn("Invalid email address", str(context.exception))
    
    def test_validate_email_none(self):
        """Test validate_email with None."""
        with self.assertRaises(ValueError) as context:
            validate_email(None)
        self.assertIn("Invalid email address", str(context.exception))


if __name__ == '__main__':
    unittest.main()
