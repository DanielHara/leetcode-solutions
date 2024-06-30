"""
    Question 2410: https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/

    This question is very similar to question 2592: https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/
"""

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        player_index = 0
        trainer_index = 0

        result = 0
        while player_index < len(players):
            while trainer_index < len(trainers) and trainers[trainer_index] < players[player_index]:
                trainer_index = trainer_index + 1
            
            if trainer_index < len(trainers):
                trainer_index = trainer_index + 1
                result = result + 1
            
            player_index = player_index + 1
        
        return result
