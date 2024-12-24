# Question 2672: https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

"""
    Just some DP, no secret
"""

class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0 for element in range(n)]

        answer = []
        number_adjacent_pairs = 0
        for [index, color] in queries:
            current_color = colors[index]
            if index >= 1:
                if colors[index - 1] == current_color and current_color != 0:
                    number_adjacent_pairs = number_adjacent_pairs - 1
                if colors[index - 1] == color and color != 0:
                    number_adjacent_pairs = number_adjacent_pairs + 1
            
            if index < n - 1:
                if colors[index + 1] == current_color and current_color != 0:
                    number_adjacent_pairs = number_adjacent_pairs - 1
                if colors[index + 1] == color and color != 0:
                    number_adjacent_pairs = number_adjacent_pairs + 1

            colors[index] = color
            answer.append(number_adjacent_pairs)

        return answer
