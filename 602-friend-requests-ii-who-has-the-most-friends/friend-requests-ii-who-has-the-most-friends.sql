# Write your MySQL query statement below
WITH AllFriends AS(
    SELECT requester_id as id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id as id
    FROM RequestAccepted
)
SELECT id,
        COUNT(*) as num
FROM AllFriends
GROUP BY id
ORDER BY num DESC
LIMIT 1