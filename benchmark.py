"""
Benchmark script to compare inefficient vs efficient implementations.
Run this to see the performance differences in practice.
"""

import time
import sys
from examples.inefficient_example import (
    inefficient_list_concatenation,
    inefficient_list_search,
    inefficient_nested_loops,
    inefficient_data_processing,
    inefficient_dictionary_lookup,
    InefficientDataStructure
)
from examples.efficient_example import (
    efficient_list_concatenation,
    efficient_list_search,
    efficient_nested_loops,
    efficient_data_processing,
    efficient_dictionary_lookup_counter,
    EfficientDataStructure
)


def benchmark(func, *args, iterations=1):
    """Benchmark a function and return execution time."""
    start = time.time()
    for _ in range(iterations):
        result = func(*args)
    end = time.time()
    return end - start, result


def format_speedup(inefficient_time, efficient_time):
    """Calculate and format the speedup factor."""
    if efficient_time == 0:
        return "∞"
    speedup = inefficient_time / efficient_time
    return f"{speedup:.2f}x"


def print_benchmark_result(name, inefficient_time, efficient_time):
    """Print benchmark results in a formatted way."""
    speedup = format_speedup(inefficient_time, efficient_time)
    print(f"\n{name}:")
    print(f"  Inefficient: {inefficient_time:.6f}s")
    print(f"  Efficient:   {efficient_time:.6f}s")
    print(f"  Speedup:     {speedup}")


def main():
    print("=" * 60)
    print("Performance Benchmark: Inefficient vs Efficient Code")
    print("=" * 60)
    
    # Benchmark 1: String Concatenation
    print("\n[1] String Concatenation (10,000 items)")
    items = range(10000)
    inefficient_time, _ = benchmark(inefficient_list_concatenation, items)
    efficient_time, _ = benchmark(efficient_list_concatenation, items)
    print_benchmark_result("String Concatenation", inefficient_time, efficient_time)
    
    # Benchmark 2: List Search (Duplicate Removal)
    print("\n[2] List Search - Duplicate Removal (1,000 items with duplicates)")
    data = list(range(100)) * 10
    inefficient_time, inefficient_result = benchmark(inefficient_list_search, data, None)
    efficient_time, efficient_result = benchmark(efficient_list_search, data, None)
    print_benchmark_result("List Search", inefficient_time, efficient_time)
    print(f"  Results match: {set(inefficient_result) == set(efficient_result)}")
    
    # Benchmark 3: Nested Loops (Finding Common Elements)
    print("\n[3] Nested Loops - Finding Common Elements")
    list1 = list(range(1000))
    list2 = list(range(500, 1500))
    inefficient_time, inefficient_result = benchmark(inefficient_nested_loops, list1, list2)
    efficient_time, efficient_result = benchmark(efficient_nested_loops, list1, list2)
    print_benchmark_result("Nested Loops", inefficient_time, efficient_time)
    print(f"  Results match: {set(inefficient_result) == set(efficient_result)}")
    
    # Benchmark 4: Data Processing
    print("\n[4] Data Processing - Filter, Square, Sum (100,000 items)")
    data = list(range(-50000, 50000))
    inefficient_time, inefficient_result = benchmark(inefficient_data_processing, data)
    efficient_time, efficient_result = benchmark(efficient_data_processing, data)
    print_benchmark_result("Data Processing", inefficient_time, efficient_time)
    print(f"  Results match: {inefficient_result == efficient_result}")
    
    # Benchmark 5: Dictionary Operations
    print("\n[5] Dictionary Operations - Counting (10,000 items)")
    data = [item_value % 100 for item_value in range(10000)]
    inefficient_time, inefficient_result = benchmark(inefficient_dictionary_lookup, data)
    efficient_time, efficient_result = benchmark(efficient_dictionary_lookup_counter, data)
    print_benchmark_result("Dictionary Lookup", inefficient_time, efficient_time)
    print(f"  Results match: {inefficient_result == efficient_result}")
    
    # Benchmark 6: Data Structure Operations
    print("\n[6] Data Structure Operations - Add/Check (10,000 operations)")
    
    def test_inefficient_data_structure():
        data_structure = InefficientDataStructure()
        for item_index in range(1000):
            data_structure.add_item(item_index)
        for operation_num in range(1000):
            data_structure.has_item(operation_num % 500)
        return data_structure
    
    def test_efficient_data_structure():
        data_structure = EfficientDataStructure()
        for item_index in range(1000):
            data_structure.add_item(item_index)
        for operation_num in range(1000):
            data_structure.has_item(operation_num % 500)
        return data_structure
    
    inefficient_time, _ = benchmark(test_inefficient_data_structure)
    efficient_time, _ = benchmark(test_efficient_data_structure)
    print_benchmark_result("Data Structure Operations", inefficient_time, efficient_time)
    
    # Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print("\nKey Takeaways:")
    print("1. String concatenation: Use join() instead of + in loops")
    print("2. Membership testing: Use set instead of list for O(1) lookups")
    print("3. Finding common elements: Use set operations instead of nested loops")
    print("4. Multiple operations: Combine into single pass when possible")
    print("5. Counting: Use Counter from collections module")
    print("6. Data structures: Choose the right structure for your use case")
    print("\nFor more details, see PERFORMANCE.md")
    print("=" * 60)


if __name__ == "__main__":
    main()
