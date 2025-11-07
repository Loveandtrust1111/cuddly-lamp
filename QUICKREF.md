# Quick Reference: Performance Optimizations

## Before & After Code Examples

### 1. Find Duplicates (366x faster)

```python
# ❌ SLOW - O(n²) nested loops
def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates

# ✅ FAST - O(n) with sets
def find_duplicates(items):
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)
```

---

### 2. Statistics (1,480x faster)

```python
# ❌ SLOW - Redundant calculations
def calculate_statistics(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum([(x - sum(numbers) / len(numbers)) ** 2 for x in numbers]) / len(numbers)
    std_dev = (sum([(x - sum(numbers) / len(numbers)) ** 2 for x in numbers]) / len(numbers)) ** 0.5
    return {'mean': mean, 'variance': variance, 'std_dev': std_dev}

# ✅ FAST - Compute once, reuse
def calculate_statistics(numbers):
    n = len(numbers)
    total = sum(numbers)
    mean = total / n
    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_dev = variance ** 0.5
    return {'mean': mean, 'variance': variance, 'std_dev': std_dev}
```

---

### 3. Filter & Transform (144x faster)

```python
# ❌ SLOW - Multiple passes + O(n²) sort
def filter_and_transform(data, threshold):
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

# ✅ FAST - Single pass + efficient sort
def filter_and_transform(data, threshold):
    filtered_squared = [item ** 2 for item in data if item > threshold]
    return sorted(filtered_squared)
```

---

### 4. Merge Datasets (116x faster)

```python
# ❌ SLOW - Creates new list each time
def merge_datasets(dataset1, dataset2):
    merged = []
    for item in dataset1:
        merged = merged + [item]  # O(n) copy each time!
    for item in dataset2:
        merged = merged + [item]
    
    unique = []
    for item in merged:
        if item not in unique:  # O(n) lookup
            unique.append(item)
    return unique

# ✅ FAST - extend() and set
def merge_datasets(dataset1, dataset2):
    merged = []
    merged.extend(dataset1)
    merged.extend(dataset2)
    return list(set(merged))  # O(n) deduplication
```

---

### 5. Fibonacci (2,765x faster)

```python
# ❌ SLOW - O(2^n) exponential recursion
def compute_fibonacci(n):
    if n <= 1:
        return n
    return compute_fibonacci(n - 1) + compute_fibonacci(n - 2)

# ✅ FAST - O(n) with memoization
@staticmethod
@lru_cache(maxsize=None)
def compute_fibonacci_cached(n):
    if n <= 1:
        return n
    return compute_fibonacci_cached(n - 1) + compute_fibonacci_cached(n - 2)
```

---

### 6. String Operations (60x faster)

```python
# ❌ SLOW - String concatenation in loop
def string_operations(words):
    result = ""
    for word in words:
        result = result + word + " "  # Creates new string!
    return result.strip()

# ✅ FAST - join()
def string_operations(words):
    return " ".join(words)
```

---

### 7. Search Records (O(n) → O(1))

```python
# ❌ SLOW - Linear search every time
def search_records(records, search_key, search_value):
    results = []
    for record in records:
        if search_key in record and record[search_key] == search_value:
            results.append(record)
    return results

# ✅ FAST - Build index for O(1) lookup
def search_records(records, search_key, search_value):
    if search_key not in self.index:
        self.index[search_key] = {}
        for record in records:
            if search_key in record:
                key_val = record[search_key]
                if key_val not in self.index[search_key]:
                    self.index[search_key][key_val] = []
                self.index[search_key][key_val].append(record)
    return self.index[search_key].get(search_value, [])
```

---

## Quick Tips

1. **Use sets for membership testing** - O(1) vs O(n)
2. **Cache expensive calculations** - Don't recalculate the same value
3. **Use list comprehensions** - More efficient than manual loops
4. **Prefer built-in functions** - `sorted()`, `join()`, `extend()` are optimized
5. **Choose the right algorithm** - O(n) vs O(n²) makes a huge difference
6. **Use memoization for recursion** - `@lru_cache` can give exponential speedups
7. **Build indexes for repeated lookups** - O(n) build + O(1) lookup

## Running Comparisons

```bash
# Run benchmarks to see speedups
python benchmark.py

# Run tests to verify correctness
python -m pytest test_performance.py -v
```

## Learn More

See [PERFORMANCE.md](PERFORMANCE.md) for detailed explanations and [SUMMARY.md](SUMMARY.md) for the executive summary.
