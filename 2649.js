/*
Question 2649: https://leetcode.com/problems/nested-array-generator

Quite interesting question! I myself had never used the yield syntax before solving it!
*/


/**
 * @param {Array} arr
 * @return {Generator}
 */
 var inorderTraversal = function*(arr) {
    let i = 0;
    let recursiveGenerator;

    while (i < arr.length) {
        if (typeof arr[i] === 'number') {
            recursiveGenerator = undefined;

            const value = arr[i];
            i = i + 1;

            yield value;
        } else {
            if (!recursiveGenerator) {
                recursiveGenerator = inorderTraversal(arr[i]);
            }

            iteration = recursiveGenerator.next()

            if (iteration.done) {
                recursiveGenerator = undefined;
                i = i + 1;
            } else {
                yield iteration.value;
            }
        }
    }
};

/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */
