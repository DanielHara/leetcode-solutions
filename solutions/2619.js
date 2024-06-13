/*
    Question 2619: https://leetcode.com/problems/array-prototype-last/
    Trivial question
*/

/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    const length = this.length;
 
    if (length === 0) {
         return -1;
    }
 
    return this[length - 1]
 };
 
 /**
  * const arr = [1, 2, 3];
  * arr.last(); // 3
  */