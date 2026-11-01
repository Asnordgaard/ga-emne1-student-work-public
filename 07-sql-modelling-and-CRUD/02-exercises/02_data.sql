-- Leg inn arter
INSERT INTO animal_species (name)
VALUES ('Hund'),
       ('Katt'),
       ('Fugl'),
       ('Fisk'),
       ('Reptil'),
       ('Gnager');


-- Legg in navn på avdelinger:
INSERT INTO areas (name)
VALUES ('Regnskogen'),
       ('Hundegården'),
       ('Lekegrinda'),
       ('Akvariet'),
       ('Løpehjulet'),
       ('Buret');


-- Registrer dyr:
INSERT INTO animals (name, weight, arrived_date, areas_id, species_id)
VALUES ('Sprirt', 12.7, '2026-09-25', 3, 2),
       ('Hubert', 34.5, '2026-08-10',1, 5),
       ('Laura', 0.78, '2026-10-12', 5, 6),
       ('Hannibal', 20.45, '2026-10-09', 2, 1);

