# Question 1717: https://leetcode.com/problems/maximum-score-from-removing-substrings/

# A greedy approach: If x > y, try to eliminate as many occurences of 'ab' as you can, otherwise
# try to eliminate as many occurences of 'ba' as you can.

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        N = len(s)
        
        i = 0
        
        result = 0
        
        if x >= y:
            while i < N:
            
                deque = []
                j = i
                A = 0
                B = 0

                while j < N and (s[j] == 'a' or s[j] == 'b'):
                    if deque and deque[-1] == 'a' and s[j] == 'b':
                        deque.pop()
                        result = result + x
                        A = A - 1
                    else:
                        deque.append(s[j])
                        if s[j] == 'a':
                            A = A + 1
                        else:
                            B = B + 1

                    j = j + 1
            
                result = result + min(A, B) * y
                
                i = j + 1
        
            return result
        
        
        
        while i < N:

            deque = []
            j = i
            A = 0
            B = 0

            while j < N and (s[j] == 'b' or s[j] == 'a'):
                if deque and deque[-1] == 'b' and s[j] == 'a':
                    deque.pop()
                    result = result + y
                    B = B - 1
                else:
                    deque.append(s[j])
                    if s[j] == 'a':
                        A = A + 1
                    else:
                        B = B + 1

                j = j + 1

            result = result + min(A, B) * x

            i = j + 1
        
        return result