"""Tests for ProductManager."""
import unittest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.product_manager import ProductManager


class TestProductManager(unittest.TestCase):
    """Test cases for ProductManager class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.manager = ProductManager()
    
    def test_create_product_success(self):
        """Test creating a valid product."""
        product = self.manager.create_product("Widget", "A useful widget", 19.99)
        self.assertEqual(product['name'], "Widget")
        self.assertEqual(product['description'], "A useful widget")
        self.assertEqual(product['price'], 19.99)
        self.assertIn('id', product)
        self.assertIn('created_at', product)
    
    def test_create_product_invalid_name(self):
        """Test creating product with invalid name."""
        with self.assertRaises(ValueError) as context:
            self.manager.create_product("Wi", "A useful widget", 19.99)
        self.assertIn("Product name must be at least 3 characters", str(context.exception))
    
    def test_create_product_invalid_description(self):
        """Test creating product with invalid description."""
        with self.assertRaises(ValueError) as context:
            self.manager.create_product("Widget", "Short", 19.99)
        self.assertIn("Description must be at least 10 characters", str(context.exception))
    
    def test_create_product_invalid_price(self):
        """Test creating product with invalid price."""
        with self.assertRaises(ValueError) as context:
            self.manager.create_product("Widget", "A useful widget", -5)
        self.assertIn("Price must be greater than 0", str(context.exception))
    
    def test_update_product_success(self):
        """Test updating a product."""
        product = self.manager.create_product("Widget", "A useful widget", 19.99)
        updated = self.manager.update_product(product['id'], name="NewWidget")
        self.assertEqual(updated['name'], "NewWidget")
    
    def test_update_product_not_found(self):
        """Test updating non-existent product."""
        with self.assertRaises(ValueError) as context:
            self.manager.update_product(999, name="NewWidget")
        self.assertIn("Product not found", str(context.exception))
    
    def test_update_product_invalid_price(self):
        """Test updating product with invalid price."""
        product = self.manager.create_product("Widget", "A useful widget", 19.99)
        with self.assertRaises(ValueError) as context:
            self.manager.update_product(product['id'], price=-10)
        self.assertIn("Price must be greater than 0", str(context.exception))


if __name__ == '__main__':
    unittest.main()
