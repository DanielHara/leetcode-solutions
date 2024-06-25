/* Questions 602: https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/

   Very interesting question. I decided to use SQL Server because it supports FULL OUTER JOIN :)
*/

/* Write your T-SQL query statement below */

SELECT TOP 1 ISNULL(id1, id2) as id, (ISNULL(number_accepters, 0) + ISNULL(number_requesters, 0)) AS num FROM (
    (SELECT RA1.requester_id as id1, COUNT(RA1.accepter_id) as number_accepters FROM RequestAccepted RA1 GROUP BY RA1.requester_id) Table1
        FULL OUTER JOIN
    (SELECT RA2.accepter_id as id2, COUNT(RA2.requester_id) as number_requesters FROM RequestAccepted RA2 GROUP BY RA2.accepter_id) Table2
        ON Table1.id1 = Table2.id2
) ORDER BY num DESC
