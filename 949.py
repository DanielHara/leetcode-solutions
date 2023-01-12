# Question 949: https://leetcode.com/problems/largest-time-for-given-digits/description/

# I just brute-forced all possibilities, because 4! is not a large number.

class Solution:
    def getPermutations(self, arr: List[int]) -> List[List[int]]:
        if len(arr) == 1:
            return [arr]

        el = arr[len(arr) - 1]

        result = []
        previous = self.getPermutations(arr[0: len(arr) - 1])
        for p in previous:
            for i in range(len(p) + 1):
                result.append(p[0:i] + [el] + p[i:])
        
        return result

    def largestTimeFromDigits(self, arr: List[int]) -> str:
        possibilities = self.getPermutations(arr)

        result = None
        for possibility in possibilities:
            hour = 10 * possibility[0] + possibility[1]
            minutes = 10 * possibility[2] + possibility[3]

            if hour < 24 and minutes < 60:
                if result is None:
                    result = [hour, minutes]
                else:
                    if hour > result[0]:
                        result = [hour, minutes]
                    elif hour == result[0] and minutes > result[1]:
                        result = [hour, minutes]
        
        if result is None:
            return ''
        
        hour_string = str(result[0])
        if len(hour_string) == 1:
            hour_string = '0' + hour_string 

        minutes_string = str(result[1])
        if len(minutes_string) == 1:
            minutes_string = '0' + minutes_string
        
        return hour_string + ':' + minutes_string
