/*
    Question 2629: https://leetcode.com/problems/function-composition/description/
    Actually, a trivial question.
*/


/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
	return function(x) {
        let acc = x;
        
        let index = functions.length - 1;

        while (index >= 0) {
            acc = functions[index](acc);

            index = index - 1
        }

        return acc;
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */