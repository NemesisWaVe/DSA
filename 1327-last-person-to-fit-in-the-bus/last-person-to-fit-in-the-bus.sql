# Write your MySQL query statement below
SELECT person_name
FROM (SELECT 
        person_name,
        turn,
        SUM(weight) OVER (ORDER BY turn) AS total_weight
    FROM Queue) as cumulative_queue
WHERE total_weight<=1000
ORDER BY total_weight desc
limit 1 