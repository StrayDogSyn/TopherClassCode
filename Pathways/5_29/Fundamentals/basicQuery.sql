-- Basic SELECT statement
SELECT city, state 
FROM locations
WHERE country = 'USA'
ORDER BY city ASC
LIMIT 10;

-- Selecting all columns
SELECT * 
FROM locations
WHERE state = 'CA';