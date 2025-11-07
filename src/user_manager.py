"""User management module with duplicated code."""


class UserManager:
    """Manages user operations."""
    
    def __init__(self):
        self.users = {}
    
    def create_user(self, username, email, password):
        """Create a new user."""
        # Validation - duplicated code pattern 1
        if not username or len(username) < 3:
            raise ValueError("Username must be at least 3 characters long")
        if not email or '@' not in email:
            raise ValueError("Invalid email address")
        if not password or len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        
        # Database operation - duplicated code pattern 2
        user_id = len(self.users) + 1
        user_data = {
            'id': user_id,
            'username': username,
            'email': email,
            'password': password,
            'created_at': self._get_timestamp(),
            'updated_at': self._get_timestamp()
        }
        self.users[user_id] = user_data
        print(f"User created: {username}")
        return user_data
    
    def update_user(self, user_id, username=None, email=None, password=None):
        """Update an existing user."""
        if user_id not in self.users:
            raise ValueError("User not found")
        
        # Validation - duplicated code pattern 1
        if username and len(username) < 3:
            raise ValueError("Username must be at least 3 characters long")
        if email and '@' not in email:
            raise ValueError("Invalid email address")
        if password and len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        
        # Database operation - duplicated code pattern 2
        user_data = self.users[user_id]
        if username:
            user_data['username'] = username
        if email:
            user_data['email'] = email
        if password:
            user_data['password'] = password
        user_data['updated_at'] = self._get_timestamp()
        print(f"User updated: {user_data['username']}")
        return user_data
    
    def _get_timestamp(self):
        """Get current timestamp."""
        from datetime import datetime
        return datetime.now().isoformat()
