select query_name, 
       round(avg(rating/position), 2) as quality,  
       round(avg(IF(rating < 3, 1, 0)) * 100, 2) AS poor_query_percentage
FROM Queries
WHERE query_name IS NOT NULL
GROUP BY query_name;
