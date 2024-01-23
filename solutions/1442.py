# Question 1442: https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor

"""
    Quite easy, but interesting question. Just use some DP.
    You can use an approach similar to prefix sum for XOR, because, if
    S[j] = arr[0] ^ arr[1] ^ (...) ^ arr[j], then:
    arr[i] ^ (...) ^ arr[j] = S[j] ^ S[i - 1]

    That is quite easy to verify.
"""

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        S = []

        for number in arr:
            S.append(number ^ (S[-1] if S else 0))
        
        result = 0
        for i in range(0, len(arr) - 1, 1):
            for j in range(i + 1, len(arr), 1):
                for k in range(j, len(arr), 1):
                    if S[j - 1] ^ (S[i - 1] if i - 1 >= 0 else 0) == S[k] ^ S[j - 1]:
                        result = result + 1

        return result
