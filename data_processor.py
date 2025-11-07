"""A simple data processor module with duplicated code patterns."""


def process_user_data(user):
    """Process user data and return formatted string."""
    if not user:
        raise ValueError("User data cannot be empty")
    
    if "name" not in user:
        raise KeyError("User must have a name")
    
    if "email" not in user:
        raise KeyError("User must have an email")
    
    name = user["name"].strip().title()
    email = user["email"].strip().lower()
    
    return f"User: {name} ({email})"


def process_product_data(product):
    """Process product data and return formatted string."""
    if not product:
        raise ValueError("Product data cannot be empty")
    
    if "name" not in product:
        raise KeyError("Product must have a name")
    
    if "price" not in product:
        raise KeyError("Product must have a price")
    
    name = product["name"].strip().title()
    price = float(product["price"])
    
    return f"Product: {name} (${price:.2f})"


def process_order_data(order):
    """Process order data and return formatted string."""
    if not order:
        raise ValueError("Order data cannot be empty")
    
    if "id" not in order:
        raise KeyError("Order must have an id")
    
    if "total" not in order:
        raise KeyError("Order must have a total")
    
    order_id = str(order["id"]).strip()
    total = float(order["total"])
    
    return f"Order: {order_id} (${total:.2f})"
