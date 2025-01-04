# Question 1616: https://leetcode.com/problems/split-two-strings-to-make-palindrome/

"""
    Interesting question!

    Use some DP to do the trick. dp_a[position] saves if string a[position:len(a) - 1 - position] is a palindrome.
    First, take just the first case, you try to make the palindrome with a_prefix and b_suffix.

    Then, go through the string a, comparing the characters a[position] != b[N - 1 - position]. If they are different, no palindrome is possible.
    If they are equal, then see if a[position:len(a) - 1 - position] or b[position:len(b) - 1 - position] are a palindrome. If they are, just return True.
"""

class Solution:
    def makeDpArray(self, s: str):
        dp = [None for char in s]
        N = len(s)
        half = N // 2 - 1 if N % 2 == 0 else N // 2

        if N % 2 != 0:
            dp[half] = True
        else:
            half = N // 2 - 1
            dp[half] = (s[half] == s[half + 1])
            dp[half + 1] = dp[half]

        for position in range(half - 1, -1, -1):
            dp[position] = dp[position + 1] and (s[position] == s[N - 1 - position])
            dp[N - 1 - position] = dp[position]

        return dp
    
    def checkPalindromeFormation1(self, a: str, b: str) -> bool:
        dp_a = self.makeDpArray(a)
        dp_b = self.makeDpArray(b)

        N = len(a)
        if dp_b[0]:
            return True
        
        for position in range(0, N // 2, 1):
            if a[position] != b[N - 1 - position]:
                return False
            if dp_a[position + 1] or dp_b[position + 1]:
                return True
        
        return True

    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.checkPalindromeFormation1(a, b) or self.checkPalindromeFormation1(b, a)
