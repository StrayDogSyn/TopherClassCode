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

-- TODO: Write your query here
-- HINT: You'll need to JOIN tables and use aggregate functions

.print "\n--- CHALLENGE 2: Find the Hottest and Coldest Cities ---"
.print "Create a query that ranks cities by their average temperature,"
.print "showing the hottest and coldest cities."

-- TODO: Write your query here
-- HINT: You'll need to JOIN tables, use GROUP BY, and ORDER BY

.print "\n--- CHALLENGE 3: Comparing Cities ---"
.print "Create a query that compares two specific cities (e.g., 'New York' and 'Los Angeles')"
.print "showing their average temperatures, humidity, and precipitation."

-- TODO: Write your query here
-- HINT: You'll need to use WHERE to filter specific cities

.print "\n--- CHALLENGE 4: Rainy Day Detector ---"
.print "Create a query that finds all days with significant rainfall (precipitation > 5)"
.print "showing the city, date, and amount of rain."

-- TODO: Write your query here
-- HINT: You'll need to use WHERE with a condition on precipitation