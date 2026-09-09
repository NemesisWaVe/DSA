# Write your MySQL query statement below
SELECT customer_id
FROM Customer
group by customer_id
having COUNT(DISTINCT product_key)= (SELECT Count(*) from Product)