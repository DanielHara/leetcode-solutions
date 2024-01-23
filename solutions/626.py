"""
Question 608: https://leetcode.com/problems/exchange-seats/
"""

"""
Not a difficult question, just do it
"""

# Write your MySQL query statement below

SELECT id, (IF(id % 2 != 0, 
    IFNULL((SELECT student FROM Seat s1 WHERE s1.id = s2.id + 1), (SELECT student FROM Seat s1 WHERE s1.id = s2.id)),
    (SELECT student FROM Seat s1 WHERE s1.id = s2.id - 1)
) ) AS student FROM Seat s2

