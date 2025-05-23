# Write your MySQL query statement below
SELECT 
    s.product_id,
    p.product_name
FROM Sales s
LEFT JOIN Product p 
ON s.product_id = p.product_id
GROUP BY s.product_id
HAVING MIN(s.sale_date) >= CAST('2019-01-01' AS DATE) AND MAX(s.sale_date) <= CAST('2019-03-31' AS DATE);
