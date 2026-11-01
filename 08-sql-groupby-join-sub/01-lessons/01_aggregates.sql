SELECT
    SUM(Population) AS total_population,
    AVG(Population) AS avg_population,
    MIN(Population) AS min_population,
    MAX(Population) AS max_population
FROM city
WHERE CountryCode = 'NOR'


SELECT Name, Population / 1000000 AS "pop milions"
FROM country
WHERE Population > 10000000
ORDER BY Population DESC;


SELECT Continent,
       Region,
       COUNT(*) AS country_count,
       SUM(Population) AS Population
FROM country
GROUP BY Continent, Region
ORDER BY Continent ASC, SUM(Population) ASC;


-- Having
SELECT Continent,
       COUNT(*) AS country_count,
       SUM(Population) AS Population
FROM country
WHERE Population > 10000000
GROUP BY Continent
HAVING country_count >= 5
ORDER BY country_count ASC;