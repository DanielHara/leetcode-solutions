/* Questions 1158: https://leetcode.com/problems/market-analysis-i/

   No secret, just use a LEFT JOIN
*/

/* Write your T-SQL query statement below */

SELECT user_id as buyer_id, join_date, ISNULL(orders_in_2019, 0) as orders_in_2019 FROM (
    (SELECT user_id, join_date FROM Users) Table1
        LEFT JOIN 
    (SELECT COUNT(DISTINCT order_id) AS orders_in_2019, buyer_id FROM Orders WHERE Year(order_date) = 2019 GROUP BY buyer_id) Table2
        ON Table1.user_id = Table2.buyer_id
)
