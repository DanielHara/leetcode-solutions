# Question 1419: https://leetcode.com/problems/minimum-number-of-frogs-croaking/

"""
    A very interesting question!
"""


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        chart_to_positions_dict = {}

        frequency_dict = {}
        for index, char in enumerate(reversed(croakOfFrogs)):
            if char not in chart_to_positions_dict:
                chart_to_positions_dict[char] = []
            chart_to_positions_dict[char].append(index)

            frequency_dict[char] = frequency_dict.get(char, 0) + 1
        
        for char in 'roak':
            if frequency_dict.get(char, 0) != frequency_dict.get('c', 0):
                return -1

        result = 0
        frogs = 0
        for index, char in enumerate(croakOfFrogs):
            if char == 'c':
                frogs = frogs + 1
                chart_to_positions_dict['c'].pop()

                if not chart_to_positions_dict['r']:
                    return -1

            elif char == 'r':
                if frogs == 0:
                    return -1
                chart_to_positions_dict['r'].pop()

                if not chart_to_positions_dict['o']:
                    return -1
            
            elif char == 'o':
                if frogs == 0:
                    return -1
                chart_to_positions_dict['o'].pop()

                if not chart_to_positions_dict['a']:
                    return -1

            elif char == 'a':
                if frogs == 0:
                    return -1
                chart_to_positions_dict['a'].pop()

                if not chart_to_positions_dict['k']:
                    return -1

            elif char == 'k':
                if frogs == 0:
                    return -1

                frogs = frogs - 1

                chart_to_positions_dict['k'].pop()

            result = max(result, frogs)

        return result


