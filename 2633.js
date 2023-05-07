/*
Question 2633: https://leetcode.com/problems/convert-object-to-json-string/

Quite nice question! I opted to use an array to store the tokens of the stringified version of the input
because concatening strings with string.concat in JS is a O(N) operation, which would make my solution
explode to O(N*2) time.
*/


var recursiveJsonStringifyInPlace = function (object, acc) {
    if (object === null) {
        acc.push('null');
        return;
    }

    if (typeof object === 'number' || typeof object === 'boolean') {
        acc.push(`${object}`);
        return;
    }

    if (typeof object === 'string') {
        acc.push('"');
        acc.push(object);
        acc.push('"');
        return;
    }

    // if it's an array, then
    if (Array.isArray(object)) {
        acc.push('[');

        let i = 0;
        while (i < object.length) {
            element = object[i];

            recursiveJsonStringifyInPlace(element, acc)

            if (i < object.length - 1) {
                acc.push(',');
            }

            i = i + 1;
        }

        acc.push(']');
        return;
    }

    // If it gets here, it's an object

    const entries = Object.entries(object);

    acc.push('{');

    let i = 0;
    while (i < entries.length) {
        const key = entries[i][0];
        const value = entries[i][1];
        
        acc.push(`"${key}":`);

        recursiveJsonStringifyInPlace(value, acc);

        if (i < entries.length - 1) {
            acc.push(',');
        }
        i = i + 1;
    }    
    
    acc.push('}');
    // Then, the result will be in acc
}



/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function(object) {
    const resultTokens = [];

    recursiveJsonStringifyInPlace(object, resultTokens);

    return resultTokens.join('');
};
