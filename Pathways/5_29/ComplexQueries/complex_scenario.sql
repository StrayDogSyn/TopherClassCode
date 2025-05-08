.headers on
.mode column
.width 10 20 15 10 10 12 12 12 12 12 12 12

.print "\n--- Comprehensive weather station analysis ---"
SELECT 
    ws.station_id,
    ws.station_name,
    l.city,
    l.state,
    ws.elevation,
    COUNT(wr.reading_id) AS reading_count,
    MIN(wr.reading_date) AS first_reading,
    MAX(wr.reading_date) AS last_reading,
    ROUND(AVG(wr.temperature), 1) AS avg_temp,
    ROUND(MIN(wr.temperature), 1) AS min_temp,
    ROUND(MAX(wr.temperature), 1) AS max_temp,
    ROUND(SUM(wr.precipitation), 1) AS total_precip,
    ROUND(AVG(wr.humidity), 1) AS avg_humidity
FROM weather_stations ws
JOIN locations l ON ws.location_id = l.location_id
LEFT JOIN weather_readings wr ON ws.station_id = wr.station_id
GROUP BY ws.station_id, ws.station_name, l.city, l.state, ws.elevation
ORDER BY reading_count DESC;