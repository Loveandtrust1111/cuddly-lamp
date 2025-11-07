/**
 * Example of inefficient JavaScript code patterns.
 * These patterns should be avoided for better performance.
 */

/**
 * INEFFICIENT: Modifying DOM in a loop
 * Causes multiple reflows and repaints
 */
function inefficientDOMManipulation(items) {
    const container = document.getElementById('container');
    for (let i = 0; i < items.length; i++) {
        const div = document.createElement('div');
        div.textContent = items[i];
        container.appendChild(div);  // Multiple DOM modifications
    }
}

/**
 * INEFFICIENT: Not caching array length in loop
 */
function inefficientArrayIteration(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {  // arr.length evaluated each iteration
        sum += arr[i];
    }
    return sum;
}

/**
 * INEFFICIENT: Creating functions inside loops
 */
function inefficientFunctionCreation(items) {
    const handlers = [];
    for (let i = 0; i < items.length; i++) {
        handlers.push(function() {  // New function object created each iteration
            console.log(items[i]);
        });
    }
    return handlers;
}

/**
 * INEFFICIENT: Using delete operator on array elements
 * Creates holes in array and prevents optimization
 */
function inefficientArrayDeletion(arr, index) {
    delete arr[index];  // Creates sparse array
    return arr;
}

/**
 * INEFFICIENT: Multiple array iterations
 */
function inefficientMultipleIterations(data) {
    const filtered = data.filter(x => x > 0);
    const squared = filtered.map(x => x * x);
    const sum = squared.reduce((a, b) => a + b, 0);
    return sum;
}

/**
 * INEFFICIENT: String concatenation in loop
 */
function inefficientStringConcat(items) {
    let result = '';
    for (let i = 0; i < items.length; i++) {
        result += items[i] + ',';  // Creates new string each time
    }
    return result;
}

/**
 * INEFFICIENT: Using Array.indexOf for membership testing
 */
function inefficientMembershipTest(arr, searchItems) {
    const found = [];
    for (let item of searchItems) {
        if (arr.indexOf(item) !== -1) {  // O(n) search for each item
            found.push(item);
        }
    }
    return found;
}

/**
 * INEFFICIENT: Nested loops without optimization
 */
function inefficientNestedLoops(arr1, arr2) {
    const matches = [];
    for (let i = 0; i < arr1.length; i++) {
        for (let j = 0; j < arr2.length; j++) {
            if (arr1[i] === arr2[j]) {
                matches.push(arr1[i]);
            }
        }
    }
    return matches;
}

/**
 * INEFFICIENT: Not using const/let properly
 */
var globalVar = 0;  // Global variable
function inefficientVariableScope() {
    for (var i = 0; i < 100; i++) {  // var leaks to function scope
        globalVar += i;
    }
    return globalVar;
}

/**
 * INEFFICIENT: Synchronous operations that could be async
 */
function inefficientSyncOperation(data) {
    // Simulating blocking operation
    const start = Date.now();
    while (Date.now() - start < 1000) {
        // Blocking the event loop
    }
    return data;
}

/**
 * INEFFICIENT: Creating new objects/arrays in loops
 */
function inefficientObjectCreation(count) {
    const results = [];
    for (let i = 0; i < count; i++) {
        results.push({
            id: i,
            timestamp: new Date(),  // New Date object each iteration
            data: []
        });
    }
    return results;
}

/**
 * INEFFICIENT: Using try-catch in performance-critical code
 */
function inefficientErrorHandling(arr) {
    const results = [];
    for (let i = 0; i < arr.length; i++) {
        try {
            results.push(arr[i] * 2);  // Try-catch in hot loop
        } catch (e) {
            console.error(e);
        }
    }
    return results;
}

// Example usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        inefficientDOMManipulation,
        inefficientArrayIteration,
        inefficientFunctionCreation,
        inefficientArrayDeletion,
        inefficientMultipleIterations,
        inefficientStringConcat,
        inefficientMembershipTest,
        inefficientNestedLoops,
        inefficientVariableScope,
        inefficientSyncOperation,
        inefficientObjectCreation,
        inefficientErrorHandling
    };
}
