/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: function(arg) {
            if (arg === val) {
                return true
            }
            throw "Not Equal"
        },
        notToBe: function(arg) {
            if (arg !== val) {
                return true
            }
            throw "Equal"
        }
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
