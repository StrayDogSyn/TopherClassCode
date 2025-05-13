-- Solution 1: Add proper join condition
SELECT l.city, ws.station_name
FROM locations l
INNER JOIN weather_stations ws ON l.location_id = ws.location_id;

-- Solution 2: Add GROUP BY clause for non-aggregated column
SELECT city, AVG(temperature)
FROM weather_readings wr
JOIN weather_stations ws ON wr.station_id = ws.station_id
JOIN locations l ON ws.location_id = l.location_id
GROUP BY city;

-- Solution 3: Use correct column name (precipitation instead of rainfall)
SELECT city, temperature, precipitation
FROM weather_readings wr
JOIN weather_stations ws ON wr.station_id = ws.station_id
JOIN locations l ON ws.location_id = l.location_id;

-- Solution 4: Use IN operator instead of = for multi-row subquery
SELECT city, state
FROM locations
WHERE location_id IN (SELECT location_id FROM weather_stations);

-- Solution 5: Include all non-aggregated columns in GROUP BY
SELECT state, city, COUNT(*) as station_count
FROM locations l
JOIN weather_stations ws ON l.location_id = ws.location_id
GROUP BY state, city;