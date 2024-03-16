# Question 80: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# A very simple follow-up from question 26, very trivial

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read_pointer = 0
        write_pointer = 0
        while read_pointer < len(nums):
            search_pointer = read_pointer
            while search_pointer < len(nums) and nums[search_pointer] == nums[read_pointer]:
                search_pointer = search_pointer + 1

            nums[write_pointer] = nums[read_pointer]
            write_pointer = write_pointer + 1
            if search_pointer - read_pointer >= 2:    
                nums[write_pointer] = nums[read_pointer]
                write_pointer = write_pointer + 1

            read_pointer = search_pointer
        
        return write_pointer
