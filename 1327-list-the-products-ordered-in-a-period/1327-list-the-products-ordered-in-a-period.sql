SELECT 
    p.product_name, 
    sum(o.unit) AS unit
FROM Products p
JOIN Orders o
ON p.product_id = o.product_id
WHERE o.order_date LIKE '2020-02-%'
GROUP BY p.product_id
HAVING SUM(o.unit) >= 100

