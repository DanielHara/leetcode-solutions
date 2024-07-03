# Question 577: https://leetcode.com/problems/employee-bonus/

# Trivial question, just a table join

# Write your MySQL query statement below

SELECT name, bonus FROM (
    Employee E
        LEFT JOIN
    Bonus B
    ON E.empId = B.empId
) HAVING bonus IS NULL OR bonus < 1000
