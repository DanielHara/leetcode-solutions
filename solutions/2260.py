# Question 2260: https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

"""
    Quite a trivial question, should be Easy, and not Medium
"""

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        value_to_indexes = {}

        for index, card in enumerate(cards):
            if card not in value_to_indexes:
                value_to_indexes[card] = []

            value_to_indexes[card].append(index)

        result = None
        for indexes in value_to_indexes.values():
            for i in range(0, len(indexes) - 1, 1):
                possibility = indexes[i + 1] - indexes[i] + 1
                result = possibility if result is None else min(result, possibility)

        return result if result is not None else -1
