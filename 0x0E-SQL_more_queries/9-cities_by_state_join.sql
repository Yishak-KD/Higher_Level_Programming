-- joining tables

SELECT c.id, c.name, s.name
FROM cities c
JOIN states s
	ON c.id = s.id
ORDER BY c.id
