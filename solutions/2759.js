/**
 * @param {string} str
 * @return {null|boolean|number|string|Array|Object}
 */


 /*
    Still an incomplete solution.   
    It passes the test cases with nested JSONs, containing only strings, numbers, booleans, and null:
    '{"a":"e"}'
    '{"a":"e","b":{"c":"d"}}'
    '{"a":"e","b":{"c":{"bg":"gd"}}}'
    '{"a":"e","b":{"c":{"bg":"gd"},"tg":"avc"}}'
    '{"a":2,"b":{"c":"d"},"c":true,"d":null}'
 */

    /**
 * @param {string} str
 * @return {null|boolean|number|string|Array|Object}
 */

var parsePrimitive = function(str) {
    if (str.includes('"')) {
        return str.replaceAll('"', '');
    }

    if (str === 'true') {
        return true;
    }

    if (str === 'false') {
        return false;
    }

    if (str === 'null') {
        return null;
    }

    return Number(str);
}

var jsonParse = function(str) {
    const tokenizedStr = str.split(/({|}|}|:|,)/g)
    const tokens = tokenizedStr.filter(str => str.length > 0 && str !== ',');

    const stack = []

    for (const token of tokens) {
        if (token === '{') {
            stack.push({});
        } else if (token === '}') {
            if (stack.length >= 4) {
                const currentObject = stack.pop();
                stack.pop();
                const key = stack.pop().replaceAll('"', '');
                const object = stack.pop();
                object[key] = currentObject
                stack.push(object);
            }
        } else {
            if (stack && stack[stack.length - 1] === ':') {
                stack.pop();
                const key = stack.pop().replaceAll('"', '');
                const object = stack.pop();
                const value = parsePrimitive(token);
                object[key] = value;

                stack.push(object)
            } else {
                stack.push(token);
            }
        }
    }

    return stack[0];
};
