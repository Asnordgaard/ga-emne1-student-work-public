-- Emkleste spørring for å hente alle byer i Norge:
SELECT *
FROM city
WHERE CountryCode = 'NOR';


SELECT Name, Population
FROM city
WHERE (CountryCode = 'NOR'
  OR CountryCode = 'SWE')
  AND Population > 200000;


SELECT Name, Population
FROM city
WHERE CountryCode = 'NOR'
  OR (CountryCode = 'SWE'
  AND Population > 200000);


SELECT Name, Population
FROM city
WHERE (CountryCode = 'NOR'
  OR CountryCode = 'SWE')
  AND Population > 200000
ORDER BY Name ASC;


SELECT Name, Population
FROM city
ORDER BY Population DESC
LIMIT 5


SELECT Name, Population, CountryCode
FROM city
WHERE CountryCode LIKE 'N%'
    AND Population > 100000
ORDER BY Population DESC;

-- Gir alle byer som har fire tegn, der første og siste er
Select Name
FROM city
WHERE Name LIKE 'O__o';

-- Gir alle byer som begynner og slutter med bokstaven "O"
Select Name
FROM city
WHERE Name LIKE 'O%o';


Select Name
FROM city
WHERE CountryCode IN ('NPR', 'SWE', 'FIN');


Select *
FROM country
WHERE IndepYear IS null


Select *
FROM country
WHERE IndepYear IS NOT null

Select COUNT(*)
FROM country
WHERE Continent = 'Eur4ope'

Select COUNT(*) AS NumberOfEuropeanCities
FROM country
WHERE Continent = 'Europe'


Select Name AS CountryName, Population
FROM country
WHERE Continent = 'Europe'
