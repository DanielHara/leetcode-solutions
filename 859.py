# Question 859: https://leetcode.com/problems/buddy-strings/description/

"""
   Quite easy question
"""


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        frequency_dict_s = {}
        for char in s:
            frequency_dict_s[char] = frequency_dict_s.get(char, 0) + 1

        frequency_dict_goal = {}
        for char in goal:
            frequency_dict_goal[char] = frequency_dict_goal.get(char, 0) + 1
        
        if frequency_dict_s != frequency_dict_goal:
            return False
        
        differences = []
        for i in range(0, len(s), 1):
            if s[i] != goal[i]:
                differences.append(i)
        
        if len(differences) != 0 and len(differences) != 2:
            return False
        
        if len(differences) == 0:
            for value in frequency_dict_s.values():
                if value >= 2:
                    return True
            return False
        
        return s[differences[0]] == goal[differences[1]] and s[differences[1]] == goal[differences[0]]
