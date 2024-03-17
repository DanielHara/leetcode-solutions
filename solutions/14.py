"""
    Question 14: https://leetcode.com/problems/longest-common-prefix/
"""

# Quite interesting question, you can use a trie to make it O(N) instead of brute-forcing, which would lead to a (N**2) solution

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = {}

        for string in strs:
            p = trie
            for char in string:
                if char not in p:
                    p[char] = {}
                
                p = p[char]

            p['done'] = True
        
        prefix_chars = []
        p = trie
        while p and len(p) == 1:
            char = list(p.keys())[0]
            if char == 'done':
                break

            prefix_chars.append(char)
            p = p[char]

        return ''.join(prefix_chars)
