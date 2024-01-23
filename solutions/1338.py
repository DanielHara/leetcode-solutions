"""
Question 1338: https://leetcode.com/problems/reduce-array-size-to-the-half/

    IMHO, should actually be an easy question, not medium, as the solution is fairly trivial to come up with.
"""

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        N = len(arr)
        
        occurences_dict = {}
        
        for number in arr:
            occurences_dict[number] = occurences_dict.get(number, 0) + 1
        
        result = 0
        
        heap = []
        for value in occurences_dict.values():
            heapq.heappush(heap, -1 * value)
        
        soma = 0
        while heap and N - soma > soma:
            soma = soma + (-1)*heapq.heappop(heap)
            result = result + 1
        
        return result
