# Question 2856: https://leetcode.com/problems/minimum-array-length-after-pair-removals

"""
    This is a very interesting question!

    I struggled a lot with this question and gave up on it after some time. I've just come up with the solution today
    after coming back from a coffeeshop after drinking coffee while reading "Deep Work" by Cal Newport.

    The trick with this question is: you have to minimise cases when you have a row of distinct numbers. Those are the ones
    which make the length of nums larger after the operations.

    So, process the array, and, when processing each number, take the most frequent number which is greater than it. Use a
    heap to efficiently find which is the most frequent number.

    Then, TADA!
"""


class Solution:
    def build_frequency_dict(self, nums: List[int]):
        frequency_dict = {}
        for num in nums:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1

        return frequency_dict

    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        frequency_dict = self.build_frequency_dict(nums)
        num_freq_array = frequency_dict.items()

        heap = []
        for [num, freq] in num_freq_array:
            heapq.heappush(heap, (-1*freq, num))

        result = 0
        for [num, dummy] in num_freq_array:
            freq = frequency_dict[num]
            for remaining in range(freq, 0, -1):
                if not heap:
                    result = result + remaining
                    return result

                (negative_maximum_frequency, most_frequent_num) = heapq.heappop(heap)
                while most_frequent_num <= num:
                    if not heap:
                        result = result + remaining
                        return result
                
                    (negative_maximum_frequency, most_frequent_num) = heapq.heappop(heap)

                maximum_frequency = (-1) * negative_maximum_frequency
                if maximum_frequency > 1:
                    maximum_frequency = maximum_frequency - 1
                    heapq.heappush(heap, (-1 * maximum_frequency, most_frequent_num))
                
                if frequency_dict[most_frequent_num] >= 1:
                    frequency_dict[most_frequent_num] = frequency_dict[most_frequent_num] - 1

        return result
