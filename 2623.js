/*
    Question 2623: https://leetcode.com/problems/memoize/description/
    Actually, a trivial question.
*/


/**
 * @param {Function} fn
 */
 function memoize(fn) {
    const cache = {};

    return function(...args) {
        const key = args.join('_');
        if (key in cache) {
            return cache[key];
        }

        const result = fn(...args)
        cache[key] = result;
        return result;
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */