"""
Data processing module with various performance issues.
This module demonstrates common performance anti-patterns.
"""

import time
import json


class DataProcessor:
    """Process and analyze data with various operations."""
    
    def __init__(self):
        self.data = []
        self.cache = {}
    
    def find_duplicates(self, items):
        """Find duplicate items in a list - INEFFICIENT VERSION."""
        duplicates = []
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if items[i] == items[j] and items[i] not in duplicates:
                    duplicates.append(items[i])
        return duplicates
    
    def calculate_statistics(self, numbers):
        """Calculate basic statistics - INEFFICIENT VERSION."""
        if not numbers:
            return {}
        
        # Recalculating sum multiple times
        mean = sum(numbers) / len(numbers)
        
        # Inefficient variance calculation
        variance = sum([(x - sum(numbers) / len(numbers)) ** 2 for x in numbers]) / len(numbers)
        
        # Inefficient standard deviation
        std_dev = (sum([(x - sum(numbers) / len(numbers)) ** 2 for x in numbers]) / len(numbers)) ** 0.5
        
        return {
            'mean': mean,
            'variance': variance,
            'std_dev': std_dev
        }
    
    def filter_and_transform(self, data, threshold):
        """Filter and transform data - INEFFICIENT VERSION."""
        # Multiple passes through data
        filtered = []
        for item in data:
            if item > threshold:
                filtered.append(item)
        
        squared = []
        for item in filtered:
            squared.append(item ** 2)
        
        sorted_data = []
        for item in squared:
            inserted = False
            for i in range(len(sorted_data)):
                if item < sorted_data[i]:
                    sorted_data.insert(i, item)
                    inserted = True
                    break
            if not inserted:
                sorted_data.append(item)
        
        return sorted_data
    
    def search_records(self, records, search_key, search_value):
        """Search for records - INEFFICIENT VERSION."""
        # Linear search through all records every time
        results = []
        for record in records:
            if search_key in record and record[search_key] == search_value:
                results.append(record)
        return results
    
    def process_file_data(self, filename):
        """Process data from file - INEFFICIENT I/O VERSION."""
        # Reading file line by line without buffering
        results = []
        with open(filename, 'r') as f:
            for line in f:
                # Processing each line separately
                data = json.loads(line.strip())
                # No caching of expensive computations
                processed = self._expensive_computation(data)
                results.append(processed)
        return results
    
    def _expensive_computation(self, data):
        """Simulate expensive computation without caching."""
        # Simulating expensive operation
        result = 0
        for i in range(1000):
            result += sum([j ** 2 for j in range(100)])
        return {**data, 'computed': result}
    
    def merge_datasets(self, dataset1, dataset2):
        """Merge two datasets - INEFFICIENT VERSION."""
        # Using list concatenation in a loop
        merged = []
        for item in dataset1:
            merged = merged + [item]  # Creates new list each time
        for item in dataset2:
            merged = merged + [item]  # Creates new list each time
        
        # Remove duplicates inefficiently
        unique = []
        for item in merged:
            if item not in unique:  # O(n) lookup each time
                unique.append(item)
        
        return unique
    
    def compute_fibonacci(self, n):
        """Compute fibonacci number - INEFFICIENT RECURSIVE VERSION."""
        if n <= 1:
            return n
        return self.compute_fibonacci(n - 1) + self.compute_fibonacci(n - 2)
    
    def string_operations(self, words):
        """Perform string operations - INEFFICIENT VERSION."""
        # Inefficient string concatenation
        result = ""
        for word in words:
            result = result + word + " "  # Creates new string each time
        
        return result.strip()
    
    def matrix_multiply(self, matrix1, matrix2):
        """Multiply two matrices - UNOPTIMIZED VERSION."""
        if not matrix1 or not matrix2 or not matrix1[0] or not matrix2[0]:
            raise ValueError("Matrices cannot be empty")
        
        # Basic nested loop implementation without any optimization
        rows1 = len(matrix1)
        cols1 = len(matrix1[0])
        rows2 = len(matrix2)
        cols2 = len(matrix2[0])
        
        if cols1 != rows2:
            raise ValueError("Matrix dimensions incompatible")
        
        result = []
        for i in range(rows1):
            row = []
            for j in range(cols2):
                value = 0
                for k in range(cols1):
                    value += matrix1[i][k] * matrix2[k][j]
                row.append(value)
            result.append(row)
        
        return result


def demo_performance_issues():
    """Demonstrate the performance issues."""
    processor = DataProcessor()
    
    print("Running performance demonstrations...")
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
    demo_performance_issues()
