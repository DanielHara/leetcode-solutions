/*
    Question 2625: https://leetcode.com/problems/flatten-deeply-nested-array
    Just do it recursively
*/


/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
 var flat = function (arr, n) {
    if (n <= 0) {
        return arr;
    }

    const result = [];

    arr.forEach((element) => {
        if (typeof element === 'number') {
            result.push(element);
        } else {
            const flattened = flat(element, n - 1);
            flattened.forEach((el) => {
                result.push(el);
            });
        }
    });

    return result
};
