# Question 2182: https://leetcode.com/problems/construct-string-with-repeat-limit/

"""
    A very interesting question!
"""

import heapq

class Solution:
    # Well, just do it greedily:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        frequency_dict = {}
        for char in s:
            frequency_dict[char] = frequency_dict.get(char, 0) + 1
        
        heap = []
        for [char, frequency] in frequency_dict.items():
            heapq.heappush(heap, (-1 * ord(char), (frequency, char)))
        
        chars = []
        while heap:
            (_trash, (frequency, char)) = heapq.heappop(heap)

            if frequency <= repeatLimit:
                chars.append(char * frequency)
            else:
                if heap:
                    (_trash, (second_frequency, second_char)) = heapq.heappop(heap)
                    chars.append(char * repeatLimit)
                    chars.append(second_char)

                    heapq.heappush(heap, (-1 * ord(char), (frequency - repeatLimit, char)))
                    if second_frequency > 1:
                        heapq.heappush(heap, (-1 * ord(second_char), (second_frequency - 1, second_char)))
                else:
                    chars.append(char * repeatLimit)
                    break

        return ''.join(chars)

