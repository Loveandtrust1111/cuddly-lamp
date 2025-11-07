"""Tests for UserManager."""
import unittest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.user_manager import UserManager


class TestUserManager(unittest.TestCase):
    """Test cases for UserManager class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.manager = UserManager()
    
    def test_create_user_success(self):
        """Test creating a valid user."""
        user = self.manager.create_user("testuser", "test@example.com", "password123")
        self.assertEqual(user['username'], "testuser")
        self.assertEqual(user['email'], "test@example.com")
        self.assertIn('id', user)
        self.assertIn('created_at', user)
    
    def test_create_user_invalid_username(self):
        """Test creating user with invalid username."""
        with self.assertRaises(ValueError) as context:
            self.manager.create_user("ab", "test@example.com", "password123")
        self.assertIn("Username must be at least 3 characters", str(context.exception))
    
    def test_create_user_invalid_email(self):
        """Test creating user with invalid email."""
        with self.assertRaises(ValueError) as context:
            self.manager.create_user("testuser", "invalid-email", "password123")
        self.assertIn("Invalid email address", str(context.exception))
    
    def test_create_user_invalid_password(self):
        """Test creating user with invalid password."""
        with self.assertRaises(ValueError) as context:
            self.manager.create_user("testuser", "test@example.com", "short")
        self.assertIn("Password must be at least 8 characters", str(context.exception))
    
    def test_update_user_success(self):
        """Test updating a user."""
        user = self.manager.create_user("testuser", "test@example.com", "password123")
        updated = self.manager.update_user(user['id'], username="newname")
        self.assertEqual(updated['username'], "newname")
    
    def test_update_user_not_found(self):
        """Test updating non-existent user."""
        with self.assertRaises(ValueError) as context:
            self.manager.update_user(999, username="newname")
        self.assertIn("User not found", str(context.exception))
    
    def test_update_user_invalid_username(self):
        """Test updating user with invalid username."""
        user = self.manager.create_user("testuser", "test@example.com", "password123")
        with self.assertRaises(ValueError) as context:
            self.manager.update_user(user['id'], username="ab")
        self.assertIn("Username must be at least 3 characters", str(context.exception))


if __name__ == '__main__':
    unittest.main()
