-- Finding Anomalies with Subqueries
-- Demonstrates using subqueries for statistical analysis

.headers on
.mode column
.width 15 15 10 10 10 10

.print "\n--- Finding temperature anomalies ---"
SELECT 
    wr.reading_date,
    l.city,
    wr.temperature,
    city_stats.avg_temp,
    city_stats.std_dev,
    ROUND((wr.temperature - city_stats.avg_temp) / city_stats.std_dev, 2) AS z_score
FROM weather_readings wr
JOIN weather_stations ws ON wr.station_id = ws.station_id
JOIN locations l ON ws.location_id = l.location_id
JOIN (
    -- Calculate average and standard deviation for each city
    SELECT 
        l2.city,
        AVG(wr2.temperature) AS avg_temp,
        SQRT(AVG((wr2.temperature - AVG(wr2.temperature)) * (wr2.temperature - AVG(wr2.temperature)))) AS std_dev
    FROM weather_readings wr2
    JOIN weather_stations ws2 ON wr2.station_id = ws2.station_id
    JOIN locations l2 ON ws2.location_id = l2.location_id
    GROUP BY l2.city
) city_stats ON l.city = city_stats.city
WHERE ABS((wr.temperature - city_stats.avg_temp) / city_stats.std_dev) > 1
ORDER BY ABS((wr.temperature - city_stats.avg_temp) / city_stats.std_dev) DESC;

.print "\n--- Explanation ---"
.print "This complex query finds temperature anomalies (readings that deviate significantly from normal):"
.print "- Uses a subquery in the FROM clause to calculate statistics for each city"
.print "- Joins these statistics with individual readings"
.print "- Calculates z-scores to identify outliers (statistical measure of deviation)"
.print "- Filters for significant anomalies using the WHERE clause"
.print "- Orders results to show the most extreme anomalies first"
.print "- Note: We're using > 1 standard deviation for demonstration (typically > 2 or 3 would be used)"