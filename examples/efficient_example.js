/**
 * Optimized JavaScript code examples.
 * These patterns demonstrate best practices for performance.
 */

/**
 * EFFICIENT: Batch DOM modifications using DocumentFragment
 */
function efficientDOMManipulation(items) {
    const container = document.getElementById('container');
    const fragment = document.createDocumentFragment();
    
    for (let i = 0; i < items.length; i++) {
        const div = document.createElement('div');
        div.textContent = items[i];
        fragment.appendChild(div);
    }
    
    container.appendChild(fragment);  // Single DOM modification
}

/**
 * EFFICIENT: Cache array length and use modern iteration
 */
function efficientArrayIteration(arr) {
    let sum = 0;
    const len = arr.length;  // Cache length
    for (let i = 0; i < len; i++) {
        sum += arr[i];
    }
    return sum;
}

/**
 * EFFICIENT: Alternative using reduce (more idiomatic)
 */
function efficientArrayIterationReduce(arr) {
    return arr.reduce((sum, val) => sum + val, 0);
}

/**
 * EFFICIENT: Create function outside loop or use arrow functions properly
 */
function efficientFunctionCreation(items) {
    return items.map((item, i) => () => console.log(item));
}

/**
 * EFFICIENT: Use splice or filter instead of delete
 */
function efficientArrayDeletion(arr, index) {
    return arr.filter((_, i) => i !== index);
}

/**
 * EFFICIENT: Single pass using reduce
 */
function efficientSingleIteration(data) {
    return data.reduce((sum, x) => x > 0 ? sum + x * x : sum, 0);
}

/**
 * EFFICIENT: Use array join for string building
 */
function efficientStringConcat(items) {
    return items.join(',');
}

/**
 * EFFICIENT: Use Set for O(1) membership testing
 */
function efficientMembershipTest(arr, searchItems) {
    const arrSet = new Set(arr);
    return searchItems.filter(item => arrSet.has(item));
}

/**
 * EFFICIENT: Use Set intersection for finding matches
 */
function efficientNestedLoops(arr1, arr2) {
    const set1 = new Set(arr1);
    return arr2.filter(item => set1.has(item));
}

/**
 * EFFICIENT: Use const/let with proper scoping
 */
function efficientVariableScope() {
    let counter = 0;  // Local variable
    for (let i = 0; i < 100; i++) {  // Block-scoped
        counter += i;
    }
    return counter;
}

/**
 * EFFICIENT: Use async/await for non-blocking operations
 */
async function efficientAsyncOperation(data) {
    // Simulate async operation
    return new Promise(resolve => {
        setTimeout(() => resolve(data), 1000);
    });
}

/**
 * EFFICIENT: Reuse objects/optimize allocations
 */
function efficientObjectCreation(count) {
    const results = new Array(count);  // Pre-allocate array
    const timestamp = new Date();  // Reuse timestamp
    
    for (let i = 0; i < count; i++) {
        results[i] = {
            id: i,
            timestamp: timestamp,
            data: []
        };
    }
    return results;
}

/**
 * EFFICIENT: Avoid try-catch in hot loops
 */
function efficientErrorHandling(arr) {
    // Validate input before processing
    if (!Array.isArray(arr)) {
        throw new Error('Input must be an array');
    }
    
    // Process without try-catch in loop
    return arr.map(x => x * 2);
}

/**
 * EFFICIENT: Use Map for key-value pairs with frequent lookups
 */
function efficientDataStructure(items) {
    const map = new Map();
    for (const item of items) {
        map.set(item.id, item);
    }
    return map;
}

/**
 * EFFICIENT: Debounce expensive operations
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function computeExpensiveValue(obj) {
    /**
     * Simulated expensive operation that takes significant time.
     * In reality, this could be parsing, validation, transformation, etc.
     */
    let result = 0;
    const keys = Object.keys(obj);
    // Simulate some expensive computation
    for (let i = 0; i < keys.length * 1000; i++) {
        result += keys.length;
    }
    return result;
}

/**
 * EFFICIENT: Use WeakMap for memory-efficient caching
 */
const cache = new WeakMap();
function efficientCaching(obj) {
    if (cache.has(obj)) {
        return cache.get(obj);
    }
    const result = computeExpensiveValue(obj);
    cache.set(obj, result);
    return result;
}

/**
 * EFFICIENT: Use Object.freeze for immutable constants
 */
const CONFIG = Object.freeze({
    API_URL: 'https://api.example.com',
    TIMEOUT: 5000,
    MAX_RETRIES: 3
});

/**
 * EFFICIENT: Use for...of for iterating arrays (more readable)
 */
function efficientModernIteration(arr) {
    let sum = 0;
    for (const value of arr) {
        sum += value;
    }
    return sum;
}

// Example usage and benchmarking
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        efficientDOMManipulation,
        efficientArrayIteration,
        efficientArrayIterationReduce,
        efficientFunctionCreation,
        efficientArrayDeletion,
        efficientSingleIteration,
        efficientStringConcat,
        efficientMembershipTest,
        efficientNestedLoops,
        efficientVariableScope,
        efficientAsyncOperation,
        efficientObjectCreation,
        efficientErrorHandling,
        efficientDataStructure,
        debounce,
        efficientCaching,
        efficientModernIteration
    };
}
