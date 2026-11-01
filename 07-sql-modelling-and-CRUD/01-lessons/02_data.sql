-- Legge inn en verdi i en kolonne. Her er "name" kolonnen spesifisert
INSERT INTO rooms (name)
VALUES ('Studio A');


-- Legge inn flere verdier på en gang:
INSERT INTO rooms (name)
VALUES  ('Studio B'),
        ('Practice room');


-- Legge inn verdier i en tabell når tabellen inneholder mange kolonner:
INSERT INTO instruments (name, purchase_price, acquired_on, room_id)
VALUES ('Piano', 18000.00, '2026-09-01', 1);


-- Endre verdi i en rad
UPDATE rooms
SET name = 'Studio A'
WHERE id = 1;


-- Endre verdi i en rad ved hjelp av beregning:
UPDATE instruments
SET purchase_price = purchase_price * 1.1, name = 'Grand Piano'
WHERE id = 1;


-- Slette en rad i en tabell
DELETE FROM instruments
WHERE id = 1;