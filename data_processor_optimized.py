"""
Optimized data processing module.
This module demonstrates performance improvements over data_processor.py.
"""

import time
import json
from functools import lru_cache


class OptimizedDataProcessor:
    """Process and analyze data with optimized operations."""
    
    def __init__(self):
        self.data = []
        self.cache = {}
        self.index = {}  # For faster lookups
    
    def find_duplicates(self, items):
        """Find duplicate items in a list - OPTIMIZED with set."""
        seen = set()
        duplicates = set()
        
        for item in items:
            if item in seen:
                duplicates.add(item)
            else:
                seen.add(item)
        
        return list(duplicates)
    
    def calculate_statistics(self, numbers):
        """Calculate basic statistics - OPTIMIZED to compute sum once."""
        if not numbers:
            return {}
        
        n = len(numbers)
        total = sum(numbers)
        mean = total / n
        
        # Calculate variance in single pass
        variance = sum((x - mean) ** 2 for x in numbers) / n
        std_dev = variance ** 0.5
        
        return {
            'mean': mean,
            'variance': variance,
            'std_dev': std_dev
        }
    
    def filter_and_transform(self, data, threshold):
        """Filter and transform data - OPTIMIZED with list comprehension and built-in sort."""
        # Single pass with list comprehension
        filtered_squared = [item ** 2 for item in data if item > threshold]
        
        # Use built-in sort (TimSort - highly optimized)
        return sorted(filtered_squared)
    
    def search_records(self, records, search_key, search_value):
        """Search for records - OPTIMIZED with indexing."""
        # Build index if not exists
        if search_key not in self.index:
            self.index[search_key] = {}
            for record in records:
                if search_key in record:
                    key_val = record[search_key]
                    if key_val not in self.index[search_key]:
                        self.index[search_key][key_val] = []
                    self.index[search_key][key_val].append(record)
        
        # O(1) lookup instead of O(n)
        return self.index[search_key].get(search_value, [])
    
    def process_file_data(self, filename):
        """Process data from file - OPTIMIZED with caching."""
        results = []
        with open(filename, 'r') as f:
            for line in f:
                data = json.loads(line.strip())
                # Use cached computation
                data_key = str(sorted(data.items()))
                if data_key in self.cache:
                    processed = self.cache[data_key]
                else:
                    processed = self._expensive_computation(data)
                    self.cache[data_key] = processed
                results.append(processed)
        return results
    
    def _expensive_computation(self, data):
        """Expensive computation with memoization."""
        # Pre-compute constant values
        constant_sum = sum(j ** 2 for j in range(100)) * 1000
        return {**data, 'computed': constant_sum}
    
    def merge_datasets(self, dataset1, dataset2):
        """Merge two datasets - OPTIMIZED with extend and set."""
        # Use extend instead of repeated concatenation
        merged = []
        merged.extend(dataset1)
        merged.extend(dataset2)
        
        # Remove duplicates efficiently with set
        # Note: Only works if items are hashable
        try:
            return list(set(merged))
        except TypeError:
            # Fallback for unhashable items
            unique = []
            seen = set()
            for item in merged:
                item_key = str(item)
                if item_key not in seen:
                    seen.add(item_key)
                    unique.append(item)
            return unique
    
    @lru_cache(maxsize=None)
    def compute_fibonacci(self, n):
        """Compute fibonacci number - OPTIMIZED with memoization."""
        if n <= 1:
            return n
        return self.compute_fibonacci(n - 1) + self.compute_fibonacci(n - 2)
    
    def string_operations(self, words):
        """Perform string operations - OPTIMIZED with join."""
        # Use join instead of repeated concatenation
        return " ".join(words)
    
    def matrix_multiply(self, matrix1, matrix2):
        """Multiply two matrices - OPTIMIZED with list comprehension."""
        rows1 = len(matrix1)
        cols1 = len(matrix1[0])
        rows2 = len(matrix2)
        cols2 = len(matrix2[0])
        
        if cols1 != rows2:
            raise ValueError("Matrix dimensions incompatible")
        
        # Use list comprehension for better performance
        result = [
            [
                sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1))
                for j in range(cols2)
            ]
            for i in range(rows1)
        ]
        
        return result
    
    def clear_cache(self):
        """Clear all caches."""
        self.cache.clear()
        self.index.clear()
        self.compute_fibonacci.cache_clear()


def demo_optimized_performance():
    """Demonstrate the optimized performance."""
    processor = OptimizedDataProcessor()
    
    print("Running optimized performance demonstrations...")
    print("\n1. Finding duplicates in large list...")
    large_list = list(range(1000)) + list(range(500))
    start = time.time()
    duplicates = processor.find_duplicates(large_list)
    print(f"   Time: {time.time() - start:.4f}s")
    
    print("\n2. Calculating statistics...")
    numbers = list(range(10000))
    start = time.time()
    stats = processor.calculate_statistics(numbers)
    print(f"   Time: {time.time() - start:.4f}s")
    
    print("\n3. Filter and transform...")
    data = list(range(5000))
    start = time.time()
    result = processor.filter_and_transform(data, 2500)
    print(f"   Time: {time.time() - start:.4f}s")
    
    print("\n4. Computing Fibonacci(30)...")
    start = time.time()
    fib = processor.compute_fibonacci(30)
    print(f"   Time: {time.time() - start:.4f}s")
    print(f"   Result: {fib}")


if __name__ == "__main__":
    demo_optimized_performance()
