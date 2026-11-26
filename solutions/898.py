# Question 898: https://leetcode.com/problems/bitwise-ors-of-subarrays/

# I first misread the question and thought it was XOR - had to take a look at the hint to figure it out


class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        possible_values = set()
        
        previous_possible_values = set()

        for number in arr:
            current_possible_values = set()
            current_possible_values.add(number)
            possible_values.add(number)

            for value in previous_possible_values:
                current_possible_values.add(value | number)
                possible_values.add(value | number)

            previous_possible_values = current_possible_values

        return len(possible_values)
