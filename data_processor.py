"""A simple data processor module with refactored code."""


def _validate_data(data, data_type, required_fields):
    """Validate that data is not empty and contains required fields."""
    if not data:
        raise ValueError(f"{data_type} data cannot be empty")
    
    for field in required_fields:
        if field not in data:
            raise KeyError(f"{data_type} must have a {field}")


def process_user_data(user):
    """Process user data and return formatted string."""
    _validate_data(user, "User", ["name", "email"])
    
    name = user["name"].strip().title()
    email = user["email"].strip().lower()
    
    return f"User: {name} ({email})"


def process_product_data(product):
    """Process product data and return formatted string."""
    _validate_data(product, "Product", ["name", "price"])
    
    name = product["name"].strip().title()
    price = float(product["price"])
    
    return f"Product: {name} (${price:.2f})"


def process_order_data(order):
    """Process order data and return formatted string."""
    _validate_data(order, "Order", ["id", "total"])
    
    order_id = str(order["id"]).strip()
    total = float(order["total"])
    
    return f"Order: {order_id} (${total:.2f})"
