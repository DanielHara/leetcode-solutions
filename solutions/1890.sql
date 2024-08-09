# Question 1890: https://leetcode.com/problems/the-latest-login-in-2020/

# Trivial question

# Write your MySQL query statement below

SELECT user_id, MAX(time_stamp) AS last_stamp FROM Logins WHERE Year(time_stamp) = 2020 GROUP BY user_id
