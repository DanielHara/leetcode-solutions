# Question 601: https://leetcode.com/problems/human-traffic-of-stadium/description/

# Nothing fancy, very similar to question https://leetcode.com/problems/consecutive-numbers/

# Write your MySQL query statement below

SELECT DISTINCT num as ConsecutiveNums
FROM Logs l1

WHERE ( 
    (
        ((SELECT l2.num FROM Logs l2 WHERE l2.id = l1.id - 1 AND l2.num = l1.num) IS NOT NULL)
            AND 
        ((SELECT l2.num FROM Logs l2 WHERE l2.id = l1.id + 1 AND l2.num = l1.num) IS NOT NULL)
    )
    OR
    (
        ((SELECT l2.num FROM Logs l2 WHERE l2.id = l1.id - 2 AND l2.num = l1.num) IS NOT NULL)
            AND 
        ((SELECT l2.num FROM Logs l2 WHERE l2.id = l1.id - 1 AND l2.num = l1.num) IS NOT NULL)
    )
    OR
    (
        ((SELECT l2.num FROM Logs l2 WHERE l2.id = l1.id + 1 AND l2.num = l1.num) IS NOT NULL)
            AND 
        ((SELECT l2.num FROM Logs l2 WHERE l2.id = l1.id + 2 AND l2.num = l1.num) IS NOT NULL)
    )
)
