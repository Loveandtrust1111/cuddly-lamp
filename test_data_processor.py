"""Tests for data processor module."""
import pytest
from data_processor import (
    process_user_data,
    process_product_data,
    process_order_data,
)


def test_process_user_data():
    """Test user data processing."""
    user = {"name": "john doe", "email": "JOHN@EXAMPLE.COM"}
    result = process_user_data(user)
    assert result == "User: John Doe (john@example.com)"


def test_process_user_data_empty():
    """Test user data processing with empty data."""
    with pytest.raises(ValueError):
        process_user_data({})


def test_process_user_data_missing_name():
    """Test user data processing with missing name."""
    with pytest.raises(KeyError):
        process_user_data({"email": "test@example.com"})


def test_process_user_data_missing_email():
    """Test user data processing with missing email."""
    with pytest.raises(KeyError):
        process_user_data({"name": "John Doe"})


def test_process_product_data():
    """Test product data processing."""
    product = {"name": "laptop", "price": "999.99"}
    result = process_product_data(product)
    assert result == "Product: Laptop ($999.99)"


def test_process_product_data_empty():
    """Test product data processing with empty data."""
    with pytest.raises(ValueError):
        process_product_data({})


def test_process_product_data_missing_name():
    """Test product data processing with missing name."""
    with pytest.raises(KeyError):
        process_product_data({"price": 99.99})


def test_process_product_data_missing_price():
    """Test product data processing with missing price."""
    with pytest.raises(KeyError):
        process_product_data({"name": "Laptop"})


def test_process_order_data():
    """Test order data processing."""
    order = {"id": "12345", "total": "150.50"}
    result = process_order_data(order)
    assert result == "Order: 12345 ($150.50)"


def test_process_order_data_empty():
    """Test order data processing with empty data."""
    with pytest.raises(ValueError):
        process_order_data({})


def test_process_order_data_missing_id():
    """Test order data processing with missing id."""
    with pytest.raises(KeyError):
        process_order_data({"total": 100})


def test_process_order_data_missing_total():
    """Test order data processing with missing total."""
    with pytest.raises(KeyError):
        process_order_data({"id": "12345"})
