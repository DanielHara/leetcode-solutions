/*
    Question 3220: https://leetcode.com/problems/odd-and-even-transactions/

    Just use a join, nothing fancy
*/

/* Write your T-SQL query statement below */

SELECT ISNULL(T3.transaction_date, T4.transaction_date) AS transaction_date, ISNULL(T4.odd_sum, 0) AS odd_sum, ISNULL(T3.even_sum, 0) AS even_sum FROM
(SELECT SUM(T1.amount) as even_sum , T1.transaction_date FROM transactions T1 WHERE T1.amount % 2 = 0 GROUP BY T1.transaction_date) T3
FULL OUTER JOIN
(SELECT SUM(T2.amount) AS odd_sum, T2.transaction_date FROM transactions T2 WHERE T2.amount % 2 != 0 GROUP BY T2.transaction_date) T4
ON T3.transaction_date = T4.transaction_date ORDER BY transaction_date
