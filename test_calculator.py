"""Tests for calculator module."""
import pytest
from calculator import (
    add_numbers,
    subtract_numbers,
    multiply_numbers,
    divide_numbers,
    calculate_average,
    calculate_sum,
)


def test_add_numbers():
    """Test addition function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0.5, 0.5) == 1.0


def test_add_numbers_invalid_input():
    """Test addition with invalid input."""
    with pytest.raises(TypeError):
        add_numbers("2", 3)
    with pytest.raises(TypeError):
        add_numbers(2, "3")


def test_subtract_numbers():
    """Test subtraction function."""
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(1, 1) == 0
    assert subtract_numbers(0.5, 0.3) == pytest.approx(0.2)


def test_subtract_numbers_invalid_input():
    """Test subtraction with invalid input."""
    with pytest.raises(TypeError):
        subtract_numbers("5", 3)


def test_multiply_numbers():
    """Test multiplication function."""
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(-2, 3) == -6
    assert multiply_numbers(0.5, 2) == 1.0


def test_multiply_numbers_invalid_input():
    """Test multiplication with invalid input."""
    with pytest.raises(TypeError):
        multiply_numbers(2, None)


def test_divide_numbers():
    """Test division function."""
    assert divide_numbers(6, 3) == 2
    assert divide_numbers(5, 2) == 2.5
    assert divide_numbers(1, 4) == 0.25


def test_divide_numbers_by_zero():
    """Test division by zero."""
    with pytest.raises(ValueError):
        divide_numbers(5, 0)


def test_divide_numbers_invalid_input():
    """Test division with invalid input."""
    with pytest.raises(TypeError):
        divide_numbers(6, "3")


def test_calculate_average():
    """Test average calculation."""
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    assert calculate_average([10, 20]) == 15.0
    assert calculate_average([5]) == 5.0


def test_calculate_average_empty_list():
    """Test average with empty list."""
    with pytest.raises(ValueError):
        calculate_average([])


def test_calculate_average_invalid_input():
    """Test average with invalid input."""
    with pytest.raises(TypeError):
        calculate_average([1, 2, "3"])


def test_calculate_sum():
    """Test sum calculation."""
    assert calculate_sum([1, 2, 3, 4, 5]) == 15
    assert calculate_sum([10, 20]) == 30
    assert calculate_sum([5]) == 5


def test_calculate_sum_empty_list():
    """Test sum with empty list."""
    with pytest.raises(ValueError):
        calculate_sum([])


def test_calculate_sum_invalid_input():
    """Test sum with invalid input."""
    with pytest.raises(TypeError):
        calculate_sum([1, 2, "3"])
