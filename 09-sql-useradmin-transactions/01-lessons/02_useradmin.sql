CREATE USER 'city_reader'@'%'
IDENTIFIED BY 'ReadOnly_09!'; -- Passord

GRANT SELECT ON world.city
TO 'city_reader'@'%';

SHOW GRANTS
FOR 'city_reader'@'%';


-- Logg på som city_reader (Ny DataSourcce)
SELECT * FROM city;

INSERT INTO city (name, CountryCode, District, Population)
VALUES (blabla, AFG, Kabol, 1000);


