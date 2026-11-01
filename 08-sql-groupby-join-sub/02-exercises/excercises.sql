-- Oppgave 1: Samlet areal
SELECT SUM(country.SurfaceArea) AS 'Samlet areal'
FROM country
WHERE Continent = 'Asia';


-- Oppgave 2: Gjennomsnittlig forlketall
SELECT AVG(city.Population) AS 'Gjennomsnittlig befolkning i byer'
FROM city
WHERE CountryCode = 'DNK';


-- Oppgave 3: Laveste og høyeste verdier
SELECT MIN(LifeExpectancy) AS 'Lowest life expectancy', MAX(LifeExpectancy) AS 'Highest life expectancy'
FROM country;


-- Oppgave 4: Antall land per region
SELECT region, COUNT(*)
FROM country
GROUP BY region;