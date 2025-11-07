"""Base manager class with common functionality."""
from src.utils import get_timestamp


class BaseManager:
    """Base class for entity managers with common CRUD operations."""
    
    def __init__(self):
        """Initialize the base manager."""
        self._storage = {}
        self._id_counter = 0
    
    def _generate_id(self):
        """Generate a new unique ID.
        
        Returns:
            int: A new unique identifier.
        """
        self._id_counter += 1
        return self._id_counter
    
    def _create_record(self, data):
        """Create a new record with common metadata.
        
        Args:
            data: Dictionary containing the record data.
            
        Returns:
            dict: The created record with id and timestamps.
        """
        record_id = self._generate_id()
        record = {
            'id': record_id,
            **data,
            'created_at': get_timestamp(),
            'updated_at': get_timestamp()
        }
        self._storage[record_id] = record
        return record
    
    def _update_record(self, record_id, updates, entity_name="Record"):
        """Update an existing record.
        
        Args:
            record_id: ID of the record to update.
            updates: Dictionary of fields to update.
            entity_name: Name of the entity for error messages (default: "Record").
            
        Returns:
            dict: The updated record.
            
        Raises:
            ValueError: If record is not found.
        """
        if record_id not in self._storage:
            raise ValueError(f"{entity_name} not found")
        
        record = self._storage[record_id]
        for key, value in updates.items():
            if value is not None:
                record[key] = value
        record['updated_at'] = get_timestamp()
        return record
    
    def _get_record(self, record_id, entity_name="Record"):
        """Get a record by ID.
        
        Args:
            record_id: ID of the record to retrieve.
            entity_name: Name of the entity for error messages (default: "Record").
            
        Returns:
            dict: The requested record.
            
        Raises:
            ValueError: If record is not found.
        """
        if record_id not in self._storage:
            raise ValueError(f"{entity_name} not found")
        return self._storage[record_id]
