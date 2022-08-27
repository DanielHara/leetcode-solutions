# Question 1849: https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

"""
    Try all the possibilities from the first digit on (I called each of them value), and try
    to find (value - 1), (value - 2), ..., and so on.
"""

class Solution:
    def splitString(self, s: str) -> bool:
        N = len(s)

        value = 0
        
        for i in range(N - 1):
            value = value * 10 + int(s[i])
            
            # Begin the search, looking for value - 1, value - 2, ...
            j = i + 1
            count = 1

            while j < N:
                if value - count < 0:
                    break

                current = int(s[j])
                k = j + 1
                # Treat case value - count == 0
                while k < len(s) and (current < value - count or (current == 0 and value - count == 0)):
                    current = 10 * current + int(s[k])
                    k = k + 1
                
                if current == value - count:
                    count = count + 1
                else:
                    break
                
                j = k

            if count > 1 and j >= N:
                return True

        return False
        
        