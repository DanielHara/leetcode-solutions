/*
    Question 2622: https://leetcode.com/problems/cache-with-time-limit/
    Just use setTimeout and clearTimeout to do it.
*/


class TimeLimitedCache {
    constructor() {
        this.key_count = 0;
        this.key_2_value = {};
    }
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const result = key in this.key_2_value;

    if (key in this.key_2_value) {
        timeoutId = this.key_2_value[key][1];
        clearTimeout(timeoutId);
    } else {
        this.key_count = this.key_count + 1;
    }

    this.key_2_value[key] = [value, setTimeout(() => {
        delete this.key_2_value[key];
        this.key_count = this.key_count - 1;
    }, duration)];

    return result;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (key in this.key_2_value) {
        return this.key_2_value[key][0];
    }

    return -1;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    return this.key_count;
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */