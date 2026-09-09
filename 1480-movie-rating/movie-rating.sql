# Write your MySQL query statement below
(SELECT u.name as results
FROM MovieRating mr
JOIN Users u ON mr.user_id=u.user_id
GROUP BY u.user_id
ORDER BY COUNT(*) DESC,u.name ASC
limit 1)
UNION ALL
(SELECT m.title as results
FROM MovieRating mr
JOIN Movies m ON mr.movie_id=m.movie_id
WHERE mr.created_at>='2020-02-01' AND mr.created_at<='2020-02-29'
GROUP BY m.title
ORDER BY AVG(mr.rating) desc,m.title ASC
limit 1)