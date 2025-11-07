"""
Example of inefficient code patterns that should be avoided.
This file demonstrates common performance issues.
"""

import time


def inefficient_list_concatenation(items):
    """
    INEFFICIENT: Using + operator in a loop for string concatenation.
    Time Complexity: O(n²) due to string immutability
    """
    result = ""
    for item in items:
        result = result + str(item) + ","
    return result


def inefficient_list_search(data, target):
    """
    INEFFICIENT: Using list for membership testing in a loop.
    Time Complexity: O(n) for each lookup
    """
    found_items = []
    for item in data:
        if item in found_items:
            continue
        found_items.append(item)
    return found_items


def inefficient_nested_loops(list1, list2):
    """
    INEFFICIENT: Nested loops without optimization.
    Time Complexity: O(n²)
    """
    matches = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                matches.append(item1)
    return matches


def inefficient_file_reading(filename):
    """
    INEFFICIENT: Reading entire file into memory at once.
    Memory: O(n) where n is file size
    """
    with open(filename, 'r') as f:
        content = f.read()
        lines = content.split('\n')
        return [line.upper() for line in lines]


def inefficient_data_processing(data):
    """
    INEFFICIENT: Multiple iterations over the same data.
    """
    # First pass: filter
    filtered = []
    for item in data:
        if item > 0:
            filtered.append(item)
    
    # Second pass: square
    squared = []
    for item in filtered:
        squared.append(item ** 2)
    
    # Third pass: sum
    total = 0
    for item in squared:
        total += item
    
    return total


def inefficient_dictionary_lookup(data):
    """
    INEFFICIENT: Repeatedly checking if key exists instead of using get().
    """
    results = {}
    for item in data:
        if item in results:
            results[item] = results[item] + 1
        else:
            results[item] = 1
    return results


class InefficientDataStructure:
    """
    INEFFICIENT: Using inappropriate data structure for the use case.
    """
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        """O(n) lookup to check duplicates"""
        if item not in self.items:
            self.items.append(item)
    
    def has_item(self, item):
        """O(n) lookup"""
        return item in self.items
    
    def remove_item(self, item):
        """O(n) lookup and removal"""
        if item in self.items:
            self.items.remove(item)


def inefficient_global_variable():
    """
    INEFFICIENT: Using global variables that can cause cache misses
    and make code harder to optimize.
    """
    global global_counter
    global_counter = 0
    for i in range(1000000):
        global_counter += 1
    return global_counter


# Global variable (avoid this pattern)
global_counter = 0


if __name__ == "__main__":
    # Example usage
    print("Demonstrating inefficient patterns...")
    
    # Test string concatenation
    start = time.time()
    result = inefficient_list_concatenation(range(1000))
    print(f"String concatenation: {time.time() - start:.4f}s")
    
    # Test list search
    start = time.time()
    data = list(range(100)) * 10
    result = inefficient_list_search(data, 50)
    print(f"List search: {time.time() - start:.4f}s")
