/*
    Question 2627: https://leetcode.com/problems/debounce/
    Just know how setTimeout and clearTimeout work
*/


/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
 var debounce = function(fn, t) {
    let id = null;

    return function(...args) {
        if (id) {
            clearTimeout(id);
            id = null;
        }

        id = setTimeout(() => {
            fn(...args)
        }, t)
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */