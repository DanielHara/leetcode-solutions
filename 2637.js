/*
Question 2637: https://leetcode.com/problems/promise-time-limit/

Quite easy question if you know your stuff about Promises.
*/


/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
 var timeLimit = function(fn, t) {
	return async function(...args) {
        return new Promise((resolve, reject) => {
            fn(...args).then((result) => resolve(result)).catch(error => reject(error))

            setTimeout(() => reject('Time Limit Exceeded'), t)
        })
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */