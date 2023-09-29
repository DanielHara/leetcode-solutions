# Question 2225: https://leetcode.com/problems/find-players-with-zero-or-one-losses/

"""
    Just do it, quite easy question. I'm wondering why it's tagged as Medium
"""

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        set_players = set()
        frequency_losses = {}

        for [winner, loser] in matches:
            set_players.add(winner)
            set_players.add(loser)

            frequency_losses[loser] = frequency_losses.get(loser, 0) + 1
        
        not_lost_any_matches = []
        lost_exactly_one_match = []
        for player in set_players:
            if player not in frequency_losses:
                not_lost_any_matches.append(player)
            elif frequency_losses[player] == 1:
                lost_exactly_one_match.append(player)
        
        not_lost_any_matches.sort()
        lost_exactly_one_match.sort()
        
        return [not_lost_any_matches, lost_exactly_one_match]
