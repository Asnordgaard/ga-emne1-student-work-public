-- Opprett ny database:
CREATE DATABASE IF NOT EXISTS
    music_school;

USE music_school

-- For å sjekke at vi står i rett DB:
SELECT DATABASE()


-- Opprett tabell:
CREATE TABLE rooms (
    id INT AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    PRIMARY KEY(id),
    UNIQUE(name)
);

-- Kan også skrives slik (med PK og UNIQUE)
CREATE TABLE rooms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40) NOT NULL UNIQUE
);


-- Opprette tabell med fremmednøkkel:
CREATE TABLE instruments(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    purchase_price DECIMAL(8,2),
    acquired_on DATE,
    room_id INT NOT NULL,
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);

