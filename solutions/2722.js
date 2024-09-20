/*
    Question 2722: https://leetcode.com/problems/join-two-arrays-by-id/

    The trick in this question is to read the docs about Object.assign:
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign

    It reads:
        "Properties in the target object are overwritten by properties in the sources if they have the same key"
    which translates the requirement:
        "If a key is included in both objects, the value in the object from arr2 should override the value from arr1."
*/

/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    dictionary1 = {};
    arr1.forEach((obj) => {
        dictionary1[obj.id] = obj;
    });

    dictionary2 = {};
    arr2.forEach((obj) => {
        dictionary2[obj.id] = obj;
    });

    answerDictionary = {};
    Object.entries(dictionary1).forEach(([id, obj]) => {
        answerDictionary[id] = obj;
    });

    Object.entries(dictionary2).forEach(([id, obj]) => {
        if (!(id in answerDictionary)) {
            answerDictionary[id] = obj;
        } else {
            Object.assign(answerDictionary[id], obj)
        }
    });

    objects = Object.values(answerDictionary);

    return objects.sort(({id1, id2}) => id1 - id2);
};
