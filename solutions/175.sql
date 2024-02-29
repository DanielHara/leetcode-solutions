# Write your MySQL query statement below

# Very easy question. Just remember the difference between INNER JOIN, LEFT JOIN and RIGHT JOIN

SELECT Person.firstName, Person.lastName, Address.city, Address.state FROM Person LEFT JOIN Address ON Person.personId = Address.personId
