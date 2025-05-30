-- Working Standard Deviation Query for SQLite
-- This version uses a simpler but mathematically equivalent approach

SELECT 
    wr.reading_date,
    l.city,
    l.state,
    wr.temperature as actual_temp,
    ROUND(city_stats.avg_temp, 2) as city_avg_temp,
    ROUND(city_stats.std_dev, 2) as city_std_dev,
    ROUND((wr.temperature - city_stats.avg_temp) / 
          CASE WHEN city_stats.std_dev > 0 THEN city_stats.std_dev ELSE 1 END, 2) AS z_score,
    CASE 
        WHEN ABS((wr.temperature - city_stats.avg_temp) / 
                 CASE WHEN city_stats.std_dev > 0 THEN city_stats.std_dev ELSE 1 END) > 3 THEN 'EXTREME'
        WHEN ABS((wr.temperature - city_stats.avg_temp) / 
                 CASE WHEN city_stats.std_dev > 0 THEN city_stats.std_dev ELSE 1 END) > 2 THEN 'SIGNIFICANT'
        WHEN ABS((wr.temperature - city_stats.avg_temp) / 
                 CASE WHEN city_stats.std_dev > 0 THEN city_stats.std_dev ELSE 1 END) > 1 THEN 'MILD'
        ELSE 'NORMAL'
    END as anomaly_level
FROM weather_readings wr
JOIN weather_stations ws ON wr.station_id = ws.station_id
JOIN locations l ON ws.location_id = l.location_id
JOIN (
    -- Calculate statistics using variance formula: VAR = AVG(x²) - AVG(x)²
    SELECT 
        l2.city,
        COUNT(*) as reading_count,
        AVG(wr2.temperature) AS avg_temp,
        -- Standard deviation = SQRT(variance)
        -- Variance = (sum of squares / n) - (mean)²
        SQRT(
            AVG(wr2.temperature * wr2.temperature) - 
            (AVG(wr2.temperature) * AVG(wr2.temperature))
        ) AS std_dev
    FROM weather_readings wr2
    JOIN weather_stations ws2 ON wr2.station_id = ws2.station_id
    JOIN locations l2 ON ws2.location_id = l2.location_id
    GROUP BY l2.city
    HAVING COUNT(*) > 1
) city_stats ON l.city = city_stats.city
WHERE ABS((wr.temperature - city_stats.avg_temp) / 
          CASE WHEN city_stats.std_dev > 0 THEN city_stats.std_dev ELSE 1 END) > 1
  AND city_stats.std_dev > 0
ORDER BY ABS((wr.temperature - city_stats.avg_temp) / city_stats.std_dev) DESC;
