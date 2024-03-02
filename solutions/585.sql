# Write your MySQL query statement below

# Not a difficult question, just do it

SELECT ROUND(SUM(tiv_2016), 2) AS 'tiv_2016' FROM Insurance I1 WHERE (
    SELECT COUNT(I2.pid) FROM Insurance I2 WHERE I2.tiv_2015 = I1.tiv_2015 AND I1.pid != I2.pid
) > 0 AND (
    SELECT COUNT(I2.pid) FROM Insurance I2 WHERE I2.lat = I1.lat AND I2.lon = I1.lon AND I1.pid != I2.pid
) = 0
