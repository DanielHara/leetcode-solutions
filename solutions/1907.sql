# Question 1907: https://leetcode.com/problems/count-salary-categories/

# Trivial question

# Write your MySQL query statement below

SELECT 'Low Salary' AS category, COUNT(income) AS accounts_count FROM Accounts WHERE income < 20000
UNION
SELECT 'Average Salary' AS category, COUNT(income) AS accounts_count  FROM Accounts WHERE income >= 20000 AND income <= 50000
UNION
SELECT 'High Salary' AS category, COUNT(income) AS accounts_count  FROM Accounts WHERE income > 50000
