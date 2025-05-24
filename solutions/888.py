# Question 888: https://leetcode.com/problems/fair-candy-swap/

"""
    Really nice warm-up question
"""

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        total_alice = sum(aliceSizes)
        total_bob = sum(bobSizes)

        bob_set = set(bobSizes)

        for aliceSize in aliceSizes:
            # Alice will have total_alice - aliceSize + bobSize
            # Bob will have total_bob + aliceSize - bobSize
            # So, we want to check if total_alice - aliceSize + bobSize == total_bob + aliceSize - bobSize, that is:
            # 2 * bobSize == total_bob + 2 * aliceSize - total_alice
            if (total_bob + 2 * aliceSize - total_alice) % 2 == 0:
                bobSize = (total_bob + 2 * aliceSize - total_alice) // 2
                if bobSize in bob_set:
                    return [aliceSize, bobSize]
