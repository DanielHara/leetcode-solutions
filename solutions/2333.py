# Question 2333: https://leetcode.com/problems/minimum-sum-of-squared-difference/

"""
    Very interesting question, just use a stack.
"""

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        stack = [{
            'value': 0,
            'count': 1
        }]
        
        for i in range(0, len(nums1)):
            stack.append({
                'value': abs(nums1[i] - nums2[i]),
                'count': 1
            })

        stack.sort(key=lambda el: el['value'])
        k = k1 + k2

        result = 0
        while len(stack) > 1 and k > 0:
            el = stack.pop()

            necessary = (el['value'] - stack[-1]['value']) * el['count']
            if k >= necessary:
                k = k - necessary
                stack[-1]['count'] = 1 + el['count']
            else:
                remaining = k % el['count']
                stack.append({
                    'value': (el['value'] - k // el['count'] - 1),
                    'count': remaining
                })

                stack.append({
                    'value': (el['value'] - k // el['count']),
                    'count': el['count'] - remaining
                })
                k = 0

        while stack:
            el = stack.pop()
            result = result + el['count'] * (el['value'] ** 2)

        return result
