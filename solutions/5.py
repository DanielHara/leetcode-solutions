class Solution:
    def isPalindrome(self, start, end) -> bool:
        if start == end:
            return True

        if start + 1 == end:
            return self.s[start] == self.s[end]
        
        if self.dp[start][end] is not None:
            return self.dp[start][end]
        
        if self.s[start] != self.s[end]:
            self.dp[start][end] = False
            return False
        
        result = self.isPalindrome(start + 1, end - 1)
        self.dp[start][end] = result
        return result

    def longestPalindrome(self, s: str) -> str:
        result = ''

        # O(N**2)
        # dp[start][end] will save the result of isPalindrome for string s[start:end]
        self.dp = [[None for i in range(len(s))] for j in range(len(s))]
        self.s = s

        best_indexes = [0, 0]
        for start in range(len(s)):
            for end in range(len(s) - 1, start - 1, -1):
                if self.isPalindrome(start, end):
                    if end - start + 1 > best_indexes[1] - best_indexes[0] + 1:
                        best_indexes = [start, end]
        
        [start, end] = best_indexes
        result = s[start:end + 1]
    
        return result
