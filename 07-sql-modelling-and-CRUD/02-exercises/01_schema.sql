-- Oppretter DB (Schema)
CREATE DATABASE IF NOT EXISTS
animal_center;

-- Bruk den nye databasen:
USE animal_center;

-- Opprett tabelllen avdelinger:
CREATE TABLE areas(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40)
);

-- Opprett tabell for arter:
CREATE TABLE animal_species(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name varchar(20)
);

-- Opprett tabell for dyrene med fremmednøkler:
CREATE TABLE animals(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    weight DECIMAL(6,2),
    arrived_date DATE,
    areas_id INT NOT NULL,
    species_id INT NOT NULL,
    FOREIGN KEY (areas_id) REFERENCES areas(id),
    FOREIGN KEY (species_id) REFERENCES animal_species(id)
);



12999.00,Computers
399.00,Accessories
899.00,Accessories
3299.00,Monitors
699.00,Accessories
799.00,Accessories
1199.00,Audio
1499.00,Audio
1099.00,Storage
549.00,Accessories
