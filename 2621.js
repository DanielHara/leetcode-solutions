/*
    Question 2621: https://leetcode.com/problems/sleep/
    Trivial question
*/

/**
 * @param {number} millis
 */
 async function sleep(millis) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(0);
        }, millis);
    })
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */
