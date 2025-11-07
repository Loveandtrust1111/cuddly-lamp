# Performance Optimization Guide

This guide provides best practices and common patterns for writing efficient code. The examples in the `/examples` directory demonstrate these principles in practice.

## Table of Contents

1. [Data Structures](#data-structures)
2. [Algorithm Complexity](#algorithm-complexity)
3. [String Operations](#string-operations)
4. [Loop Optimization](#loop-optimization)
5. [Memory Management](#memory-management)
6. [Language-Specific Tips](#language-specific-tips)

## Data Structures

### Choose the Right Data Structure

The choice of data structure significantly impacts performance:

#### Python
- **List**: Use for ordered sequences with index-based access
  - O(1) for append, index access
  - O(n) for search, insert, delete
  
- **Set**: Use for unique items and membership testing
  - O(1) for add, remove, membership testing
  - Cannot maintain order (use in Python 3.7+)
  
- **Dict**: Use for key-value mappings
  - O(1) for get, set, delete operations
  
- **deque**: Use for queue operations (from collections)
  - O(1) for append/pop from both ends

#### JavaScript
- **Array**: Ordered sequences
  - O(1) for push, pop, index access
  - O(n) for shift, unshift, indexOf
  
- **Set**: Unique values with fast lookups
  - O(1) for add, delete, has
  
- **Map**: Key-value pairs with any type as key
  - O(1) for get, set, delete
  - Maintains insertion order
  
- **WeakMap/WeakSet**: For garbage collection-friendly caching

### Example: Membership Testing

❌ **Inefficient** (Python):
```python
items = [1, 2, 3, 4, 5]
if 3 in items:  # O(n) search
    print("Found")
```

✅ **Efficient**:
```python
items = {1, 2, 3, 4, 5}  # Use set
if 3 in items:  # O(1) search
    print("Found")
```

## Algorithm Complexity

### Big O Notation Quick Reference

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | Hash table lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Array iteration |
| O(n log n) | Linearithmic | Efficient sorting |
| O(n²) | Quadratic | Nested loops |
| O(2ⁿ) | Exponential | Recursive Fibonacci |

### Avoid Nested Loops When Possible

❌ **Inefficient** - O(n²):
```python
def find_matches(list1, list2):
    matches = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                matches.append(item1)
    return matches
```

✅ **Efficient** - O(n + m):
```python
def find_matches(list1, list2):
    return list(set(list1) & set(list2))
```

## String Operations

### String Concatenation

Strings are immutable in most languages. Repeated concatenation creates new objects.

#### Python

❌ **Inefficient** - O(n²):
```python
result = ""
for item in items:
    result += str(item) + ","
```

✅ **Efficient** - O(n):
```python
result = ",".join(str(item) for item in items)
```

#### JavaScript

❌ **Inefficient**:
```javascript
let result = '';
for (let item of items) {
    result += item + ',';
}
```

✅ **Efficient**:
```javascript
const result = items.join(',');
```

## Loop Optimization

### 1. Minimize Work Inside Loops

❌ **Inefficient**:
```python
for i in range(len(data)):
    if expensive_function():  # Called every iteration
        process(data[i])
```

✅ **Efficient**:
```python
should_process = expensive_function()  # Called once
for item in data:
    if should_process:
        process(item)
```

### 2. Use List Comprehensions (Python)

List comprehensions are optimized in CPython and more readable.

❌ **Inefficient**:
```python
result = []
for item in data:
    if item > 0:
        result.append(item ** 2)
```

✅ **Efficient**:
```python
result = [item ** 2 for item in data if item > 0]
```

### 3. Combine Multiple Passes

❌ **Inefficient** - Multiple passes:
```python
filtered = [x for x in data if x > 0]
squared = [x ** 2 for x in filtered]
total = sum(squared)
```

✅ **Efficient** - Single pass:
```python
total = sum(x ** 2 for x in data if x > 0)
```

### 4. Cache Array Length (JavaScript)

❌ **Inefficient**:
```javascript
for (let i = 0; i < arr.length; i++) {
    // arr.length evaluated each iteration
}
```

✅ **Efficient**:
```javascript
const len = arr.length;
for (let i = 0; i < len; i++) {
    // Length cached
}
```

## Memory Management

### 1. Use Generators for Large Data (Python)

Generators compute values on-demand, saving memory.

❌ **Inefficient** - Loads all into memory:
```python
def read_large_file(filename):
    with open(filename) as f:
        return [line.strip() for line in f]
```

✅ **Efficient** - Yields one at a time:
```python
def read_large_file(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()
```

### 2. Avoid Creating Unnecessary Objects

❌ **Inefficient**:
```javascript
for (let i = 0; i < 1000; i++) {
    const obj = { timestamp: new Date() };  // New Date each iteration
    process(obj);
}
```

✅ **Efficient**:
```javascript
const timestamp = new Date();  // Create once
for (let i = 0; i < 1000; i++) {
    const obj = { timestamp };
    process(obj);
}
```

### 3. Pre-allocate Arrays When Size is Known

✅ **Efficient** (JavaScript):
```javascript
const results = new Array(count);  // Pre-allocate
for (let i = 0; i < count; i++) {
    results[i] = process(i);
}
```

## Language-Specific Tips

### Python

1. **Use Built-in Functions**: Built-ins are implemented in C and are faster
   ```python
   # Fast: sum(numbers)
   # Slow: reduce(lambda x, y: x + y, numbers)
   ```

2. **Use `collections` Module**:
   - `Counter` for counting
   - `defaultdict` for dictionaries with default values
   - `deque` for queue operations

3. **Avoid Global Variables**: Local variable lookups are faster

4. **Use `__slots__` for Classes with Many Instances**:
   ```python
   class Point:
       __slots__ = ['x', 'y']  # Reduces memory usage
   ```

### JavaScript

1. **Batch DOM Operations**:
   ```javascript
   // Use DocumentFragment
   const fragment = document.createDocumentFragment();
   // ... add elements to fragment
   container.appendChild(fragment);
   ```

2. **Use `const` and `let`**: Helps JS engine optimize

3. **Avoid `delete` on Arrays**: Creates sparse arrays
   ```javascript
   // Use: arr.splice(index, 1)
   // Or: arr.filter((_, i) => i !== index)
   ```

4. **Use Modern Array Methods**:
   - `map`, `filter`, `reduce` are optimized and readable
   - Consider `for...of` for simple iterations

5. **Debounce Expensive Operations**:
   ```javascript
   const debouncedSearch = debounce(search, 300);
   ```

## Performance Measurement

Always measure before optimizing!

### Python
```python
import time
import timeit

# Quick timing
start = time.time()
result = function()
print(f"Time: {time.time() - start:.4f}s")

# More accurate timing
timeit.timeit('function()', number=1000)
```

### JavaScript
```javascript
// Console timing
console.time('operation');
operation();
console.timeEnd('operation');

// Performance API
const start = performance.now();
operation();
const end = performance.now();
console.log(`Time: ${end - start}ms`);
```

## Common Anti-Patterns to Avoid

1. **Premature Optimization**: Optimize after profiling
2. **Ignoring Complexity**: O(n²) algorithms on large datasets
3. **Memory Leaks**: Forgetting to clean up event listeners, closures
4. **Synchronous Operations**: Blocking the main thread
5. **Not Caching**: Recalculating expensive operations
6. **Wrong Data Structure**: Using lists for frequent lookups

## Best Practices Summary

✅ **Do:**
- Profile before optimizing
- Use appropriate data structures
- Minimize operations in loops
- Use language-specific optimizations
- Cache expensive computations
- Use generators/streams for large data

❌ **Don't:**
- Optimize prematurely
- Use global variables unnecessarily
- Create objects in hot loops
- Ignore algorithm complexity
- Block the main thread
- Forget to measure performance

## Additional Resources

- [Python Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
- [JavaScript Performance Best Practices](https://developer.mozilla.org/en-US/docs/Web/Performance)
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/)

## See Also

- `/examples/inefficient_example.py` - Python anti-patterns
- `/examples/efficient_example.py` - Python best practices
- `/examples/inefficient_example.js` - JavaScript anti-patterns
- `/examples/efficient_example.js` - JavaScript best practices
