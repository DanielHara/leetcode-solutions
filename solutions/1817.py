# Question 1817: https://leetcode.com/problems/finding-the-users-active-minutes/

"""
    Quite trivial question. Just tweak a bit with dictionaries.
"""

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_2_active_minutes_set_dict = {}

        for [user_id, time] in logs:
            if user_id not in user_2_active_minutes_set_dict:
                user_2_active_minutes_set_dict[user_id] = set()

            user_2_active_minutes_set_dict[user_id].add(time)
        
        answer = [0 for dummy in range(k)]
        for time_set in user_2_active_minutes_set_dict.values():
            uam = len(time_set)
            if uam >= 1 and uam <= k:
                answer[uam - 1] = answer[uam - 1] + 1

        return answer
