"""
Benchmark script to compare performance between original and optimized versions.
"""

import time
import statistics
from data_processor import DataProcessor
from data_processor_optimized import OptimizedDataProcessor


def benchmark_function(func, *args, iterations=3, **kwargs):
    """Benchmark a function with multiple iterations."""
    times = []
    result = None
    
    for _ in range(iterations):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        times.append(elapsed)
    
    return {
        'mean': statistics.mean(times),
        'min': min(times),
        'max': max(times),
        'result': result
    }


def run_benchmarks():
    """Run comprehensive benchmarks comparing both implementations."""
    print("=" * 80)
    print("PERFORMANCE BENCHMARK COMPARISON")
    print("=" * 80)
    
    original = DataProcessor()
    optimized = OptimizedDataProcessor()
    
    # Benchmark 1: Find Duplicates
    print("\n1. FIND DUPLICATES")
    print("-" * 80)
    test_data = list(range(1000)) + list(range(500))
    
    print("Original implementation:")
    orig_result = benchmark_function(original.find_duplicates, test_data)
    print(f"  Average time: {orig_result['mean']:.4f}s")
    print(f"  Min time: {orig_result['min']:.4f}s")
    print(f"  Max time: {orig_result['max']:.4f}s")
    
    print("\nOptimized implementation:")
    opt_result = benchmark_function(optimized.find_duplicates, test_data)
    print(f"  Average time: {opt_result['mean']:.4f}s")
    print(f"  Min time: {opt_result['min']:.4f}s")
    print(f"  Max time: {opt_result['max']:.4f}s")
    
    speedup = orig_result['mean'] / opt_result['mean']
    print(f"\n  Speedup: {speedup:.2f}x faster")
    print(f"  Improvement: {((orig_result['mean'] - opt_result['mean']) / orig_result['mean'] * 100):.1f}%")
    
    # Benchmark 2: Calculate Statistics
    print("\n2. CALCULATE STATISTICS")
    print("-" * 80)
    numbers = list(range(10000))
    
    print("Original implementation:")
    orig_result = benchmark_function(original.calculate_statistics, numbers)
    print(f"  Average time: {orig_result['mean']:.4f}s")
    
    print("\nOptimized implementation:")
    opt_result = benchmark_function(optimized.calculate_statistics, numbers)
    print(f"  Average time: {opt_result['mean']:.4f}s")
    
    speedup = orig_result['mean'] / opt_result['mean']
    print(f"\n  Speedup: {speedup:.2f}x faster")
    print(f"  Improvement: {((orig_result['mean'] - opt_result['mean']) / orig_result['mean'] * 100):.1f}%")
    
    # Benchmark 3: Filter and Transform
    print("\n3. FILTER AND TRANSFORM")
    print("-" * 80)
    data = list(range(2000))
    
    print("Original implementation:")
    orig_result = benchmark_function(original.filter_and_transform, data, 1000)
    print(f"  Average time: {orig_result['mean']:.4f}s")
    
    print("\nOptimized implementation:")
    opt_result = benchmark_function(optimized.filter_and_transform, data, 1000)
    print(f"  Average time: {opt_result['mean']:.4f}s")
    
    speedup = orig_result['mean'] / opt_result['mean']
    print(f"\n  Speedup: {speedup:.2f}x faster")
    print(f"  Improvement: {((orig_result['mean'] - opt_result['mean']) / orig_result['mean'] * 100):.1f}%")
    
    # Benchmark 4: Merge Datasets
    print("\n4. MERGE DATASETS")
    print("-" * 80)
    dataset1 = list(range(1000))
    dataset2 = list(range(500, 1500))
    
    print("Original implementation:")
    orig_result = benchmark_function(original.merge_datasets, dataset1, dataset2)
    print(f"  Average time: {orig_result['mean']:.4f}s")
    
    print("\nOptimized implementation:")
    opt_result = benchmark_function(optimized.merge_datasets, dataset1, dataset2)
    print(f"  Average time: {opt_result['mean']:.4f}s")
    
    speedup = orig_result['mean'] / opt_result['mean']
    print(f"\n  Speedup: {speedup:.2f}x faster")
    print(f"  Improvement: {((orig_result['mean'] - opt_result['mean']) / orig_result['mean'] * 100):.1f}%")
    
    # Benchmark 5: Fibonacci
    print("\n5. FIBONACCI(30)")
    print("-" * 80)
    
    print("Original implementation:")
    orig_result = benchmark_function(original.compute_fibonacci, 30, iterations=1)
    print(f"  Time: {orig_result['mean']:.4f}s")
    print(f"  Result: {orig_result['result']}")
    
    print("\nOptimized implementation:")
    opt_result = benchmark_function(optimized.compute_fibonacci, 30)
    print(f"  Average time: {opt_result['mean']:.6f}s")
    print(f"  Result: {opt_result['result']}")
    
    speedup = orig_result['mean'] / opt_result['mean']
    print(f"\n  Speedup: {speedup:.2f}x faster")
    print(f"  Improvement: {((orig_result['mean'] - opt_result['mean']) / orig_result['mean'] * 100):.1f}%")
    
    # Benchmark 6: String Operations
    print("\n6. STRING OPERATIONS")
    print("-" * 80)
    words = ["word"] * 5000
    
    print("Original implementation:")
    orig_result = benchmark_function(original.string_operations, words)
    print(f"  Average time: {orig_result['mean']:.4f}s")
    
    print("\nOptimized implementation:")
    opt_result = benchmark_function(optimized.string_operations, words)
    print(f"  Average time: {opt_result['mean']:.6f}s")
    
    speedup = orig_result['mean'] / opt_result['mean']
    print(f"\n  Speedup: {speedup:.2f}x faster")
    print(f"  Improvement: {((orig_result['mean'] - opt_result['mean']) / orig_result['mean'] * 100):.1f}%")
    
    # Benchmark 7: Matrix Multiplication
    print("\n7. MATRIX MULTIPLICATION")
    print("-" * 80)
    size = 100
    matrix1 = [[i + j for j in range(size)] for i in range(size)]
    matrix2 = [[i * j for j in range(size)] for i in range(size)]
    
    print("Original implementation:")
    orig_result = benchmark_function(original.matrix_multiply, matrix1, matrix2, iterations=1)
    print(f"  Time: {orig_result['mean']:.4f}s")
    
    print("\nOptimized implementation:")
    opt_result = benchmark_function(optimized.matrix_multiply, matrix1, matrix2, iterations=1)
    print(f"  Time: {opt_result['mean']:.4f}s")
    
    speedup = orig_result['mean'] / opt_result['mean']
    print(f"\n  Speedup: {speedup:.2f}x faster")
    print(f"  Improvement: {((orig_result['mean'] - opt_result['mean']) / orig_result['mean'] * 100):.1f}%")
    
    print("\n" + "=" * 80)
    print("BENCHMARK COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    run_benchmarks()
