# Question 1358: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        
        index_dict = {}
        
        A_only_substrings = 0
        B_only_substrings = 0
        C_only_substrings = 0
        
        no_A_substrings = 0
        no_B_substrings = 0
        no_C_substrings = 0
        
        consecutive_A = 0
        consecutive_B = 0
        consecutive_C = 0
        
        for index, char in enumerate(s):
            if char not in index_dict:
                index_dict[char] = [index]
                
                if char == 'a':
                    no_A_substrings = no_A_substrings + int(index * (index + 1) / 2)
                elif char == 'b':
                    no_B_substrings = no_B_substrings + int(index * (index + 1) / 2)
                else:
                    no_C_substrings = no_C_substrings + int(index * (index + 1) / 2)
            else:
                if char == 'a':
                    no_A_substrings = no_A_substrings + int((index - index_dict[char][-1] - 1) * (index - index_dict[char][-1]) / 2)
                elif char == 'b':
                    no_B_substrings = no_B_substrings + int((index - index_dict[char][-1] - 1) * (index - index_dict[char][-1]) / 2)
                else:
                    no_C_substrings = no_C_substrings + int((index - index_dict[char][-1] - 1) * (index - index_dict[char][-1]) / 2)
                    
                index_dict[char].append(index)
                
            
            if char == 'a':
                consecutive_A = consecutive_A + 1
                
                B_only_substrings = B_only_substrings + int(consecutive_B * (consecutive_B + 1) / 2)
                C_only_substrings = C_only_substrings + int(consecutive_C * (consecutive_C + 1) / 2)
                
                consecutive_B = 0
                consecutive_C = 0
            elif char == 'b':
                consecutive_B = consecutive_B + 1
                
                A_only_substrings = A_only_substrings + int(consecutive_A * (consecutive_A + 1) / 2)
                C_only_substrings = C_only_substrings + int(consecutive_C * (consecutive_C + 1) / 2)
                consecutive_A = 0
                consecutive_C = 0
            else:
                consecutive_C = consecutive_C + 1

                A_only_substrings = A_only_substrings + int(consecutive_A * (consecutive_A + 1) / 2)
                B_only_substrings = B_only_substrings + int(consecutive_B * (consecutive_B + 1) / 2)
                consecutive_A = 0
                consecutive_B = 0
        
        A_only_substrings = A_only_substrings + int(consecutive_A * (consecutive_A + 1) / 2)
        B_only_substrings = B_only_substrings + int(consecutive_B * (consecutive_B + 1) / 2)
        C_only_substrings = C_only_substrings + int(consecutive_C * (consecutive_C + 1) / 2)
        
        total = (len(s) * (len(s) + 1)) // 2

        if 'a' in index_dict:
            index = index_dict['a'][-1]
            no_A_substrings = no_A_substrings + int((len(s) - index - 1) * (len(s) - index) / 2)
        else:
            no_A_substrings = total
        
        if 'b' in index_dict:
            index = index_dict['b'][-1]
            no_B_substrings = no_B_substrings + int((len(s) - index - 1) * (len(s) - index) / 2)
        else:
            no_B_substrings = total
        
        if 'c' in index_dict:
            index = index_dict['c'][-1]
            no_C_substrings = no_C_substrings + int((len(s) - index - 1) * (len(s) - index) / 2)
        else:
            no_C_substrings = total
        
        return total - no_A_substrings - no_B_substrings - no_C_substrings + A_only_substrings + B_only_substrings + C_only_substrings
