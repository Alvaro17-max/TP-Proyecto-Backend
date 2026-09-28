CREATE DATABASE IF NOT EXISTS club_deportivo;
USE club_deportivo;

DROP TABLE IF EXISTS reservas;
DROP TABLE IF EXISTS canchas;
DROP TABLE IF EXISTS socios;
DROP TABLE IF EXISTS deportes;

CREATE TABLE deportes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE canchas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_deporte INT NOT NULL,
    precio_hora INT NOT NULL,
    techada BOOLEAN NOT NULL DEFAULT FALSE,
    activa BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (id_deporte) REFERENCES deportes(id)
);

CREATE TABLE socios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    activo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_socio INT NOT NULL,
    id_cancha INT NOT NULL,
    fecha_hora_inicio VARCHAR(35) NOT NULL,
    fecha_hora_fin VARCHAR(35) NOT NULL,
    tarifa_historica INT NOT NULL,
    total INT NOT NULL,
    estado VARCHAR(20) NOT NULL DEFAULT 'confirmada',
    FOREIGN KEY (id_socio) REFERENCES socios(id),
    FOREIGN KEY (id_cancha) REFERENCES canchas(id)
);

INSERT INTO deportes (id, nombre) VALUES 
(1, 'Futbol'),
(2, 'Tenis'),
(3, 'Padel'),
(4, 'Basquet');