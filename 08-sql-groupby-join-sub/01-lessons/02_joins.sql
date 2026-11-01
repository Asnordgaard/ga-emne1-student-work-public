SELECT country.Name AS country_name, country.Code, CountryCode, city.Name AS city
FROM city
JOIN country
    ON city.CountryCode = Code;


SELECT country.Name AS country_name,
       city.Name AS capital_name,
       countrylanguage.Language
FROM country
JOIN city ON country.Capital = city.ID
JOIN countrylanguage ON country.Code = countrylanguage.CountryCode
WHERE country.Continent = 'Europe'
    AND countrylanguage.IsOfficial = 'T'
ORDER BY country_name ASC;


SELECT country.Name,
       city.Name
FROM country
         LEFT JOIN city
                   ON country.Code = city.CountryCode
ORDER BY country.Name;

SELECT country.Name,
       city.Name
FROM country
LEFT JOIN city
    ON country.Code = city.CountryCode
WHERE city.Name IS NULL
ORDER BY country.Name;