"""
Question 1573: https://leetcode.com/problems/number-of-ways-to-split-a-string/

Just keep an array with the positions of the "1" characters. If its length it's not divisible by 3, it's impossible to
split the string in 3 parts with equal numbers of "1"s. Going further, you can split this array into 3 and check how many
zeros there are between these chunks. You can then count the number of possibilities by multiplying the number of zeros
between the first and second chunk, by the number of zeros between the second and third.

If the string doesn't have any ones, then any split in 3 strings is valid, and this can be done by choosing between (k - 1)
zero characters (where k is the string length). The number of ways to choose 2 elements out of a group of (k - 1) is then (k-1)*(k-2) / 2.

"""

class Solution:
    def numWays(self, s: str) -> int:
        mod = 10 ** 9 + 7
        
        array = []
        
        for index, char in enumerate(s):
            if char == '1':
                array.append(index)
        
        if len(array) % 3 != 0:
            return 0
        
        if len(array) == 0:
            k = len(s)
            
            return int(((k - 1) * (k - 2) / 2) % mod) if k >= 3 else 0
        
        N = len(array)
        x = array[int(N/3) - 1]
        y = array[int(N/3)]
        
        z = array[int(2*N/3) - 1]
        w = array[int(2*N/3)]
        
        # My first submission failed with "Wrong answer" because I forgot to include the module operation :)
        return ((w - z) % mod)* ((y - x) % mod) % mod
