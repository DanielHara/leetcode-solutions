/*
    Question 2618: https://leetcode.com/problems/check-if-object-instance-of-class/

    Interesting, but quite frustrating question, as it's a bit misleading.
    I had to peak at the hints to come up with a solution.
*/

/**
 * @param {any} obj
 * @param {any} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if (obj === null || obj === undefined) {
        return false;
    }

    if (classFunction === null || classFunction === undefined) {
        return false;
    }

    let prototype = Object.getPrototypeOf(obj);

    while (prototype !== null) {
        if (prototype === classFunction.prototype) {
            return true;
        }
        prototype = Object.getPrototypeOf(prototype);
    }

    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */