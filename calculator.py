"""A simple calculator module with refactored code."""


def _validate_number(value, argument_name):
    """Validate that a value is a number."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"{argument_name} must be a number")


def _validate_number_list(numbers):
    """Validate that all elements in a list are numbers."""
    if not numbers:
        raise ValueError("List cannot be empty")
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements must be numbers")


def _perform_operation(a, b, operator, operation_func):
    """Perform a binary operation with validation and logging."""
    _validate_number(a, "First argument")
    _validate_number(b, "Second argument")
    result = operation_func(a, b)
    print(f"Operation: {a} {operator} {b} = {result}")
    return result


def add_numbers(a, b):
    """Add two numbers and return the result."""
    return _perform_operation(a, b, "+", lambda x, y: x + y)


def subtract_numbers(a, b):
    """Subtract two numbers and return the result."""
    return _perform_operation(a, b, "-", lambda x, y: x - y)


def multiply_numbers(a, b):
    """Multiply two numbers and return the result."""
    return _perform_operation(a, b, "*", lambda x, y: x * y)


def divide_numbers(a, b):
    """Divide two numbers and return the result."""
    _validate_number(b, "Second argument")  # Validate b first for zero check
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return _perform_operation(a, b, "/", lambda x, y: x / y)


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    _validate_number_list(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    print(f"Average of {numbers} = {average}")
    return average


def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    _validate_number_list(numbers)
    total = sum(numbers)
    print(f"Sum of {numbers} = {total}")
    return total
