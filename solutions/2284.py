# Question 2284: https://leetcode.com/problems/sender-with-largest-word-count/

"""
    Just do it, quite easy question. Why is it rated as Medium?
"""

from functools import cmp_to_key

class Solution:
    def comparison(self, item1, item2) -> int:
        if item1[1] > item2[1]:
            return 1
        if item1[1] < item2[1]:
            return -1
        if item1[0] > item2[0]:
            return 1
        if item1[0] < item2[0]:
            return -1
        return 0

    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        sender_2_word_count_dict = {}

        for index in range(len(messages)):
            message = messages[index]
            sender = senders[index]

            tokens = message.split(' ')
            sender_2_word_count_dict[sender] = sender_2_word_count_dict.get(sender, 0) + len(tokens)

        items = list(sender_2_word_count_dict.items())
        items.sort(key=cmp_to_key(self.comparison), reverse=True)

        return items[0][0]
