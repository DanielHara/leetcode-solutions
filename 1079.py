# Question 1079: https://leetcode.com/problems/letter-tile-possibilities/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        frequency_dict = {}
        
        for tile in tiles:
            frequency_dict[tile] = frequency_dict.get(tile, 0) + 1
        
        frequencies = frequency_dict.values()
        
        N = len(frequencies)
        array = [[]]
        
        for frequency in frequencies:
            new_array = []
            
            for el in array:
                for i in range(frequency + 1):
                    new_array.append([i] + el)
            
            array = new_array
        
        result = 0
        for el in array:
            divisor = 1
            for p in el:
                divisor = divisor * math.factorial(p)
            
            result = result + math.factorial(sum(el)) // divisor
        
        result = result - 1
        
        return result
