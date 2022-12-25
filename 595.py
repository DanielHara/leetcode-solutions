"""
Question 595: https://leetcode.com/problems/big-countries
"""

# Write your MySQL query statement below
# Trivial question, part of day 1 of the SQL study plan

SELECT name, population, area FROM World WHERE area >= 3000000 OR population >= 25000000
