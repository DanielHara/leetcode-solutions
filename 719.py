# Question 719: https://leetcode.com/problems/find-k-th-smallest-pair-distance/

"""
    I just peaked at the hint:
        Binary search for the answer. How can you check how many pairs have distance <= X?
    That's quite easy. Just sort the array and use binary search.

    Then just use this and binary-search for the answer.
"""    

class Solution:
    def binarySearchForResult(self, nums: List[int], start: int, end: int, k: int):
        if start > end:
            return None
        
        half = (start + end) // 2

        number_of_pairs_less_or_equal = self.getNumberOfPairsWithDistanceLessOrEqualTo(nums, half)
        number_of_pairs_less_or_equal_previous = self.getNumberOfPairsWithDistanceLessOrEqualTo(nums, half - 1)

        if number_of_pairs_less_or_equal >= k and number_of_pairs_less_or_equal_previous < k:
            return half
        
        if number_of_pairs_less_or_equal < k:
            return self.binarySearchForResult(nums, half + 1, end, k)
        
        return self.binarySearchForResult(nums, start, half - 1, k)

    # returns the largest index for which nums[index] <= target, and returns None, if there is none
    def binarySearch(self, start: int, end: int, nums: List[int], target: int):
        if start > end:
            return None

        half = (start + end) // 2

        if nums[half] <= target and (half == end or nums[half + 1] > target):
            return half

        if nums[half] <= target:
            return self.binarySearch(half + 1, end, nums, target)

        return self.binarySearch(start, half - 1, nums, target)

    # returns the number of pairs which have distance <= target
    def getNumberOfPairsWithDistanceLessOrEqualTo(self, nums: List[int], target: int):
        result = 0

        if (target == 0):
            print(nums)

        for start in range(0, len(nums) - 1):
            end = self.binarySearch(start + 1, len(nums) - 1, nums, target + nums[start])

            if target == 0:
                print('start = ', start)
                print('end = ', end)

            if end is not None:
                result = result + end - start
        
        print('getNumberOfPairsWithDistanceLessOrEqualTo ', target, 'result = ', result)

        return result

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        N = len(nums)
        
        return self.binarySearchForResult(nums, 0, nums[-1] - nums[0], k)
