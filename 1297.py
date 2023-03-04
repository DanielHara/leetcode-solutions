# Question 1297: https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

# Because of the constraints of the problem: 1 <= minSize <= maxSize <= min(26, s.length), I just 
# used brute-force and it passed.

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        string_frequency = {}
        for i in range(len(s) - minSize + 1):
            letters_set = set()
            for j in range(i, i + minSize - 1):
                letters_set.add(s[j])

            for j in range(i + minSize - 1, min(i + maxSize, len(s))):
                letters_set.add(s[j])
                if len(letters_set) <= maxLetters:
                    possibility = s[i:j + 1]
                    string_frequency[possibility] = string_frequency.get(possibility, 0) + 1
                else:
                    break
        
        if not string_frequency:
            return 0
        
        return max(string_frequency.values())
