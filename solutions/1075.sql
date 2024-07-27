# Question 1075: https://leetcode.com/problems/project-employees-i/
# Trivial question, just do it

# Write your MySQL query statement below

SELECT Project.project_id, ROUND(AVG(Employee.experience_years), 2) as average_years  FROM PROJECT LEFT JOIN Employee ON Project.employee_id = Employee.employee_id GROUP BY project_id
