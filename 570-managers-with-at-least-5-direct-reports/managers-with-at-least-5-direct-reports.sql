# Write your MySQL query statement below
SELECT mgr.name
FROM Employee e
JOIN Employee mgr
    ON mgr.id=e.managerId
GROUP BY mgr.id
HAVING COUNT(*)>=5