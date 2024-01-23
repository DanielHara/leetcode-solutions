# Question 860: https://leetcode.com/problems/lemonade-change/

"""
   Quite easy question
"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # change[0] is the amount of $5 bills, change[1] is the amount of $10 bills
        change = [0, 0]

        for bill in bills:
            if bill == 5:
                change[0] = change[0] + 1
            
            elif bill == 10:
                if change[0] == 0:
                    return False

                change[1] = change[1] + 1
                change[0] = change[0] - 1

            else:
                if change[1] > 0 and change[0] > 0:
                    change[1] = change[1] - 1
                    change[0] = change[0] - 1
                elif change[0] >= 3:
                    change[0] = change[0] - 3
                else:
                    return False
            
        return True
