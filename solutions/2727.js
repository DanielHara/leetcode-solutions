/*
    Question 2727: https://leetcode.com/problems/is-object-empty/

    Trivial question, just warm-up of a study session!
*/

/**
 * @param {Object | Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    if (Array.isArray(obj)) {
        return obj.length === 0;
    }

    return Object.keys(obj).length === 0;
};
