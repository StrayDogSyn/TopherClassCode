-- Subquery in SELECT clause
SELECT 
    l.city,
    (SELECT AVG(temperature) 
     FROM weather_readings wr
     JOIN weather_stations ws ON wr.station_id = ws.station_id
     WHERE ws.location_id = l.location_id) AS avg_temp
FROM locations l;

-- Subquery in WHERE clause
SELECT l.city, l.state
FROM locations l
WHERE l.location_id IN (
    SELECT ws.location_id
    FROM weather_stations ws
    JOIN weather_readings wr ON ws.station_id = wr.station_id
    GROUP BY ws.location_id
    HAVING AVG(wr.temperature) > 25
);