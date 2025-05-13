-- Set output formatting
.headers on
.mode column

-- Create tables
CREATE TABLE locations (
    location_id INTEGER PRIMARY KEY,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    country TEXT NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL
);

CREATE TABLE weather_stations (
    station_id INTEGER PRIMARY KEY,
    station_name TEXT NOT NULL,
    location_id INTEGER NOT NULL,
    elevation REAL NOT NULL,
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

CREATE TABLE weather_readings (
    reading_id INTEGER PRIMARY KEY,
    station_id INTEGER NOT NULL,
    temperature REAL NOT NULL,
    humidity REAL NOT NULL,
    pressure REAL NOT NULL,
    precipitation REAL NOT NULL,
    reading_date TEXT NOT NULL,
    FOREIGN KEY (station_id) REFERENCES weather_stations(station_id)
);

-- Insert sample data
INSERT INTO locations (city, state, country, latitude, longitude)
VALUES 
('New York', 'NY', 'USA', 40.7128, -74.0060),
('Los Angeles', 'CA', 'USA', 34.0522, -118.2437),
('Chicago', 'IL', 'USA', 41.8781, -87.6298),
('Houston', 'TX', 'USA', 29.7604, -95.3698),
('Phoenix', 'AZ', 'USA', 33.4484, -112.0740);

INSERT INTO weather_stations (station_name, location_id, elevation)
VALUES 
('NY Central Park', 1, 10.5),
('LA Downtown', 2, 89.0),
('Chicago O''Hare', 3, 205.7),
('Houston Metro', 4, 13.1);

INSERT INTO weather_readings (station_id, temperature, humidity, pressure, precipitation, reading_date)
VALUES 
(1, 22.5, 65.0, 1012.3, 0.0, '2023-06-01'),
(1, 24.8, 70.2, 1010.1, 5.2, '2023-06-02'),
(2, 28.3, 45.5, 1011.2, 0.0, '2023-06-01'),
(2, 29.7, 42.0, 1012.5, 0.0, '2023-06-02'),
(3, 19.5, 72.5, 1009.8, 12.5, '2023-06-01'),
(3, 21.2, 68.0, 1011.0, 0.5, '2023-06-02'),
(4, 31.2, 80.5, 1008.2, 0.0, '2023-06-01'),
(4, 32.8, 78.0, 1007.5, 22.5, '2023-06-02');