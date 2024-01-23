# Question 1282: https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/

# Easily done in a greedy fashion

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups_dict = {}

        for element in groupSizes:
            groups_dict[element] = []
        
        for index, element in enumerate(groupSizes):
            if groups_dict[element] and len(groups_dict[element][-1]) < element:
                groups_dict[element][-1].append(index)
            else:
                groups_dict[element].append([index])
        
        result = []
        for groups in groups_dict.values():
            result = result + groups
        
        return result
