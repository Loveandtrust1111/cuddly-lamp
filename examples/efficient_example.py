"""
Optimized version of the code with performance improvements.
This file demonstrates best practices for efficient code.
"""

import time
from collections import Counter


def efficient_list_concatenation(items):
    """
    EFFICIENT: Using join() for string concatenation.
    Time Complexity: O(n)
    """
    return ",".join(str(item) for item in items)


def efficient_list_search(data, target=None):
    """
    EFFICIENT: Using set for O(1) membership testing.
    Time Complexity: O(n) total
    """
    return list(set(data))


def efficient_nested_loops(list1, list2):
    """
    EFFICIENT: Using set intersection for finding common elements.
    Time Complexity: O(n + m)
    """
    return list(set(list1) & set(list2))


def efficient_file_reading_generator(filename):
    """
    EFFICIENT: Processing file line by line using generator.
    Memory: O(1) per line - truly memory efficient
    """
    try:
        with open(filename, 'r') as f:
            for line in f:
                yield line.upper()
    except FileNotFoundError:
        print(f"Warning: File {filename} not found")
        return


def efficient_file_reading(filename):
    """
    EFFICIENT: Processing file line by line with list comprehension.
    Memory: O(n) but more efficient than read() + split()
    Note: For truly memory-efficient processing, use the generator version above.
    """
    try:
        with open(filename, 'r') as f:
            return [line.upper() for line in f]
    except FileNotFoundError:
        print(f"Warning: File {filename} not found")
        return []


def efficient_data_processing(data):
    """
    EFFICIENT: Single pass using generator expression.
    Time Complexity: O(n)
    """
    return sum(item ** 2 for item in data if item > 0)


def efficient_dictionary_lookup(data):
    """
    EFFICIENT: Using get() with default value or Counter.
    """
    # Option 1: Using get()
    results = {}
    for item in data:
        results[item] = results.get(item, 0) + 1
    return results


def efficient_dictionary_lookup_counter(data):
    """
    EFFICIENT: Using Counter from collections.
    Most Pythonic and efficient approach.
    """
    return dict(Counter(data))


class EfficientDataStructure:
    """
    EFFICIENT: Using set for O(1) operations.
    """
    def __init__(self):
        self.items = set()
    
    def add_item(self, item):
        """O(1) insertion with automatic duplicate handling"""
        self.items.add(item)
    
    def has_item(self, item):
        """O(1) lookup"""
        return item in self.items
    
    def remove_item(self, item):
        """O(1) removal"""
        self.items.discard(item)


def efficient_local_variable():
    """
    EFFICIENT: Using local variables for better performance
    and code clarity.
    """
    counter = 0
    for i in range(1000000):
        counter += 1
    return counter


def efficient_list_comprehension(data):
    """
    EFFICIENT: Using list comprehension instead of append in loop.
    List comprehensions are optimized in CPython.
    """
    return [item ** 2 for item in data if item > 0]


def efficient_generator_for_large_data(data):
    """
    EFFICIENT: Using generator for memory-efficient processing.
    Only computes values as needed.
    """
    return (item ** 2 for item in data if item > 0)


def efficient_membership_testing(items, check_items):
    """
    EFFICIENT: Convert to set before multiple membership tests.
    """
    items_set = set(items)
    return [item for item in check_items if item in items_set]


def efficient_string_building(parts):
    """
    EFFICIENT: Using list and join for building strings.
    """
    result = []
    for part in parts:
        result.append(str(part))
    return "".join(result)


def efficient_dict_iteration(data_dict):
    """
    EFFICIENT: Iterating over items() instead of keys().
    """
    results = []
    for key, value in data_dict.items():
        results.append(f"{key}: {value}")
    return results


if __name__ == "__main__":
    # Example usage demonstrating performance improvements
    print("Demonstrating efficient patterns...")
    
    # Test string concatenation
    start = time.time()
    result = efficient_list_concatenation(range(1000))
    print(f"String concatenation: {time.time() - start:.4f}s")
    
    # Test list search
    start = time.time()
    data = list(range(100)) * 10
    result = efficient_list_search(data)
    print(f"List search: {time.time() - start:.4f}s")
    
    # Test data processing
    start = time.time()
    result = efficient_data_processing(range(-100, 100))
    print(f"Data processing: {time.time() - start:.4f}s, Result: {result}")
    
    # Test Counter
    start = time.time()
    result = efficient_dictionary_lookup_counter([1, 2, 2, 3, 3, 3])
    print(f"Counter: {time.time() - start:.4f}s, Result: {result}")
