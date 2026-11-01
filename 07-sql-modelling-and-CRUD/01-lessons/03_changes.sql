-- Endre eksisterende tabell - legge til kolonne:
ALTER TABLE rooms
ADD COLUMN capacity INT NOT NULL DEFAULT 1;


-- Endre eksisterende kolonne:
ALTER TABLE rooms
ADD COLUMN capacity INT NOT NULL DEFAULT 1;


-- Slette en kolonne:
ALTER TABLE rooms
DROP COLUMN capacity;


-- Slette en tabell
DROP TABLE table_name;


-- Finn top 3 kunden som har høyest samlet beregnet verdi på bestillingene sine. Relatert til innlevering 2 database.
SELECT
    customers.first_name,
    customers.last_name,
    SUM(orders.quantity * products.price) AS totalt
FROM customers
         JOIN orders
              ON customers.id = orders.customer_id
         JOIN products
              ON orders.product_id = products.id
GROUP BY customers.id
HAVING totalt > 5000.00
ORDER BY totalt DESC
LIMIT 3;