# Write your MySQL query statement below
SELECT MAX(salary) AS secondHighestSalary
FROM Employee
WHERE salary<(SELECT MAX(Salary) FROM Employee)