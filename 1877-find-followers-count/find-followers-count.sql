# Write your MySQL query statement below
Select user_id,COUNT(follower_id) as followers_count
from Followers
group by user_id
order by user_id ASC