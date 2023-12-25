# Question 2261: https://leetcode.com/problems/k-divisible-elements-subarrays/

"""
    Looking at the contraints, I saw that, 1 <= nums.length <= 200, so just brute-forcing in O(N**3) will be enough.
    A way to get a better, O(N**2) solution, is to use a sliding window approach.
"""

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        i = 0
        j = 0

        result = 0
        subarrays_set = set()
        for i in range(len(nums)):
            count = 0
            array = []

            for j in range(i, len(nums)):
                if nums[j] % p == 0:
                    count = count + 1

                if count > k:
                    break

                array.append(str(nums[j]))

                serialized_array = '_'.join(array)
                if serialized_array not in subarrays_set:
                    subarrays_set.add(serialized_array)
                    result = result + 1

        return result
