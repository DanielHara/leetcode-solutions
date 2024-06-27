/*
    Question 1164: https://leetcode.com/problems/product-price-at-a-given-date/
    Nice question to refresh my mind about RIGHT and LEFT JOIN
*/


/* Write your T-SQL query statement below */

SELECT final_product_id AS product_id, new_price As price FROM (
    (SELECT P2.product_id AS final_product_id, P2.new_price, P2.change_date FROM Products P2) Table2
        RIGHT JOIN
    (SELECT P1.product_id, MAX(P1.change_date) AS max_change_date FROM Products P1 WHERE P1.change_date <= '2019-08-16' GROUP BY P1.product_id) Table1
        ON Table1.product_id = Table2.final_product_id AND Table1.max_change_date = Table2.change_date
) UNION
SELECT P3.product_id, 10 AS Price FROM Products P3 GROUP BY P3.product_id HAVING MIN(P3.change_date) > '2019-08-16'
