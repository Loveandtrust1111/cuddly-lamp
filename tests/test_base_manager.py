"""Tests for BaseManager class."""
import unittest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.base_manager import BaseManager


class TestBaseManager(unittest.TestCase):
    """Test cases for BaseManager class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.manager = BaseManager()
    
    def test_initialization(self):
        """Test manager initialization."""
        self.assertEqual(len(self.manager._storage), 0)
        self.assertEqual(self.manager._id_counter, 0)
    
    def test_generate_id(self):
        """Test ID generation."""
        id1 = self.manager._generate_id()
        id2 = self.manager._generate_id()
        self.assertEqual(id1, 1)
        self.assertEqual(id2, 2)
    
    def test_create_record(self):
        """Test record creation."""
        record = self.manager._create_record({
            'name': 'Test',
            'value': 42
        })
        self.assertEqual(record['id'], 1)
        self.assertEqual(record['name'], 'Test')
        self.assertEqual(record['value'], 42)
        self.assertIn('created_at', record)
        self.assertIn('updated_at', record)
        self.assertEqual(len(self.manager._storage), 1)
    
    def test_update_record(self):
        """Test record update."""
        record = self.manager._create_record({'name': 'Test', 'value': 42})
        original_created_at = record['created_at']
        
        updated = self.manager._update_record(record['id'], {
            'name': 'Updated',
            'value': None  # None values should not update
        })
        
        self.assertEqual(updated['name'], 'Updated')
        self.assertEqual(updated['value'], 42)  # Should remain unchanged
        self.assertEqual(updated['created_at'], original_created_at)  # Should not change
        self.assertNotEqual(updated['updated_at'], original_created_at)  # Should be updated
    
    def test_update_record_not_found(self):
        """Test updating non-existent record."""
        with self.assertRaises(ValueError) as context:
            self.manager._update_record(999, {'name': 'Test'})
        self.assertIn("Record not found", str(context.exception))
    
    def test_update_record_custom_entity_name(self):
        """Test updating non-existent record with custom entity name."""
        with self.assertRaises(ValueError) as context:
            self.manager._update_record(999, {'name': 'Test'}, entity_name="CustomEntity")
        self.assertIn("CustomEntity not found", str(context.exception))
    
    def test_get_record(self):
        """Test getting a record."""
        record = self.manager._create_record({'name': 'Test'})
        retrieved = self.manager._get_record(record['id'])
        self.assertEqual(retrieved, record)
    
    def test_get_record_not_found(self):
        """Test getting non-existent record."""
        with self.assertRaises(ValueError) as context:
            self.manager._get_record(999)
        self.assertIn("Record not found", str(context.exception))
    
    def test_get_record_custom_entity_name(self):
        """Test getting non-existent record with custom entity name."""
        with self.assertRaises(ValueError) as context:
            self.manager._get_record(999, entity_name="Widget")
        self.assertIn("Widget not found", str(context.exception))


if __name__ == '__main__':
    unittest.main()
