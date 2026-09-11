# Write your MySQL query statement below
WITH rankedSalary AS(SELECT e.name AS Employee,d.name AS Department,salary as Salary,
        DENSE_RANK() OVER(PARTITION BY d.name ORDER BY e.salary desc) as rnk
FROM Employee e
JOIN Department d ON e.departmentId=d.id)
SELECT Employee,Department,Salary
FROM rankedSalary
WHERE rnk=1
