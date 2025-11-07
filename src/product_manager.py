"""Product management module with duplicated code."""


class ProductManager:
    """Manages product operations."""
    
    def __init__(self):
        self.products = {}
    
    def create_product(self, name, description, price):
        """Create a new product."""
        # Validation - duplicated code pattern 1
        if not name or len(name) < 3:
            raise ValueError("Product name must be at least 3 characters long")
        if not description or len(description) < 10:
            raise ValueError("Description must be at least 10 characters long")
        if not price or price <= 0:
            raise ValueError("Price must be greater than 0")
        
        # Database operation - duplicated code pattern 2
        product_id = len(self.products) + 1
        product_data = {
            'id': product_id,
            'name': name,
            'description': description,
            'price': price,
            'created_at': self._get_timestamp(),
            'updated_at': self._get_timestamp()
        }
        self.products[product_id] = product_data
        print(f"Product created: {name}")
        return product_data
    
    def update_product(self, product_id, name=None, description=None, price=None):
        """Update an existing product."""
        if product_id not in self.products:
            raise ValueError("Product not found")
        
        # Validation - duplicated code pattern 1
        if name and len(name) < 3:
            raise ValueError("Product name must be at least 3 characters long")
        if description and len(description) < 10:
            raise ValueError("Description must be at least 10 characters long")
        if price and price <= 0:
            raise ValueError("Price must be greater than 0")
        
        # Database operation - duplicated code pattern 2
        product_data = self.products[product_id]
        if name:
            product_data['name'] = name
        if description:
            product_data['description'] = description
        if price:
            product_data['price'] = price
        product_data['updated_at'] = self._get_timestamp()
        print(f"Product updated: {product_data['name']}")
        return product_data
    
    def _get_timestamp(self):
        """Get current timestamp."""
        from datetime import datetime
        return datetime.now().isoformat()
