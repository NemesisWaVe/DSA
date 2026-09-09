# Write your MySQL query statement below
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag='Y'

UNION

SELECT employee_id,department_id
FROM Employee
group by employee_id
HAVING COUNT(department_id)=1