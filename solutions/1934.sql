# Question 1934: hhttps://leetcode.com/problems/confirmation-rate/

# No secrets, just use a few joins

# Write your MySQL query statement below

SELECT S.user_id, IFNULL(Table3.confirmation_rate, 0) AS confirmation_rate FROM Signups S
    LEFT JOIN
(
    SELECT Table1.user_id, ROUND(number_confirmations / number_actions, 2) AS confirmation_rate FROM (
    (SELECT C1.user_id, COUNT(C1.action) AS number_confirmations FROM Confirmations C1 WHERE C1.action = 'confirmed' GROUP BY C1.user_id) Table1
        LEFT JOIN
    (SELECT C2.user_id, COUNT(C2.action) AS number_actions FROM Confirmations C2 GROUP BY C2.user_id) Table2
        ON Table1.user_id = Table2.user_id
    )
) Table3
ON S.user_id = Table3.user_id
