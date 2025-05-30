.headers on
.mode column

-- Add some more data to make the exercise more interesting
INSERT OR IGNORE INTO locations (city, state, country, latitude, longitude)
VALUES 
('Miami', 'FL', 'USA', 25.7617, -80.1918),
('Seattle', 'WA', 'USA', 47.6062, -122.3321);

INSERT OR IGNORE INTO weather_stations (station_name, location_id, elevation)
VALUES 
('Miami Beach', 6, 0.9),
('Seattle Downtown', 7, 56.4);

INSERT OR IGNORE INTO weather_readings (station_id, temperature, humidity, pressure, precipitation, reading_date)
VALUES 
-- Miami (hot, humid, occasional heavy rain)
(5, 31.5, 85.0, 1010.1, 0.0, '2023-06-01'),
(5, 32.1, 87.5, 1009.8, 20.5, '2023-06-02'),
-- Seattle (cool, moderate humidity, light rain)
(6, 18.2, 68.0, 1012.5, 1.2, '2023-06-01'),
(6, 17.5, 72.0, 1011.8, 2.3, '2023-06-02');

-- First check that our data is there
.print "\n--- Checking our data ---"
.print "\nLocations:"
SELECT * FROM locations;

.print "\nWeather Stations:"
SELECT * FROM weather_stations;

.print "\nSome Weather Readings:"
SELECT * FROM weather_readings LIMIT 10;

.print "\n--- CHALLENGE 1: Weather Station Summary ---"
.print "Create a query that shows a summary of each weather station,"
.print "including the city it's in, average temperature, and total precipitation."

-- SOLUTION: Weather Station Summary
-- This query joins all three tables to connect weather readings with station info and location details
-- We use aggregate functions to calculate average temperature and total precipitation per station
SELECT 
    ws.station_name,
    l.city,
    l.state,
    ROUND(AVG(wr.temperature), 2) as avg_temperature,
    ROUND(SUM(wr.precipitation), 2) as total_precipitation,
    COUNT(wr.reading_id) as total_readings
FROM weather_stations ws
    INNER JOIN locations l ON ws.location_id = l.location_id
    INNER JOIN weather_readings wr ON ws.station_id = wr.station_id
GROUP BY ws.station_id, ws.station_name, l.city, l.state
ORDER BY avg_temperature DESC;

.print "\n--- CHALLENGE 2: Find the Hottest and Coldest Cities ---"
.print "Create a query that ranks cities by their average temperature,"
.print "showing the hottest and coldest cities."

-- SOLUTION: Hottest and Coldest Cities Ranking
-- This query aggregates temperature data by city and ranks them from hottest to coldest
-- We include additional metrics like min/max temperatures and reading count for context
SELECT 
    l.city,
    l.state,
    ROUND(AVG(wr.temperature), 2) as avg_temperature,
    ROUND(MIN(wr.temperature), 2) as min_temperature,
    ROUND(MAX(wr.temperature), 2) as max_temperature,
    COUNT(wr.reading_id) as reading_count,
    -- Add a ranking column to clearly show hottest (1) to coldest
    ROW_NUMBER() OVER (ORDER BY AVG(wr.temperature) DESC) as temperature_rank
FROM locations l
    INNER JOIN weather_stations ws ON l.location_id = ws.location_id
    INNER JOIN weather_readings wr ON ws.station_id = wr.station_id
GROUP BY l.city, l.state
ORDER BY avg_temperature DESC;

.print "\n--- CHALLENGE 3: Comparing Cities ---"
.print "Create a query that compares two specific cities (e.g., 'New York' and 'Los Angeles')"
.print "showing their average temperatures, humidity, and precipitation."

-- SOLUTION: City Comparison (New York vs Los Angeles)
-- This query filters for specific cities and provides a side-by-side comparison
-- Using WHERE with IN clause to select multiple specific cities
SELECT 
    l.city,
    l.state,
    ROUND(AVG(wr.temperature), 2) as avg_temperature,
    ROUND(AVG(wr.humidity), 2) as avg_humidity,
    ROUND(AVG(wr.pressure), 2) as avg_pressure,
    ROUND(SUM(wr.precipitation), 2) as total_precipitation,
    ROUND(AVG(wr.precipitation), 2) as avg_precipitation_per_reading,
    COUNT(wr.reading_id) as total_readings
FROM locations l
    INNER JOIN weather_stations ws ON l.location_id = ws.location_id
    INNER JOIN weather_readings wr ON ws.station_id = wr.station_id
WHERE l.city IN ('New York', 'Los Angeles')
GROUP BY l.city, l.state
ORDER BY l.city;

-- Alternative: Compare any two cities with UNION for side-by-side display
.print "\nAlternative comparison format:"
SELECT 'New York' as comparison_city, 
       ROUND(AVG(wr.temperature), 2) as avg_temp,
       ROUND(AVG(wr.humidity), 2) as avg_humidity
FROM locations l
    INNER JOIN weather_stations ws ON l.location_id = ws.location_id
    INNER JOIN weather_readings wr ON ws.station_id = wr.station_id
WHERE l.city = 'New York'
UNION ALL
SELECT 'Los Angeles' as comparison_city,
       ROUND(AVG(wr.temperature), 2) as avg_temp,
       ROUND(AVG(wr.humidity), 2) as avg_humidity
FROM locations l
    INNER JOIN weather_stations ws ON l.location_id = ws.location_id
    INNER JOIN weather_readings wr ON ws.station_id = wr.station_id
WHERE l.city = 'Los Angeles';

.print "\n--- CHALLENGE 4: Rainy Day Detector ---"
.print "Create a query that finds all days with significant rainfall (precipitation > 5)"
.print "showing the city, date, and amount of rain."

-- SOLUTION: Rainy Day Detection
-- This query finds all readings with significant precipitation (> 5mm)
-- Results are ordered by precipitation amount to show heaviest rain first
SELECT 
    l.city,
    l.state,
    ws.station_name,
    wr.reading_date,
    wr.precipitation as rainfall_amount,
    wr.temperature,
    wr.humidity,
    -- Add a descriptive category for the rainfall intensity
    CASE 
        WHEN wr.precipitation > 20 THEN 'Heavy Rain'
        WHEN wr.precipitation > 10 THEN 'Moderate Rain'
        WHEN wr.precipitation > 5 THEN 'Light Rain'
        ELSE 'No Significant Rain'
    END as rain_category
FROM weather_readings wr
    INNER JOIN weather_stations ws ON wr.station_id = ws.station_id
    INNER JOIN locations l ON ws.location_id = l.location_id
WHERE wr.precipitation > 5
ORDER BY wr.precipitation DESC, wr.reading_date;

-- Additional Analysis: Summary of rainy days by city
.print "\nRainy Day Summary by City:"
SELECT 
    l.city,
    l.state,
    COUNT(*) as rainy_days,
    ROUND(AVG(wr.precipitation), 2) as avg_rainfall_on_rainy_days,
    ROUND(MAX(wr.precipitation), 2) as max_rainfall,
    MIN(wr.reading_date) as first_rainy_day,
    MAX(wr.reading_date) as last_rainy_day
FROM weather_readings wr
    INNER JOIN weather_stations ws ON wr.station_id = ws.station_id
    INNER JOIN locations l ON ws.location_id = l.location_id
WHERE wr.precipitation > 5
GROUP BY l.city, l.state
ORDER BY rainy_days DESC, avg_rainfall_on_rainy_days DESC;


-- Additional Challenge: Weather Trends Over Time
.print "\n--- CHALLENGE 5: Weather Trends Over Time ---"
SELECT 
    strftime('%Y-%m', wr.reading_date) as month,
    l.city,
    l.state,
    ROUND(AVG(wr.temperature), 2) as avg_temperature,
    ROUND(AVG(wr.humidity), 2) as avg_humidity,
    ROUND(SUM(wr.precipitation), 2) as total_precipitation
FROM weather_readings wr
    INNER JOIN weather_stations ws ON wr.station_id = ws.station_id
    INNER JOIN locations l ON ws.location_id = l.location_id
WHERE wr.reading_date >= '2023-01-01' AND wr.reading_date < '2024-01-01'
GROUP BY month, l.city, l.state
ORDER BY month, l.city;

-- Add additional data for more comprehensive trends
INSERT OR IGNORE INTO weather_readings (station_id, temperature, humidity, pressure, precipitation, reading_date)
VALUES
(5, 30.0, 80.0, 1011.0, 0.0, '2023-07-01'),
(5, 29.5, 82.0, 1010.5, 15.0, '2023-07-02'),
(6, 20.0, 65.0, 1013.0, 3.0, '2023-07-01'),
(6, 19.5, 70.0, 1012.5, 4.5, '2023-07-02');
-- Final check to ensure all data is inserted correctly
.print "\n--- Final Data Check ---"
.print "\nLocations:"
SELECT * FROM locations;

-- Add additional cities and weather stations if needed
.print "\nWeather Stations:"
SELECT * FROM weather_stations;
.print "\nWeather Readings:"
SELECT * FROM weather_readings ORDER BY reading_date DESC LIMIT 10;
