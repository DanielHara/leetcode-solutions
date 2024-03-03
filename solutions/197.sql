# Write your MySQL query statement below

# Just do it

SELECT W1.id FROM Weather W1 WHERE W1.temperature > (
    SELECT W2.temperature FROM Weather W2 WHERE DATE_ADD(W2.recordDate, INTERVAL 1 DAY) = W1.recordDate
)
