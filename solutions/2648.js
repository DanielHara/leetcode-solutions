/*
    Question 2648: https://leetcode.com/problems/generate-fibonacci-sequence/

    Easy question, just use yield
*/


/**
 * @return {Generator<number>}
 */
var fibGenerator = function*() {
    const numbers = [0, 1]

    while (true) {
        const nextNumber = numbers[0] + numbers[1];
        numbers.push(nextNumber);
        const number = numbers.shift();
        
        yield number;
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */