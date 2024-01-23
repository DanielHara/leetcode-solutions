# Question 970: https://leetcode.com/problems/powerful-integers/description/

# Not a difficult question, set the boundaries and use brute-force.

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound <= 0:
            return []

        if x == 1 and y == 1:
            return [2] if bound >= 2 else []

        if y == 1:
            temp = y
            y = x
            x = temp

        if x == 1:
            bound_y = math.floor(math.log(bound, y))

            answers = set()

            result = 0
            for j in range(bound_y + 1):
                element = y ** j + 1

                if element <= bound:
                    answers.add(element)
            
            return list(answers)

        bound_x = math.floor(math.log(bound, x))
        bound_y = math.floor(math.log(bound, y))
        answers = set()

        result = 0
        for i in range(bound_x + 1):
            for j in range(bound_y + 1):
                element = x ** i + y ** j
                if element <= bound:
                    answers.add(element)

        return list(answers)
