# Question 87: https://leetcode.com/problems/scramble-string/

"""
    Very interesting question!
    Just brute-force all the possibilities, and use some DP for the solution not to explode exponentially in time.
"""


class Solution:
    def recursiveIsScramble(self, s1: str, s2: str) -> bool:
        if len(s1) == 1 and len(s2) == 1:
            return s1 == s2
        
        key_1 = s1 + '_' + s2
        if key_1 in self.dp:
            return self.dp[key_1]

        key_2 = s2 + '_' + s1
        if key_2 in self.dp:
            return self.dp[key_2]

        frequency_dict_1_right = {}
        for char in s1:
            frequency_dict_1_right[char] = frequency_dict_1_right.get(char, 0) + 1
        
        frequency_dict_2_right = {}
        for char in s2:
            frequency_dict_2_right[char] = frequency_dict_2_right.get(char, 0) + 1
        
        if not (frequency_dict_1_right == frequency_dict_2_right):
            return False

        frequency_dict_1_left = {}
        frequency_dict_2_left = {}

        N = len(s1)
        for index in range(N - 1):
            frequency_dict_1_left[s1[index]] = frequency_dict_1_left.get(s1[index], 0) + 1
            frequency_dict_2_left[s2[index]] = frequency_dict_2_left.get(s2[index], 0) + 1

            frequency_dict_1_right[s1[index]] = frequency_dict_1_right.get(s1[index], 0) - 1
            if frequency_dict_1_right.get(s1[index], 0) == 0:
                del frequency_dict_1_right[s1[index]]

            frequency_dict_2_right[s2[index]] = frequency_dict_2_right.get(s2[index], 0) - 1
            if frequency_dict_2_right.get(s2[index], 0) == 0:
                del frequency_dict_2_right[s2[index]]
            
            if frequency_dict_1_left == frequency_dict_2_left and frequency_dict_1_right == frequency_dict_2_right:
                if self.recursiveIsScramble(s1[:index + 1], s2[:index + 1]) and self.recursiveIsScramble(s1[index + 1:], s2[index + 1:]):
                    key_1 = s1 + '_' + s2
                    self.dp[key_1] = True
                    key_2 = s2 + '_' + s1
                    self.dp[key_2] = True

                    return True

            if frequency_dict_1_left == frequency_dict_2_right and frequency_dict_2_left == frequency_dict_1_right:
                if self.recursiveIsScramble(s1[:index + 1], s2[index + 1:]) and self.recursiveIsScramble(s1[index + 1:], s2[:index + 1]):
                    key_1 = s1 + '_' + s2
                    self.dp[key_1] = True
                    key_2 = s2 + '_' + s1
                    self.dp[key_2] = True

                    return True
        
        
        frequency_dict_1_right = {}
        for char in s1:
            frequency_dict_1_right[char] = frequency_dict_1_right.get(char, 0) + 1
        
        frequency_dict_2_left = {}
        for char in s2:
            frequency_dict_2_left[char] = frequency_dict_2_left.get(char, 0) + 1

        frequency_dict_1_left = {}
        frequency_dict_2_right = {}

        for index in range(N - 1):
            frequency_dict_1_left[s1[index]] = frequency_dict_1_left.get(s1[index], 0) + 1
            frequency_dict_2_right[s2[N - 1 - index]] = frequency_dict_2_right.get(s2[N - 1 - index], 0) + 1

            frequency_dict_1_right[s1[index]] = frequency_dict_1_right.get(s1[index], 0) - 1
            if frequency_dict_1_right.get(s1[index], 0) == 0:
                del frequency_dict_1_right[s1[index]]

            frequency_dict_2_left[s2[N - 1 - index]] = frequency_dict_2_left.get(s2[N - 1 - index], 0) - 1
            if frequency_dict_2_left.get(s2[N - 1 - index], 0) == 0:
                del frequency_dict_2_left[s2[N - 1 - index]]
            
            if frequency_dict_1_left == frequency_dict_2_right and frequency_dict_1_right == frequency_dict_2_left:
                if self.recursiveIsScramble(s1[:index + 1], s2[N - 1 - index:]) and self.recursiveIsScramble(s1[index + 1:], s2[:N - 1 - index]):
                    key_1 = s1 + '_' + s2
                    self.dp[key_1] = True
                    key_2 = s2 + '_' + s1
                    self.dp[key_2] = True

                    return True

        
        key_1 = s1 + '_' + s2
        self.dp[key_1] = False
        key_2 = s2 + '_' + s1
        self.dp[key_2] = False

        return False


    def isScramble(self, s1: str, s2: str) -> bool:
        self.dp = {}

        return self.recursiveIsScramble(s1, s2)
