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
    ineff_time, _ = benchmark(inefficient_list_concatenation, items)
    eff_time, _ = benchmark(efficient_list_concatenation, items)
    print_benchmark_result("String Concatenation", ineff_time, eff_time)
    
    # Benchmark 2: List Search (Duplicate Removal)
    print("\n[2] List Search - Duplicate Removal (1,000 items with duplicates)")
    data = list(range(100)) * 10
    ineff_time, ineff_result = benchmark(inefficient_list_search, data, None)
    eff_time, eff_result = benchmark(efficient_list_search, data, None)
    print_benchmark_result("List Search", ineff_time, eff_time)
    print(f"  Results match: {set(ineff_result) == set(eff_result)}")
    
    # Benchmark 3: Nested Loops (Finding Common Elements)
    print("\n[3] Nested Loops - Finding Common Elements")
    list1 = list(range(1000))
    list2 = list(range(500, 1500))
    ineff_time, ineff_result = benchmark(inefficient_nested_loops, list1, list2)
    eff_time, eff_result = benchmark(efficient_nested_loops, list1, list2)
    print_benchmark_result("Nested Loops", ineff_time, eff_time)
    print(f"  Results match: {set(ineff_result) == set(eff_result)}")
    
    # Benchmark 4: Data Processing
    print("\n[4] Data Processing - Filter, Square, Sum (100,000 items)")
    data = list(range(-50000, 50000))
    ineff_time, ineff_result = benchmark(inefficient_data_processing, data)
    eff_time, eff_result = benchmark(efficient_data_processing, data)
    print_benchmark_result("Data Processing", ineff_time, eff_time)
    print(f"  Results match: {ineff_result == eff_result}")
    
    # Benchmark 5: Dictionary Operations
    print("\n[5] Dictionary Operations - Counting (10,000 items)")
    data = [i % 100 for i in range(10000)]
    ineff_time, ineff_result = benchmark(inefficient_dictionary_lookup, data)
    eff_time, eff_result = benchmark(efficient_dictionary_lookup_counter, data)
    print_benchmark_result("Dictionary Lookup", ineff_time, eff_time)
    print(f"  Results match: {ineff_result == eff_result}")
    
    # Benchmark 6: Data Structure Operations
    print("\n[6] Data Structure Operations - Add/Check (10,000 operations)")
    
    def test_inefficient_ds():
        ds = InefficientDataStructure()
        for i in range(1000):
            ds.add_item(i)
        for i in range(1000):
            ds.has_item(i % 500)
        return ds
    
    def test_efficient_ds():
        ds = EfficientDataStructure()
        for i in range(1000):
            ds.add_item(i)
        for i in range(1000):
            ds.has_item(i % 500)
        return ds
    
    ineff_time, _ = benchmark(test_inefficient_ds)
    eff_time, _ = benchmark(test_efficient_ds)
    print_benchmark_result("Data Structure Operations", ineff_time, eff_time)
    
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
