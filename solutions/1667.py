"""
Question 1667: https://leetcode.com/problems/fix-names-in-a-table/
"""

"""
Trivial question
"""

# Write your MySQL query statement below

SELECT user_id, CONCAT (UPPER(SUBSTRING(t1.name, 1, 1)), LOWER(SUBSTRING(t1.name, 2))) as name FROM Users t1 ORDER BY user_id
