/* Question 1211: https://leetcode.com/problems/queries-quality-and-percentage/

   No secret, just do it. The last test case is really weird, because it has rows where query_name is NULL
*/

# Write your MySQL query statement below

SELECT Q1.query_name, ROUND(AVG(Q1.rating / Q1.position), 2) AS quality, ROUND(
     (SELECT 100 * COUNT(Q3.query_name) FROM Queries Q3 WHERE Q3.rating < 3 AND Q3.query_name = Q1.query_name) / (SELECT COUNT(Q2.query_name) FROM Queries Q2 WHERE Q2.query_name = Q1.query_name), 2
) AS poor_query_percentage FROM Queries Q1 GROUP BY Q1.query_name HAVING Q1.query_name IS NOT NULL
