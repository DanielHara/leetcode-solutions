# Question 1823: https://leetcode.com/problems/find-the-winner-of-the-circular-game/

"""
    Just follow the prompt. The constraints 1 <= k <= n <= 500 hint on the fact that a O(N**2) would be fine.
"""

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [friend for friend in range(1, n + 1)]

        index_friend = 0
        while len(friends) > 1:
            remove_friend_index = (index_friend + k - 1) % len(friends)
            friends.pop(remove_friend_index)

            index_friend = remove_friend_index
        
        return friends[0]
