# Write your MySQL query statement below
WITH DailySpend AS (SELECT 
    visited_on,
    SUM(amount) AS daily_amount
FROM Customer
GROUP BY visited_on),
RollingStats AS (
    SELECT visited_on,
            SUM(daily_amount) OVER(
                order by visited_on
                ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
            ) AS amount,
            ROUND(AVG(daily_amount) OVER(order by visited_on
                                    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)
                                    ,2) as average_amount
            
    FROM DailySpend)
SELECT visited_on,
        amount,average_amount
FROM RollingStats
WHERE visited_on>=(
    SELECT DATE_ADD(MIN(visited_on),INTERVAL 6 DAY)
    FROM Customer
)
order by visited_on asc


