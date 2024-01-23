/*
    Question 2631: https://leetcode.com/problems/group-by/
    Actually, another trivial question labeled as "Medium"
*/

/**
 * @param {Function} fn
 * @return {Array}
 */
 Array.prototype.groupBy = function(fn) {
    const result = {};

    this.forEach((element) => {
        key = fn(element);

        if (!(key in result)) {
            result[key] = []
        }
        result[key].push(element)
    })

    return result;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */