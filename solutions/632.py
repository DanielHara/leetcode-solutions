"""
    Question 632: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

    Another very interesting Hard (but actually not so hard) question. Just put all the numbers in ascending order, in the same
    array, but also save in which list they are. Then use a sliding-window approach, trying always to get the shortest window
    for which there are elements of all lists. You can do that easily with a frequency dictionary.
"""

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)

        v = []
        for array_index, array in enumerate(nums):
            for number in array:
                v.append({
                    'list_index': array_index,
                    'number': number
                })
        
        v.sort(key=lambda el: el['number'])

        # Now, use a sliding window
        frequency_dict_list_indexes = {}

        j = 0
        while j < len(v) and len(frequency_dict_list_indexes) < k:
            element = v[j]
            
            frequency_dict_list_indexes[element['list_index']] = frequency_dict_list_indexes.get(element['list_index'], 0) + 1
            j = j + 1
        
        result = [v[0]['number'], v[j - 1]['number']]

        i = 0
        while i < len(v):
            while i < len(v) and len(frequency_dict_list_indexes) >= k:
                possibility = [v[i]['number'], v[j - 1]['number']]
                if possibility[1] - possibility[0] < result[1] - result[0]:
                    result = possibility

                element = v[i]
                
                frequency_dict_list_indexes[element['list_index']] = frequency_dict_list_indexes[element['list_index']] - 1
                if frequency_dict_list_indexes[element['list_index']] == 0:
                    del frequency_dict_list_indexes[element['list_index']]

                i = i + 1
            
            while j < len(v) and len(frequency_dict_list_indexes) < k:
                element = v[j]
                frequency_dict_list_indexes[element['list_index']] = frequency_dict_list_indexes.get(element['list_index'], 0) + 1

                j = j + 1

            # Update the result
            if len(frequency_dict_list_indexes) >= k:
                possibility = [v[i]['number'], v[j - 1]['number']]

                if possibility[1] - possibility[0] < result[1] - result[0]:
                    result = possibility
            else:
                return result
        
        return result

