-- SQL Fundamentals Practice - Breakout #1
-- Instructions: For each query below:
-- 1. Identify what's wrong with the query
-- 2. Fix the query to make it work
-- 3. Explain why your solution corrects the issue

.headers on
.mode column
.width 40 40

.print "\n--- Query 1: Trying to join tables without a join condition ---"
-- PROBLEM: This query uses comma-separated table syntax without a WHERE clause
-- This creates a CARTESIAN PRODUCT - every location paired with every station
-- Result: If you have 5 locations and 4 stations, you get 5×4=20 meaningless rows

-- Problem query (BROKEN):
-- SELECT l.city, ws.station_name
-- FROM locations l, weather_stations ws;

-- DEMONSTRATION: Let's see the cartesian product in action
.print "Cartesian Product Result (BROKEN):"
SELECT l.city, ws.station_name
FROM locations l, weather_stations ws;

.print "\n--- Query 2: Selecting non-aggregated columns without grouping ---"
-- PROBLEM: This query mixes aggregate functions (AVG) with non-aggregated columns (city)
-- SQL requires that when using aggregate functions, all non-aggregated columns 
-- must be included in the GROUP BY clause
-- Result: Database doesn't know how to group the data for aggregation

-- Problem query (BROKEN):
.print "Aggregate without GROUP BY (BROKEN):"
SELECT city, AVG(temperature)
FROM weather_readings wr
JOIN weather_stations ws ON wr.station_id = ws.station_id
JOIN locations l ON ws.location_id = l.location_id;

.print "\n--- Query 3: Using a column name that doesn't exist ---"
-- PROBLEM: The query references 'rainfall' column which doesn't exist in the database schema
-- The weather_readings table has 'precipitation' column, not 'rainfall'
-- Result: SQL error - "no such column: rainfall"

-- Problem query (BROKEN):
.print "Non-existent column error (BROKEN):"
SELECT city, temperature, rainfall
FROM weather_readings wr
JOIN weather_stations ws ON wr.station_id = ws.station_id
JOIN locations l ON ws.location_id = l.location_id;

.print "\n--- Query 4: Incorrect subquery (returning multiple rows for a single-value context) ---"
-- PROBLEM: The subquery returns multiple rows (multiple location_ids from weather_stations),
-- but the WHERE clause expects a single value when using the = operator.
-- Result: SQL error - "subquery returned more than 1 row"

-- Problem query (BROKEN):
.print "Multiple row subquery error (BROKEN):"
SELECT city, state
FROM locations
WHERE location_id = (SELECT location_id FROM weather_stations);

.print "\n--- Query 5: Using GROUP BY incorrectly ---"
-- PROBLEM: The query groups by 'state' only but selects both 'state' and 'city' columns.
-- When using GROUP BY, all non-aggregated columns in SELECT must be in the GROUP BY clause.
-- The current query would randomly pick one city per state, which is not deterministic.
-- Result: Inconsistent results and potential SQL errors

-- Problem query (BROKEN):
.print "Incomplete GROUP BY (BROKEN):"
SELECT state, city, COUNT(*) as station_count
FROM locations l
JOIN weather_stations ws ON l.location_id = ws.location_id
GROUP BY state;

.print "\n--- SOLUTION AREA ---"
.print "\nAfter identifying the issues, write your fixed queries below:"

.print "\n1. Fixed Query 1:"
-- ISSUE: The original query uses comma-separated table syntax (FROM locations l, weather_stations ws)
-- without a WHERE clause to specify the join condition. This creates a CARTESIAN PRODUCT,
-- which returns every combination of rows from both tables (potentially thousands of rows).
-- SOLUTION: Use proper INNER JOIN syntax with ON clause to specify the relationship
SELECT l.city, ws.station_name
FROM locations l
INNER JOIN weather_stations ws ON l.location_id = ws.location_id;

.print "\n2. Fixed Query 2:"
-- ISSUE: The query selects both an aggregate function (AVG) and a non-aggregated column (city)
-- without using GROUP BY. SQL requires that when using aggregate functions, all non-aggregated
-- columns must be included in the GROUP BY clause.
-- SOLUTION: Add GROUP BY clause to group results by city, allowing proper aggregation
SELECT l.city, AVG(wr.temperature) as avg_temperature
FROM weather_readings wr
JOIN weather_stations ws ON wr.station_id = ws.station_id
JOIN locations l ON ws.location_id = l.location_id
GROUP BY l.city;

.print "\n3. Fixed Query 3:"
-- ISSUE: The query references 'rainfall' column which doesn't exist in the database schema.
-- The weather_readings table has 'precipitation' column, not 'rainfall'.
-- SOLUTION: Replace 'rainfall' with the correct column name 'precipitation'
SELECT l.city, wr.temperature, wr.precipitation
FROM weather_readings wr
JOIN weather_stations ws ON wr.station_id = ws.station_id
JOIN locations l ON ws.location_id = l.location_id;

.print "\n4. Fixed Query 4:"
-- ISSUE: The subquery returns multiple rows (multiple location_ids from weather_stations),
-- but the WHERE clause expects a single value when using the = operator.
-- SOLUTION: Use IN operator to handle multiple values, or use ANY/EXISTS for more complex logic
SELECT city, state
FROM locations
WHERE location_id IN (SELECT location_id FROM weather_stations);

-- Alternative solution using EXISTS (more efficient for large datasets):
-- SELECT city, state
-- FROM locations l
-- WHERE EXISTS (SELECT 1 FROM weather_stations ws WHERE ws.location_id = l.location_id);

.print "\n5. Fixed Query 5:"
-- ISSUE: The query groups by 'state' only but selects both 'state' and 'city' columns.
-- When using GROUP BY, all non-aggregated columns in SELECT must be in the GROUP BY clause.
-- The current query would randomly pick one city per state, which is not deterministic.
-- SOLUTION: Include 'city' in the GROUP BY clause to get station count per city per state
SELECT l.state, l.city, COUNT(*) as station_count
FROM locations l
JOIN weather_stations ws ON l.location_id = ws.location_id
GROUP BY l.state, l.city
ORDER BY l.state, l.city;

-- Alternative solution if you only want count per state (without city breakdown):
-- SELECT state, COUNT(*) as station_count
-- FROM locations l
-- JOIN weather_stations ws ON l.location_id = ws.location_id
-- GROUP BY state;

.print "\n--- SUMMARY OF COMMON SQL MISTAKES ---"
.print "\n1. CARTESIAN PRODUCT: Always use explicit JOIN syntax with ON conditions"
.print "2. AGGREGATION RULES: All non-aggregated columns must be in GROUP BY"
.print "3. SCHEMA AWARENESS: Verify column names exist in your database"
.print "4. SUBQUERY CARDINALITY: Use IN/EXISTS for multi-row subqueries"
.print "5. GROUP BY COMPLETENESS: Include all selected non-aggregated columns"