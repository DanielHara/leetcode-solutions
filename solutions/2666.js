/*
    Question 2666: https://leetcode.com/problems/allow-one-function-call/
    In this question, also just use the concept of JavaScript closures.
*/

/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let hasBeenCalled = false

    return function(...args){
        if (hasBeenCalled) {
            return undefined;
        }

        hasBeenCalled = true;
        return fn(...args);
    }
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
