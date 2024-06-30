# Question 262: https://leetcode.com/problems/trips-and-users/

# Definitely not an elegant way of solving it, but today I am too lazy to look into this :/

# Write your MySQL query statement below

SELECT * FROM (
        SELECT ROUND(COUNT(T.id) / (
        SELECT COUNT(T2.id)  FROM Trips T2 INNER JOIN Users u1 ON u1.users_id = T2.client_id
        INNER JOIN Users u2 ON u2.users_id = T2.driver_id
        WHERE u1.banned = 'No' AND u2.banned = 'No' AND request_at = '2013-10-01'
    ), 2) AS `Cancellation Rate`, '2013-10-01' AS `Day` FROM Trips T
    INNER JOIN Users u1 ON u1.users_id = T.client_id
    INNER JOIN Users u2 ON u2.users_id = T.driver_id
    WHERE (status = 'cancelled_by_driver' OR status = 'cancelled_by_client') AND u1.banned = 'No' AND u2.banned = 'No' AND request_at = '2013-10-01'
    UNION
    SELECT ROUND(COUNT(T.id) / (
        SELECT COUNT(T2.id)  FROM Trips T2 INNER JOIN Users u1 ON u1.users_id = T2.client_id
        INNER JOIN Users u2 ON u2.users_id = T2.driver_id
        WHERE u1.banned = 'No' AND u2.banned = 'No' AND request_at = '2013-10-02'
    ), 2) AS `Cancellation Rate`, '2013-10-02' AS `Day` FROM Trips T
    INNER JOIN Users u1 ON u1.users_id = T.client_id
    INNER JOIN Users u2 ON u2.users_id = T.driver_id
    WHERE (status = 'cancelled_by_driver' OR status = 'cancelled_by_client') AND u1.banned = 'No' AND u2.banned = 'No' AND request_at = '2013-10-02'
    UNION
    SELECT ROUND(COUNT(T.id) / (
        SELECT COUNT(T2.id)  FROM Trips T2 INNER JOIN Users u1 ON u1.users_id = T2.client_id
        INNER JOIN Users u2 ON u2.users_id = T2.driver_id
        WHERE u1.banned = 'No' AND u2.banned = 'No' AND request_at = '2013-10-03'
    ), 2) AS `Cancellation Rate`, '2013-10-03' AS `Day` FROM Trips T
    INNER JOIN Users u1 ON u1.users_id = T.client_id
    INNER JOIN Users u2 ON u2.users_id = T.driver_id
    WHERE (status = 'cancelled_by_driver' OR status = 'cancelled_by_client') AND u1.banned = 'No' AND u2.banned = 'No' AND request_at = '2013-10-03'
) Table1 WHERE Table1.`Cancellation Rate` IS NOT NULL
