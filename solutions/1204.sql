# Question 1204: https://leetcode.com/problems/last-person-to-fit-in-the-bus/

# Not difficult, just do it

# Write your MySQL query statement below

SELECT person_name FROM (
    SELECT Q1.person_name, (
        SELECT SUM(Q2.weight) FROM Queue Q2 WHERE Q2.turn <= Q1.turn 
    ) AS total_weight FROM Queue Q1 HAVING total_weight <= 1000 ORDER BY Q1.turn DESC LIMIT 1
) Table1
