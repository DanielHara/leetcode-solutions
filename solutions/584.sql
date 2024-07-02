# Question 584: https://leetcode.com/problems/find-customer-referee/

# Trivial question

# Write your MySQL query statement below
SELECT name FROM Customer WHERE referee_id IS NULL OR referee_id != 2
