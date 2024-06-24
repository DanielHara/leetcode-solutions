# Question 550: https://leetcode.com/problems/game-play-analysis-iv/

# Nothing fancy, just use an auxiliary query

# Write your MySQL query statement below

SELECT ROUND(COUNT(DISTINCT A2.player_id) / (SELECT COUNT(DISTINCT A4.player_id) FROM Activity A4), 2) AS fraction FROM Activity A2
WHERE (
    SELECT COUNT(A3.player_id) FROM (
        SELECT A1.player_id, MIN(A1.event_date) AS min_event_date FROM Activity A1 GROUP BY A1.player_id
    ) A3 WHERE DATE_SUB(A2.event_date, INTERVAL 1 DAY) = A3.min_event_date AND A2.player_id = A3.player_id
) > 0
