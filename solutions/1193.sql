/*
    Question 1193: https://leetcode.com/problems/monthly-transactions-i/

    Sometimes the testcases include country: null, which is weird
*/

/* Write your T-SQL query statement below */

SELECT Table1.country, CONCAT(YEAR(Table1.month), '-', FORMAT(Month(Table1.month), '00'))  As month, ISNULL(trans_total_amount, 0) AS trans_total_amount, ISNULL(trans_count, 0) AS trans_count, ISNULL(approved_total_amount, 0) AS approved_total_amount, ISNULL(approved_count, 0)  AS approved_count FROM (
    (SELECT SUM(amount) AS trans_total_amount, country, DATEFROMPARTS(Year(trans_date), Month(trans_date), 1) AS month, COUNT(trans_date) AS trans_count FROM Transactions GROUP BY DATEFROMPARTS(Year(trans_date), Month(trans_date), 1), country) Table1
        LEFT JOIN
    (SELECT SUM(T1.amount) AS approved_total_amount, T1.country, DATEFROMPARTS(Year(T1.trans_date), Month(T1.trans_date), 1) As month, COUNT(T1.trans_date) AS approved_count FROM Transactions T1 WHERE T1.state = 'approved' GROUP BY DATEFROMPARTS(Year(T1.trans_date), Month(T1.trans_date), 1), T1.country) Table2
    ON Table1.month = Table2.month AND Table1.month IS NOT NULL AND ISNULL(Table1.country, 'null') = ISNULL(Table2.country, 'null')
)
