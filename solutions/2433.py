"""
    Question 2433: https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

    Not a difficult question. Notice that, if a = b ^ c, then a ^ c = b. Then, if
        pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i], then
        pref[i] = pref[i - 1] ^ arr[i], which means:
        arr[i] = pref[i] ^ pref[i - 1]
"""

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        answer = [pref[0]]

        for i in range(1, len(pref)):
            answer.append(pref[i] ^ pref[i - 1])
        
        return answer
