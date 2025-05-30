-- Finding Anomalies with Subqueries
-- Demonstrates using subqueries for statistical analysis

.headers on
.mode column
.width 15 15 10 10 10 10

.print "\n--- Finding temperature anomalies ---"
-- ADVANCED STATISTICAL ANOMALY DETECTION QUERY
-- This query demonstrates complex subqueries, statistical functions, and anomaly detection
-- using Z-score analysis to identify temperature readings that deviate significantly from normal

SELECT 
    wr.reading_date,
    l.city,
    l.state,
    ws.station_name,
    wr.temperature as actual_temp,
    ROUND(city_stats.avg_temp, 2) as city_avg_temp,
    ROUND(city_stats.std_dev, 2) as city_std_dev,
    ROUND((wr.temperature - city_stats.avg_temp) / city_stats.std_dev, 2) AS z_score,
    -- Add interpretation of the z-score
    CASE 
        WHEN ABS((wr.temperature - city_stats.avg_temp) / city_stats.std_dev) > 3 THEN 'EXTREME ANOMALY'
        WHEN ABS((wr.temperature - city_stats.avg_temp) / city_stats.std_dev) > 2 THEN 'SIGNIFICANT ANOMALY'
        WHEN ABS((wr.temperature - city_stats.avg_temp) / city_stats.std_dev) > 1 THEN 'MILD ANOMALY'
        ELSE 'NORMAL'
    END as anomaly_level,
    -- Calculate deviation in actual temperature units
    ROUND(wr.temperature - city_stats.avg_temp, 2) as temp_deviation
FROM weather_readings wr
JOIN weather_stations ws ON wr.station_id = ws.station_id
JOIN locations l ON ws.location_id = l.location_id
JOIN (
    -- SUBQUERY: Calculate statistical measures for each city
    -- This creates a derived table with city-level statistics
    SELECT 
        l2.city,
        COUNT(*) as reading_count,
        AVG(wr2.temperature) AS avg_temp,
        -- FIXED STANDARD DEVIATION CALCULATION
        -- Standard deviation formula: SQRT(SUM((x - mean)²) / (n-1)) for sample std dev
        -- SQLite doesn't have built-in STDEV function, so we calculate manually
        CASE 
            WHEN COUNT(*) > 1 THEN
                SQRT(
                    SUM((wr2.temperature - (
                        SELECT AVG(wr3.temperature) 
                        FROM weather_readings wr3 
                        JOIN weather_stations ws3 ON wr3.station_id = ws3.station_id
                        JOIN locations l3 ON ws3.location_id = l3.location_id
                        WHERE l3.city = l2.city
                    )) * (wr2.temperature - (
                        SELECT AVG(wr3.temperature) 
                        FROM weather_readings wr3 
                        JOIN weather_stations ws3 ON wr3.station_id = ws3.station_id
                        JOIN locations l3 ON ws3.location_id = l3.location_id
                        WHERE l3.city = l2.city
                    ))) / (COUNT(*) - 1)
                )
            ELSE 0  -- No standard deviation for single data point
        END AS std_dev
    FROM weather_readings wr2
    JOIN weather_stations ws2 ON wr2.station_id = ws2.station_id
    JOIN locations l2 ON ws2.location_id = l2.location_id
    GROUP BY l2.city
    HAVING COUNT(*) > 1  -- Only include cities with multiple readings
) city_stats ON l.city = city_stats.city
-- FILTER: Only show readings that deviate by more than 1 standard deviation
WHERE ABS((wr.temperature - city_stats.avg_temp) / city_stats.std_dev) > 1
  AND city_stats.std_dev > 0  -- Avoid division by zero
-- ORDER: Show most extreme anomalies first
ORDER BY ABS((wr.temperature - city_stats.avg_temp) / city_stats.std_dev) DESC;

.print "\n--- DETAILED EXPLANATION ---"
.print "This advanced statistical anomaly detection query demonstrates several complex SQL concepts:"
.print ""
.print "1. SUBQUERY IN FROM CLAUSE (Derived Table):"
.print "   - Creates a temporary table 'city_stats' with statistical measures for each city"
.print "   - Calculates mean temperature and standard deviation per city"
.print "   - Uses proper sample standard deviation formula: SQRT(SUM((x-mean)²)/(n-1))"
.print ""
.print "2. Z-SCORE CALCULATION:"
.print "   - Z-score = (individual_value - mean) / standard_deviation"
.print "   - Measures how many standard deviations a value is from the mean"
.print "   - Values > 2 or < -2 are typically considered significant anomalies"
.print ""
.print "3. ANOMALY CLASSIFICATION:"
.print "   - EXTREME: |z-score| > 3 (99.7% confidence)"
.print "   - SIGNIFICANT: |z-score| > 2 (95% confidence)"
.print "   - MILD: |z-score| > 1 (68% confidence)"
.print ""
.print "4. ADVANCED SQL FEATURES USED:"
.print "   - Complex JOINs across multiple tables"
.print "   - Subqueries with correlated references"
.print "   - CASE statements for conditional logic"
.print "   - Aggregate functions (COUNT, AVG, SUM)"
.print "   - Mathematical functions (SQRT, ABS, ROUND)"
.print "   - HAVING clause for aggregate filtering"
.print ""
.print "5. PRACTICAL APPLICATIONS:"
.print "   - Weather monitoring and climate analysis"
.print "   - Quality control in scientific measurements"
.print "   - Fraud detection in financial systems"
.print "   - Performance monitoring in manufacturing"
.print ""
.print "Note: This query filters for readings > 1 standard deviation for demonstration."
.print "In practice, typically use > 2 or 3 standard deviations for true anomaly detection."