/*
    Question 2634: https://leetcode.com/problems/filter-elements-from-array/

    Trivial question
*/

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const result = [];

    let index = 0;
    while (index < arr.length) {
        if (fn(arr[index], index)) {
            result.push(arr[index]);
        }

        index = index + 1;
    }

    return result;
};
