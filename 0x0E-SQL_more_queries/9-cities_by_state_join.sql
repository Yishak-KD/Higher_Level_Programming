-- joining tables

USE hbtn_0d_usa;
SELECT cities.id, cities.name, states.name
FROM states
JOIN cities 
	ON states.id = cities.id
ORDER BY cities.id
