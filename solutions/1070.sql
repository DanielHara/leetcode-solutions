# Question 1070: https://leetcode.com/problems/product-sales-analysis-iii/
# Kinda similar solution to question 550: https://leetcode.com/problems/game-play-analysis-iv/

# Write your MySQL query statement below

SELECT S1.product_id, S1.year AS first_year, S1.quantity, S1.price FROM Sales S1
WHERE (
    SELECT COUNT(S1.product_id) FROM (
        SELECT S2.product_id, MIN(S2.year) AS min_year FROM Sales S2 GROUP BY S2.product_id
    ) S3 WHERE S1.product_id = S3.product_id AND S1.year = S3.min_year
) > 0
