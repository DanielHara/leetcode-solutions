"""
    Question 2526: https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/
    
    Quite easy question, I don't understand why it's rated as Medium.
"""

class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.number_seen_values = 0

    def consec(self, num: int) -> bool:
        if num != self.value:
            self.number_seen_values = 0
            return False
        
        self.number_seen_values = self.number_seen_values + 1
        return self.number_seen_values >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)