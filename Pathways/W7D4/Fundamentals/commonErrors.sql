-- Incorrect (missing comma)
-- SELECT city state FROM locations;

-- Correct
SELECT city, state FROM locations;

-- Incorrect (ambiguous column)
-- SELECT id FROM locations JOIN weather_stations;

-- Correct
SELECT l.location_id 
FROM locations l 
JOIN weather_stations ws;

-- Incorrect (grouping error)
-- SELECT city, AVG(temperature) FROM weather_readings;

-- Correct
SELECT l.city, AVG(wr.temperature) 
FROM weather_readings wr
JOIN weather_stations ws ON wr.station_id = ws.station_id
JOIN locations l ON ws.location_id = l.location_id
GROUP BY l.city;