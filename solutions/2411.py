# Question 2411: https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

# This question is quite challenging! Store the power of the digits in dicts, and use a sliding window

class Solution:
    def digits_maps_evaluate_to_equal_or(self, A_dict, B_dict):
        for key in A_dict:
            if A_dict.get(key, 0) > 0 and B_dict.get(key, 0) <= 0:
                return False

        for key in B_dict:
            if B_dict.get(key, 0) > 0 and A_dict.get(key, 0) <= 0:
                return False

        return True

    def add_digits_dicts(self, A_dict, B_dict):
        result = {}

        for [key, value] in A_dict.items():
            result[key] = result.get(key, 0) + value
        
        for [key, value] in B_dict.items():
            result[key] = result.get(key, 0) + value

        return result
    
    def subtract_digits_dicts(self, A_dict, B_dict):
        result = {}

        for [key, value] in A_dict.items():
            result[key] = result.get(key, 0) + value

        for [key, value] in B_dict.items():
            result[key] = result.get(key, 0) - value
        
        return result


    def get_digits_dict(self, num: int):
        power = 0

        digits_dict = {}
        while num > 0:
            if num % 2 == 1:
                digits_dict[power] = digits_dict.get(power, 0) + 1

            power = power + 1
            num = num // 2

        return digits_dict


    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        sufix_maps = []
        for num in nums:
            sufix_maps.append(None)

        current_or = 0
        for index in range(len(nums) - 1, -1, -1):
            current_or = current_or | nums[index]

            sufix_maps[index] = self.get_digits_dict(current_or)
        
        start = 0
        end = 0
        current_digits_map = {}

        answer = []
        while start < len(nums):
            end = max(end, start)

            while end < len(nums):
                current_digits_map = self.add_digits_dicts(current_digits_map, self.get_digits_dict(nums[end]))

                if self.digits_maps_evaluate_to_equal_or(current_digits_map, self.add_digits_dicts(current_digits_map, sufix_maps[end + 1] if end + 1 < len(sufix_maps) else {})):
                    answer.append(end - start + 1)
                    if end > start:
                        current_digits_map = self.subtract_digits_dicts(current_digits_map, self.get_digits_dict(nums[end]))
                    break
                else:
                    end = end + 1

            # Substract
            current_digits_map = self.subtract_digits_dicts(current_digits_map, self.get_digits_dict(nums[start]))
            start = start + 1

        return answer
