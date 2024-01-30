"""
    Question 1629: https://leetcode.com/problems/slowest-key/

    A trivial question, just do it
"""

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longest_duration = None
        answer = None

        for i in range(len(releaseTimes)):
            duration = releaseTimes[i] - (releaseTimes[i - 1] if i - 1 >= 0 else 0)
            keyPressed = keysPressed[i]

            if longest_duration is None or longest_duration < duration or (longest_duration == duration and answer < keyPressed):
                longest_duration = duration
                answer = keyPressed
        
        return answer
