# Write your MySQL query statement below

# Write your MySQL query statement below

SELECT e1.name FROM Employee e1 WHERE (
    (SELECT COUNT(e2.id) FROM Employee e2 WHERE e2.managerId = e1.id) >= 5
)
