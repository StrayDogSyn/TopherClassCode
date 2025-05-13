
.headers on
.mode column

-- SOLUTION 1: Weather Station Summary
.print "\n--- SOLUTION 1: Weather Station Summary ---"
SELECT 
    ws.station_name,
    l.city,
    ROUND(AVG(wr.temperature), 1) AS avg_temperature,
    ROUND(SUM(wr.precipitation), 1) AS total_precipitation
FROM weather_stations ws
JOIN locations l ON ws.location_id = l.location_id
JOIN weather_readings wr ON ws.station_id = wr.station_id
GROUP BY ws.station_id
ORDER BY avg_temperature DESC;

-- SOLUTION 2: Find the Hottest and Coldest Cities
.print "\n--- SOLUTION 2: Find the Hottest and Coldest Cities ---"
SELECT 
    l.city,
    l.state,
    ROUND(AVG(wr.temperature), 1) AS avg_temperature
FROM locations l
JOIN weather_stations ws ON l.location_id = ws.location_id
JOIN weather_readings wr ON ws.station_id = wr.station_id
GROUP BY l.city, l.state
ORDER BY avg_temperature DESC;

-- SOLUTION 3: Comparing Cities
.print "\n--- SOLUTION 3: Comparing Cities ---"
SELECT 
    l.city,
    ROUND(AVG(wr.temperature), 1) AS avg_temperature,
    ROUND(AVG(wr.humidity), 1) AS avg_humidity,
    ROUND(SUM(wr.precipitation), 1) AS total_precipitation
FROM locations l
JOIN weather_stations ws ON l.location_id = ws.location_id
JOIN weather_readings wr ON ws.station_id = wr.station_id
WHERE l.city IN ('New York', 'Los Angeles')
GROUP BY l.city;

-- SOLUTION 4: Rainy Day Detector
.print "\n--- SOLUTION 4: Rainy Day Detector ---"
SELECT 
    l.city,
    wr.reading_date,
    wr.precipitation AS rainfall
FROM weather_readings wr
JOIN weather_stations ws ON wr.station_id = ws.station_id
JOIN locations l ON ws.location_id = l.location_id
WHERE wr.precipitation > 5
ORDER BY rainfall DESC;

-- BONUS SOLUTION: Temperature Anomalies
.print "\n--- BONUS SOLUTION: Temperature Anomalies ---"
.print "This finds days that were much hotter or colder than average for that city"
SELECT 
    l.city,
    wr.reading_date,
    wr.temperature,
    city_avg.avg_temp,
    ROUND(wr.temperature - city_avg.avg_temp, 1) AS temp_difference
FROM weather_readings wr
JOIN weather_stations ws ON wr.station_id = ws.station_id
JOIN locations l ON ws.location_id = l.location_id
JOIN (
    SELECT 
        l2.city,
        AVG(wr2.temperature) AS avg_temp
    FROM weather_readings wr2
    JOIN weather_stations ws2 ON wr2.station_id = ws2.station_id
    JOIN locations l2 ON ws2.location_id = l2.location_id
    GROUP BY l2.city
) city_avg ON l.city = city_avg.city
WHERE ABS(wr.temperature - city_avg.avg_temp) > 5
ORDER BY ABS(wr.temperature - city_avg.avg_temp) DESC;

-- Explanation for instructors:
-- Solution 1: Shows how to combine JOIN with GROUP BY and aggregation functions
-- Solution 2: Similar to #1 but focuses on ranking by temperature
-- Solution 3: Introduces filtering specific records with WHERE IN
-- Solution 4: Shows more advanced filtering with conditionals
-- Bonus: Demonstrates a more complex query with a subquery for comparison