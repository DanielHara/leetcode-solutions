# Question 1068: https://leetcode.com/problems/product-sales-analysis-i/
# Very easy warm-up question

# Write your MySQL query statement below
SELECT price, year, P.product_name from Sales S INNER JOIN Product P ON S.product_id = P.product_id
