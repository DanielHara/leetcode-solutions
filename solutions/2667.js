/*
    Question 2667: https://leetcode.com/problems/create-hello-world-function    
*/

// What is this question doing on Leetcode?

/**
 * @return {Function}
 */
var createHelloWorld = function() { 
    return function(...args) {
        return 'Hello World'     
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */