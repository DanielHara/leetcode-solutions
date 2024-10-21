"""
    Question 2491: https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

    The input array should be actually called skills, and not skill.
    Notice that the order of the inputs in skills doesn't matter, so probably we can make a frequency_dict.
    From the sum of skills it's easy to calculate how much total_skill_per_team will be.
    So, for each player without a team, just build the team. If there's no complementary, just return -1
"""

class Solution:
    def dividePlayers(self, skills: List[int]) -> int:
        frequency_dict = {}

        for skill in skills:
            frequency_dict[skill] = frequency_dict.get(skill, 0) + 1
        
        result = 0
        total_skill_per_team = sum(skills) // (len(skills) // 2)
        for skill in skills:
            if frequency_dict.get(skill, 0) <= 0:
                continue

            frequency_dict[skill] = frequency_dict[skill] - 1
            complementary = total_skill_per_team - skill

            if frequency_dict.get(complementary, 0) <= 0:
                return -1

            frequency_dict[complementary] = frequency_dict[complementary] - 1
            result = result + skill * complementary
        
        return result
