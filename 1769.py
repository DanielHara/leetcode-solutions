# Question 1769: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box

# Use dynamic programming to do the trick

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        S = []
        for box in boxes:
            S.append((S[-1] if S else 0) + (1 if box == '1' else 0))
        
        T = [None for i in range(len(boxes))]
        for i in range(len(boxes) - 1, -1, -1):
            T[i] = (T[i + 1] if i + 1 < len(boxes) else 0) + (1 if boxes[i] == '1' else 0)
        
        answer = [None for i in range(len(boxes))]

        last_answer = 0
        for index, box in enumerate(boxes):
            if box == '1' and index < len(boxes) - 1:
                last_answer = last_answer + len(boxes) - index - 1

        answer[len(boxes) - 1] = last_answer
        for i in range(len(boxes) - 2, -1, -1):
            answer[i] = answer[i + 1] - S[i] + T[i + 1]
        
        return answer
