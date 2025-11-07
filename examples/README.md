# Performance Examples

This directory contains side-by-side comparisons of inefficient and efficient code patterns in both Python and JavaScript.

## Files

### Python Examples

- **`inefficient_example.py`** - Demonstrates common performance anti-patterns
  - String concatenation in loops
  - Using lists for membership testing
  - Nested loops without optimization
  - Multiple iterations over the same data
  - Inappropriate data structures
  - Global variable usage

- **`efficient_example.py`** - Shows optimized versions of the same patterns
  - Using `str.join()` for string building
  - Using sets for O(1) lookups
  - Set operations for finding common elements
  - Single-pass data processing with generators
  - Using `Counter` from collections
  - Proper data structure selection

### JavaScript Examples

- **`inefficient_example.js`** - Common JavaScript performance pitfalls
  - Multiple DOM manipulations
  - Not caching array length
  - Creating functions in loops
  - Array deletion with `delete` operator
  - Multiple array iterations
  - String concatenation in loops
  - Using `indexOf` for membership testing

- **`efficient_example.js`** - Optimized JavaScript patterns
  - Batch DOM updates with DocumentFragment
  - Modern array methods (map, filter, reduce)
  - Using Set and Map for efficient lookups
  - Proper async/await usage
  - Memory-efficient object creation
  - Debouncing and caching patterns

## Running the Examples

### Python

Run individual files:
```bash
python3 inefficient_example.py
python3 efficient_example.py
```

Run the benchmark to compare performance:
```bash
cd ..
python3 benchmark.py
```

### JavaScript

The JavaScript examples can be used in Node.js or browser environments:

```bash
node efficient_example.js
```

Or include them in an HTML file:
```html
<script src="examples/efficient_example.js"></script>
```

## Key Performance Improvements

Based on our benchmarks, the optimized code shows:

- **10-50x faster** string concatenation using join()
- **30-250x faster** membership testing using sets
- **2-5x faster** data processing with single-pass algorithms
- **Significant memory reduction** with generators and proper data structures

## Learning Path

1. **Start with** `PERFORMANCE.md` in the root directory for comprehensive theory
2. **Study** the inefficient examples to recognize anti-patterns
3. **Compare** with efficient versions to see the solutions
4. **Run** `benchmark.py` to see actual performance differences
5. **Apply** these patterns to your own code

## Additional Resources

- [Python Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
- [JavaScript Performance MDN](https://developer.mozilla.org/en-US/docs/Web/Performance)
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
