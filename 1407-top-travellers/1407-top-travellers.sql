SELECT 
    users.name,
    IF(SUM(rides.distance) IS NULL, 0, SUM(rides.distance)) AS travelled_distance
FROM users
LEFT JOIN rides
    ON users.id = rides.user_id
GROUP BY users.id, users.name
ORDER BY travelled_distance DESC, users.name;