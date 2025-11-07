"""User management module - refactored."""
from src.base_manager import BaseManager
from src.utils import validate_min_length, validate_email


class UserManager(BaseManager):
    """Manages user operations."""
    
    def __init__(self):
        """Initialize the user manager."""
        super().__init__()
        self.users = self._storage
    
    def create_user(self, username, email, password):
        """Create a new user.
        
        Args:
            username: User's username (min 3 characters).
            email: User's email address.
            password: User's password (min 8 characters).
            
        Returns:
            dict: The created user record.
            
        Raises:
            ValueError: If validation fails.
        """
        # Validation using extracted utilities
        validate_min_length(username, 3, "Username")
        validate_email(email)
        validate_min_length(password, 8, "Password")
        
        # Create record using base class method
        user_data = self._create_record({
            'username': username,
            'email': email,
            'password': password
        })
        print(f"User created: {username}")
        return user_data
    
    def update_user(self, user_id, username=None, email=None, password=None):
        """Update an existing user.
        
        Args:
            user_id: ID of the user to update.
            username: New username (optional).
            email: New email (optional).
            password: New password (optional).
            
        Returns:
            dict: The updated user record.
            
        Raises:
            ValueError: If validation fails or user not found.
        """
        # Validation using extracted utilities
        if username is not None:
            validate_min_length(username, 3, "Username")
        if email is not None:
            validate_email(email)
        if password is not None:
            validate_min_length(password, 8, "Password")
        
        # Update record using base class method
        user_data = self._update_record(user_id, {
            'username': username,
            'email': email,
            'password': password
        }, entity_name="User")
        print(f"User updated: {user_data['username']}")
        return user_data
