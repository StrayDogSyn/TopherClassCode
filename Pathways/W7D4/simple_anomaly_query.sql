-- Simple working version for immediate testing

SELECT 
    wr.reading_date,
    l.city,
    wr.temperature as actual_temp,
    ROUND(city_stats.avg_temp, 2) as city_avg_temp,
    ROUND(city_stats.std_dev, 2) as city_std_dev,
    ROUND((wr.temperature - city_stats.avg_temp) / city_stats.std_dev, 2) AS z_score
FROM weather_readings wr
JOIN weather_stations ws ON wr.station_id = ws.station_id
JOIN locations l ON ws.location_id = l.location_id
JOIN (
    SELECT 
        l2.city,
        AVG(wr2.temperature) AS avg_temp,
        -- Use the variance formula: SQRT(AVG(x²) - AVG(x)²)
        SQRT(AVG(wr2.temperature * wr2.temperature) - AVG(wr2.temperature) * AVG(wr2.temperature)) AS std_dev
    FROM weather_readings wr2
    JOIN weather_stations ws2 ON wr2.station_id = ws2.station_id
    JOIN locations l2 ON ws2.location_id = l2.location_id
    GROUP BY l2.city
) city_stats ON l.city = city_stats.city
WHERE city_stats.std_dev > 0
  AND ABS((wr.temperature - city_stats.avg_temp) / city_stats.std_dev) > 1
ORDER BY ABS((wr.temperature - city_stats.avg_temp) / city_stats.std_dev) DESC;
