# Question 1045: https://leetcode.com/problems/customers-who-bought-all-products/

# Just use GROUP BY

# Write your MySQL query statement below

SELECT customer_id
FROM (
    SELECT C1.customer_id, COUNT(DISTINCT(C1.product_key)) AS count_distinct_products FROM Customer C1 GROUP BY C1.customer_id
) Table1
WHERE count_distinct_products = (SELECT COUNT(DISTINCT(P.product_key)) FROM Product P)

