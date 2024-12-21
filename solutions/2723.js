/*
    Question 2723: https://leetcode.com/problems/add-two-promises
    Trivial question
*/

/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    const [resolved_value_1, resolved_value_2] = await Promise.all([promise1, promise2])

    return resolved_value_1 + resolved_value_2
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */
