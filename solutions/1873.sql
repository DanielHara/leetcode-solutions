# Question 1873: https://leetcode.com/problems/calculate-special-bonus/description/

# Trivial SQL question
SELECT employee_id,  (IF(name NOT LIKE 'M%' AND employee_id % 2 != 0, salary, 0)) AS bonus FROM Employees ORDER BY employee_id
