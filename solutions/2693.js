/*
    Question 2693: https://leetcode.com/problems/call-function-with-custom-context/
    You can just use a Symbol: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol
*/

/**
 * @param {Object} context
 * @param {any[]} args
 * @return {any}
 */
 Function.prototype.callPolyfill = function(context, ...args) {
    const object = {...context};
    symbol = Symbol();

    object[symbol] = this;
    return object[symbol](...args);
}

/**
 * function increment() { this.count++; return this.count; }
 * increment.callPolyfill({count: 1}); // 2
 */

