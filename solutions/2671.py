# Question 2671: https://leetcode.com/problems/frequency-tracker/

"""
    Not a difficult question, just use some tricks with maps. I just was confused by this text:

    bool hasFrequency(int frequency): Returns true if there is a number in the data structure that occurs frequency number of times, otherwise, it returns false.

    It should actually add "that occurs EXACTLY frequency number of times", because it may be interpreted as "that occurs AT LEAST frequency number of times"
"""

class FrequencyTracker:
    def __init__(self):
        self.map = {}
        self.frequency_to_number_set = {}

    def add(self, number: int) -> None:
        current_frequency = self.map.get(number, 0)
        if current_frequency in self.frequency_to_number_set and number in self.frequency_to_number_set[current_frequency]:
            self.frequency_to_number_set[current_frequency].remove(number)

        self.map[number] = current_frequency + 1

        frequency = self.map[number]
        if frequency not in self.frequency_to_number_set:
            self.frequency_to_number_set[frequency] = set()

        self.frequency_to_number_set[frequency].add(number)

    def deleteOne(self, number: int) -> None:
        if number not in self.map:
            return

        current_frequency = self.map[number]
        if current_frequency in self.frequency_to_number_set and number in self.frequency_to_number_set[current_frequency]:
            self.frequency_to_number_set[current_frequency].remove(number)

        new_frequency = current_frequency - 1

        if number in self.map:
            if self.map[number] == 1:
                del self.map[number]
            else:
                self.map[number] = self.map[number] - 1
        
        if new_frequency not in self.frequency_to_number_set:
            self.frequency_to_number_set[new_frequency] = set()

        self.frequency_to_number_set[new_frequency].add(number)

    def hasFrequency(self, frequency: int) -> bool:
        return bool(self.frequency_to_number_set.get(frequency))


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)