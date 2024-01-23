/*
    Question 2620: https://leetcode.com/problems/counter
*/

/**
 * @param {number} n
 * @return {Function} counter
 */
 var createCounter = function(n) {
    let count = n - 1;

    return function() {
        count = count + 1;
        return count;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
