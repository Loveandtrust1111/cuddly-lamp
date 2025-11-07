"""A simple calculator module with duplicated code patterns."""


def add_numbers(a, b):
    """Add two numbers and return the result."""
    if not isinstance(a, (int, float)):
        raise TypeError("First argument must be a number")
    if not isinstance(b, (int, float)):
        raise TypeError("Second argument must be a number")
    result = a + b
    print(f"Operation: {a} + {b} = {result}")
    return result


def subtract_numbers(a, b):
    """Subtract two numbers and return the result."""
    if not isinstance(a, (int, float)):
        raise TypeError("First argument must be a number")
    if not isinstance(b, (int, float)):
        raise TypeError("Second argument must be a number")
    result = a - b
    print(f"Operation: {a} - {b} = {result}")
    return result


def multiply_numbers(a, b):
    """Multiply two numbers and return the result."""
    if not isinstance(a, (int, float)):
        raise TypeError("First argument must be a number")
    if not isinstance(b, (int, float)):
        raise TypeError("Second argument must be a number")
    result = a * b
    print(f"Operation: {a} * {b} = {result}")
    return result


def divide_numbers(a, b):
    """Divide two numbers and return the result."""
    if not isinstance(a, (int, float)):
        raise TypeError("First argument must be a number")
    if not isinstance(b, (int, float)):
        raise TypeError("Second argument must be a number")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    print(f"Operation: {a} / {b} = {result}")
    return result


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        raise ValueError("List cannot be empty")
    
    # Validate all numbers
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements must be numbers")
    
    total = 0
    for num in numbers:
        total += num
    
    average = total / len(numbers)
    print(f"Average of {numbers} = {average}")
    return average


def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    if not numbers:
        raise ValueError("List cannot be empty")
    
    # Validate all numbers
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements must be numbers")
    
    total = 0
    for num in numbers:
        total += num
    
    print(f"Sum of {numbers} = {total}")
    return total
