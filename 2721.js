/*
    Question 2721: https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/
    A general overview of the constructor of Promise already allows you to solve this question.
*/

/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
 var promiseAll = async function(functions) {
    return new Promise((resolve, reject) => {
        const arrayToResolve = Array.from(Array(functions.length).keys());
        let resolvedCount = 0;

        functions.forEach((f, index) => {
            f()
                .then(resolvedValue => {
                    arrayToResolve[index] = resolvedValue;
                    resolvedCount = resolvedCount + 1

                    if (resolvedCount === functions.length) {
                        resolve(arrayToResolve);
                    }
                })
                .catch(rejectedValue => {
                    reject(rejectedValue)
                });
        })
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */