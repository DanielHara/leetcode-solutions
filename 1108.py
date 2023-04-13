# Question 1108: https://leetcode.com/problems/defanging-an-ip-address/

# Trivial question

class Solution:
    def defangIPaddr(self, address: str) -> str:
        tokens = address.split('.')

        return '[.]'.join(tokens)
