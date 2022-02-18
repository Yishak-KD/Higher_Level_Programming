-- joining tables

USE hbtn_0d_usa;
SELECT c.id, c.name, s.name
FROM cities c
JOIN states s
	ON c.id = s.id
ORDER BY c.id
