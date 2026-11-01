SELECT id, name, species, area_id from animals
ORDER BY species, id ASC;


SELECT * FROM animals;



SELECT * FROM animals
WHERE admitted_on IS NULL OR weight IS NULL;

SELECT * FROM animals
WHERE area_id = 3;


INSERT INTO areas (name)
VALUES ('Cat Wing');

-- Skal feile fordi det ikke finnes en area_id 5 som FK.
INSERT INTO animals (name, species, weight, admitted_on, area_id)
VALUES ('Kira', 'cat', 1.65, '2026-10-09', 5);

-- Legger til en ny kolonne med en standardverdi. Når denne kjører legges standardverdien inn i alle eksisterende rader
ALTER TABLE animals
ADD status VARCHAR(20) not null DEFAULT 'new';


-- kolonner som ikke spesifiseres får verdien <null>
INSERT INTO animals (name, species, area_id)
VALUES ('Oreo', 'cat', 1);


-- Endre kolonne fra VARCHAR(40) --> VARCHAR(60)
-- Husk at man også må sette andre properties selv om disse ikke skal endres (eks. NOT NULL)
ALTER TABLE animals
MODIFY name VARCHAR(60) NOT NULL;

-- ************ SLETTING AV KOLONNER OG TABELL ***********
    CREATE TABLE scratch_labels(
        id INT AUTO_INCREMENT PRIMARY KEY,
        label VARCHAR(20)
    );

INSERT INTO scratch_labels (label)
VALUES ('Temporary label');

SELECT * FROM scratch_labels;

ALTER TABLE scratch_labels
DROP COLUMN label;

DROP TABLE scratch_labels;

-- ******************* Oppdatering av verdier *************

select * FROM animals;
select * FROM areas;

UPDATE animals
SET weight = 3.90
WHERE id = 1;

UPDATE animals
SET name = 'Rex Jr', weight = 19.20
WHERE id = 3;

UPDATE animals
SET area_id = 4
WHERE id = 6;

-- Ny vekt
UPDATE animals
SET weight = 14.60
WHERE id = 4;

-- Vekt var feil og blir derfor satt tilbake til <null>
UPDATE animals
SET weight = NULL
WHERE id = 4;