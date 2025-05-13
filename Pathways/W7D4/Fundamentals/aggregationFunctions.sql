-- COUNT - counting rows
SELECT COUNT(*) AS total_readings 
FROM weather_readings;

-- COUNT with DISTINCT - unique values
SELECT COUNT(DISTINCT station_id) AS station_count 
FROM weather_readings;

-- AVG - calculating averages
SELECT AVG(temperature) AS average_temperature 
FROM weather_readings;

-- MIN/MAX - finding minimum/maximum values
SELECT 
    MIN(temperature) AS coldest_temp,
    MAX(temperature) AS hottest_temp
FROM weather_readings;

-- Using GROUP BY
SELECT 
    station_id,
    COUNT(*) AS reading_count,
    AVG(temperature) AS avg_temp,
    SUM(precipitation) AS total_rainfall
FROM weather_readings
GROUP BY station_id;

-- Using HAVING to filter groups
SELECT 
    station_id,
    AVG(temperature) AS avg_temp
FROM weather_readings
GROUP BY station_id
HAVING AVG(temperature) > 25;