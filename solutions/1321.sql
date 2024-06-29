/* Question 1321: https://leetcode.com/problems/restaurant-growth/description/

   No secret, just do it.
*/

# Write your MySQL query statement below

SELECT Table1.visited_on, Table1.sum_amount as amount, ROUND(Table1.sum_amount / 7, 2) AS average_amount FROM (
    SELECT C1.visited_on, (
        SELECT SUM(C2.amount) FROM Customer C2 WHERE C2.visited_on > DATE_SUB(C1.visited_on, INTERVAL 7 DAY) AND C2.visited_on <= C1.visited_on 
            ) AS sum_amount, (
        SELECT COUNT(C3.visited_on) FROM Customer C3 WHERE C3.visited_on = DATE_SUB(C1.visited_on, INTERVAL 6 DAY)
    ) > 0 AS include
    FROM Customer C1 GROUP BY C1.visited_on
) Table1 WHERE Table1.include = 1
