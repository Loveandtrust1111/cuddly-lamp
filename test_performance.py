"""
Test suite to verify correctness of both original and optimized implementations.
"""

import pytest
from data_processor import DataProcessor
from data_processor_optimized import OptimizedDataProcessor


class TestFindDuplicates:
    """Test duplicate finding functionality."""
    
    def test_simple_duplicates(self):
        """Test finding duplicates in simple list."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        data = [1, 2, 3, 2, 4, 3, 5]
        
        orig_result = set(original.find_duplicates(data))
        opt_result = set(optimized.find_duplicates(data))
        
        assert orig_result == opt_result == {2, 3}
    
    def test_no_duplicates(self):
        """Test list with no duplicates."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        data = [1, 2, 3, 4, 5]
        
        orig_result = original.find_duplicates(data)
        opt_result = optimized.find_duplicates(data)
        
        assert len(orig_result) == len(opt_result) == 0
    
    def test_all_duplicates(self):
        """Test list where all elements are duplicates."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        data = [1, 1, 1, 1, 1]
        
        orig_result = set(original.find_duplicates(data))
        opt_result = set(optimized.find_duplicates(data))
        
        assert orig_result == opt_result == {1}


class TestCalculateStatistics:
    """Test statistics calculation."""
    
    def test_simple_stats(self):
        """Test basic statistics calculation."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        data = [1, 2, 3, 4, 5]
        
        orig_result = original.calculate_statistics(data)
        opt_result = optimized.calculate_statistics(data)
        
        assert abs(orig_result['mean'] - opt_result['mean']) < 0.0001
        assert abs(orig_result['variance'] - opt_result['variance']) < 0.0001
        assert abs(orig_result['std_dev'] - opt_result['std_dev']) < 0.0001
    
    def test_empty_list(self):
        """Test with empty list."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        data = []
        
        orig_result = original.calculate_statistics(data)
        opt_result = optimized.calculate_statistics(data)
        
        assert orig_result == opt_result == {}
    
    def test_large_numbers(self):
        """Test with large numbers."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        data = list(range(1000))
        
        orig_result = original.calculate_statistics(data)
        opt_result = optimized.calculate_statistics(data)
        
        assert abs(orig_result['mean'] - opt_result['mean']) < 0.0001
        assert abs(orig_result['variance'] - opt_result['variance']) < 0.01
        assert abs(orig_result['std_dev'] - opt_result['std_dev']) < 0.01


class TestFilterAndTransform:
    """Test filter and transform functionality."""
    
    def test_basic_filter_transform(self):
        """Test basic filtering and transformation."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        threshold = 5
        
        orig_result = original.filter_and_transform(data, threshold)
        opt_result = optimized.filter_and_transform(data, threshold)
        
        assert orig_result == opt_result
    
    def test_no_items_pass_threshold(self):
        """Test when no items pass threshold."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        data = [1, 2, 3, 4, 5]
        threshold = 10
        
        orig_result = original.filter_and_transform(data, threshold)
        opt_result = optimized.filter_and_transform(data, threshold)
        
        assert orig_result == opt_result == []
    
    def test_all_items_pass_threshold(self):
        """Test when all items pass threshold."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        data = [10, 20, 30, 40, 50]
        threshold = 5
        
        orig_result = original.filter_and_transform(data, threshold)
        opt_result = optimized.filter_and_transform(data, threshold)
        
        assert orig_result == opt_result


class TestMergeDatasets:
    """Test dataset merging."""
    
    def test_basic_merge(self):
        """Test basic dataset merge."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        dataset1 = [1, 2, 3]
        dataset2 = [3, 4, 5]
        
        orig_result = set(original.merge_datasets(dataset1, dataset2))
        opt_result = set(optimized.merge_datasets(dataset1, dataset2))
        
        assert orig_result == opt_result == {1, 2, 3, 4, 5}
    
    def test_no_overlap(self):
        """Test merge with no overlapping items."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        dataset1 = [1, 2, 3]
        dataset2 = [4, 5, 6]
        
        orig_result = set(original.merge_datasets(dataset1, dataset2))
        opt_result = set(optimized.merge_datasets(dataset1, dataset2))
        
        assert orig_result == opt_result == {1, 2, 3, 4, 5, 6}
    
    def test_complete_overlap(self):
        """Test merge with complete overlap."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        dataset1 = [1, 2, 3]
        dataset2 = [1, 2, 3]
        
        orig_result = set(original.merge_datasets(dataset1, dataset2))
        opt_result = set(optimized.merge_datasets(dataset1, dataset2))
        
        assert orig_result == opt_result == {1, 2, 3}


class TestFibonacci:
    """Test Fibonacci computation."""
    
    def test_fibonacci_base_cases(self):
        """Test Fibonacci base cases."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        assert original.compute_fibonacci(0) == optimized.compute_fibonacci(0) == 0
        assert original.compute_fibonacci(1) == optimized.compute_fibonacci(1) == 1
    
    def test_fibonacci_small_values(self):
        """Test Fibonacci for small values."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        # Only test up to 10 for original implementation to avoid exponential slowdown
        for n in range(2, 10):
            orig_result = original.compute_fibonacci(n)
            opt_result = optimized.compute_fibonacci(n)
            assert orig_result == opt_result, f"Mismatch at n={n}"
    
    def test_fibonacci_known_values(self):
        """Test Fibonacci against known values."""
        optimized = OptimizedDataProcessor()
        
        known_values = {
            0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5,
            6: 8, 7: 13, 8: 21, 9: 34, 10: 55
        }
        
        for n, expected in known_values.items():
            assert optimized.compute_fibonacci(n) == expected


class TestStringOperations:
    """Test string operations."""
    
    def test_basic_string_join(self):
        """Test basic string joining."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        words = ["hello", "world", "test"]
        
        orig_result = original.string_operations(words)
        opt_result = optimized.string_operations(words)
        
        assert orig_result == opt_result == "hello world test"
    
    def test_single_word(self):
        """Test with single word."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        words = ["hello"]
        
        orig_result = original.string_operations(words)
        opt_result = optimized.string_operations(words)
        
        assert orig_result == opt_result == "hello"
    
    def test_empty_list(self):
        """Test with empty list."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        words = []
        
        orig_result = original.string_operations(words)
        opt_result = optimized.string_operations(words)
        
        assert orig_result == opt_result == ""


class TestMatrixMultiply:
    """Test matrix multiplication."""
    
    def test_basic_multiplication(self):
        """Test basic matrix multiplication."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        
        orig_result = original.matrix_multiply(matrix1, matrix2)
        opt_result = optimized.matrix_multiply(matrix1, matrix2)
        
        assert orig_result == opt_result == [[19, 22], [43, 50]]
    
    def test_identity_matrix(self):
        """Test multiplication with identity matrix."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        matrix = [[1, 2], [3, 4]]
        identity = [[1, 0], [0, 1]]
        
        orig_result = original.matrix_multiply(matrix, identity)
        opt_result = optimized.matrix_multiply(matrix, identity)
        
        assert orig_result == opt_result == matrix
    
    def test_incompatible_dimensions(self):
        """Test with incompatible matrix dimensions."""
        original = DataProcessor()
        optimized = OptimizedDataProcessor()
        
        matrix1 = [[1, 2, 3]]  # 1x3
        matrix2 = [[1, 2], [3, 4]]  # 2x2
        
        with pytest.raises(ValueError):
            original.matrix_multiply(matrix1, matrix2)
        
        with pytest.raises(ValueError):
            optimized.matrix_multiply(matrix1, matrix2)


class TestSearchRecords:
    """Test record searching."""
    
    def test_basic_search(self):
        """Test basic record search."""
        optimized = OptimizedDataProcessor()
        
        records = [
            {'id': 1, 'name': 'Alice'},
            {'id': 2, 'name': 'Bob'},
            {'id': 3, 'name': 'Alice'}
        ]
        
        result = optimized.search_records(records, 'name', 'Alice')
        assert len(result) == 2
        assert all(r['name'] == 'Alice' for r in result)
    
    def test_no_matches(self):
        """Test search with no matches."""
        optimized = OptimizedDataProcessor()
        
        records = [
            {'id': 1, 'name': 'Alice'},
            {'id': 2, 'name': 'Bob'}
        ]
        
        result = optimized.search_records(records, 'name', 'Charlie')
        assert result == []
    
    def test_repeated_searches(self):
        """Test that indexing works for repeated searches."""
        optimized = OptimizedDataProcessor()
        
        records = [
            {'id': 1, 'category': 'A'},
            {'id': 2, 'category': 'B'},
            {'id': 3, 'category': 'A'}
        ]
        
        # First search builds index
        result1 = optimized.search_records(records, 'category', 'A')
        # Second search uses index
        result2 = optimized.search_records(records, 'category', 'A')
        
        assert len(result1) == len(result2) == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
