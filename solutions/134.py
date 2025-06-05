# Question 134: https://leetcode.com/problems/gas-station/

"""
    This question is very interesting!

    What is important is always the difference between gas and cost. So, make a diff array.
    Then, take the prefix sum of the diff array, and get the lowest point. This would be your worst-case scenario. Try to
    start on the gas station right after this worst-case scenario point. If you can make it from that gas station, just return its index.
    Otherwise, return -1
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [(gas[i] - cost[i]) for i in range(len(gas))]

        prefix_sum = []
        for number in diff:
            prefix_sum.append(number + (prefix_sum[-1] if prefix_sum else 0))
        
        min_prefix_sum = min(prefix_sum)

        for index, element in enumerate(prefix_sum):
            if prefix_sum[index] == min_prefix_sum:
                candidate = (index + 1) % len(gas)
                balance = 0
                for offset in range(0, len(gas)):
                    balance = balance + diff[(candidate + offset) % len(gas)]
                    if balance < 0:
                        return -1

                return candidate
        
        return -1
