"""Product management module - refactored."""
from src.base_manager import BaseManager
from src.utils import validate_min_length, validate_positive_number


class ProductManager(BaseManager):
    """Manages product operations."""
    
    def __init__(self):
        """Initialize the product manager."""
        super().__init__()
        self.products = self._storage
    
    def create_product(self, name, description, price):
        """Create a new product.
        
        Args:
            name: Product name (min 3 characters).
            description: Product description (min 10 characters).
            price: Product price (must be positive).
            
        Returns:
            dict: The created product record.
            
        Raises:
            ValueError: If validation fails.
        """
        # Validation using extracted utilities
        validate_min_length(name, 3, "Product name")
        validate_min_length(description, 10, "Description")
        validate_positive_number(price, "Price")
        
        # Create record using base class method
        product_data = self._create_record({
            'name': name,
            'description': description,
            'price': price
        })
        print(f"Product created: {name}")
        return product_data
    
    def update_product(self, product_id, name=None, description=None, price=None):
        """Update an existing product.
        
        Args:
            product_id: ID of the product to update.
            name: New product name (optional).
            description: New description (optional).
            price: New price (optional).
            
        Returns:
            dict: The updated product record.
            
        Raises:
            ValueError: If validation fails or product not found.
        """
        # Validation using extracted utilities
        if name is not None:
            validate_min_length(name, 3, "Product name")
        if description is not None:
            validate_min_length(description, 10, "Description")
        if price is not None:
            validate_positive_number(price, "Price")
        
        # Update record using base class method
        product_data = self._update_record(product_id, {
            'name': name,
            'description': description,
            'price': price
        }, entity_name="Product")
        print(f"Product updated: {product_data['name']}")
        return product_data
