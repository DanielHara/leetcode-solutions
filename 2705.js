/*
    Question 2705: https://leetcode.com/problems/compact-object
    Just do it, recursively
*/

/**
 * @param {Object} obj
 * @return {Object}
 */
 var compactObject = function(obj) {
    if (Array.isArray(obj)) {
        return obj.filter(element => element).map(element => typeof element === 'object' ? compactObject(element) : element);
    }

    if (typeof obj === 'object') {
        Object.keys(obj).forEach((key) => {
            if (!obj[key]) {
                delete obj[key];
            } else {
                obj[key] = compactObject(obj[key]);
            }
        })
    }

    return obj;
};
