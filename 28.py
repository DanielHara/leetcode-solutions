"""
Question 28: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

I was a bit puzzled by this question, as it's rated Medium. The string matching algorithms that make a O(haystack + needle) solution possible
are hard to implement (like the Robin Karp algorithm). I then went for the trivial solution and it passed the Leetcode judge.
"""

class Solution:
    # Let's begin with the trivial 2-pointer solution
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            found = True

            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    found = False
                    break
            
            if found:
                return i
        
        return -1
