/*
Question 2630: https://leetcode.com/problems/memoize-ii/

Just use a map: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map
Pay attention to https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#key_equality, which
states it uses === comparison (which is what you need to solve this question).
*/

/**
 * @param {Function} fn
 */
function memoize(fn) {
    // This is an incremental count
    let count = 0;
    // From object to object ids
    const objectToObjectId = new Map()

    // From object_ids to result
    const cache = {}

    return function(...args) {
        const key = args.map(arg => {
            if (objectToObjectId.has(arg)) {
                return objectToObjectId.get(arg)
            }

            objectToObjectId.set(arg, count);
            count = count + 1;

            return objectToObjectId.get(arg);
        }).join('_');

        if (key in cache) {
            return cache[key];
        }

        const result = fn(...args);
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
 