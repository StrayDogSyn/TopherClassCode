-- SQL Fundamentals Practice - Breakout #1
-- Instructions: For each query below:
-- 1. Identify what's wrong with the query
-- 2. Fix the query to make it work
-- 3. Explain why your solution corrects the issue

.headers on
.mode column
.width 40 40

.print "\n--- Query 1: Trying to join tables without a join condition ---"
-- Problem query:
SELECT l.city, ws.station_name
FROM locations l, weather_stations ws;

.print "\n--- Query 2: Selecting non-aggregated columns without grouping ---"
-- Problem query:
SELECT city, AVG(temperature)
FROM weather_readings wr
JOIN weather_stations ws ON wr.station_id = ws.station_id
JOIN locations l ON ws.location_id = l.location_id;

.print "\n--- Query 3: Using a column name that doesn't exist ---"
-- Problem query:
SELECT city, temperature, rainfall
FROM weather_readings wr
JOIN weather_stations ws ON wr.station_id = ws.station_id
JOIN locations l ON ws.location_id = l.location_id;

.print "\n--- Query 4: Incorrect subquery (returning multiple rows for a single-value context) ---"
-- Problem query:
SELECT city, state
FROM locations
WHERE location_id = (SELECT location_id FROM weather_stations);

.print "\n--- Query 5: Using GROUP BY incorrectly ---"
-- Problem query:
SELECT state, city, COUNT(*) as station_count
FROM locations l
JOIN weather_stations ws ON l.location_id = ws.location_id
GROUP BY state;

.print "\n--- SOLUTION AREA ---"
.print "\nAfter identifying the issues, write your fixed queries below:"
.print "\n1. Fixed Query 1:"
-- Your solution for Query 1
-- Example of correct solution:
-- SELECT l.city, ws.station_name
-- FROM locations l
-- INNER JOIN weather_stations ws ON l.location_id = ws.location_id;

.print "\n2. Fixed Query 2:"
-- Your solution for Query 2

.print "\n3. Fixed Query 3:"
-- Your solution for Query 3

.print "\n4. Fixed Query 4:"
-- Your solution for Query 4

.print "\n5. Fixed Query 5:"
-- Your solution for Query 5