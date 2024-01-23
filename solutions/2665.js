/*
    Question 2665: https://leetcode.com/problems/counter-ii
    Just use the concept of JavaScript closures.
*/

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
 var createCounter = function(init) {
    let count = init;

    return {
        increment: () => {
            count = count + 1;
            return count;
        },
        decrement: () => {
            count = count - 1;
            return count;
        },
        reset: () => {
            count = init;
            return count;
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */