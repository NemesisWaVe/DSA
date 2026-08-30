# Write your MySQL query statement below
SELECT mgr.name
FROM Employee emp
JOIN Employee mgr
    ON emp.managerID=mgr.id
GROUP BY mgr.id,mgr.name
HAVING COUNT(emp.id)>=5;