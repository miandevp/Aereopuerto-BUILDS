CREATE TABLE Pasajero (
    dni_pasajero VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    nacionalidad VARCHAR(50),
    telefono VARCHAR(20)
);

CREATE TABLE Reserva (
    id_reserva INTEGER PRIMARY KEY,
    dni_pasajero VARCHAR(20) REFERENCES Pasajero(dni_pasajero),
    fecha DATE,
    estado VARCHAR(30),
    numero INTEGER,
    clase VARCHAR(30)
);

CREATE TABLE Aerolinea (
    codigo_icao VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(100),
    pais_origen VARCHAR(100),
    telefono VARCHAR(20)
);

CREATE TABLE Avion (
    matricula VARCHAR(20) PRIMARY KEY,
    codigo_icao VARCHAR(10) REFERENCES Aerolinea(codigo_icao),
    modelo VARCHAR(100),
    capacidad INTEGER,
    anio_fabricacion INTEGER
);

CREATE TABLE Vuelo (
    codigo_vuelo VARCHAR(20) PRIMARY KEY,
    codigo_icao VARCHAR(10) REFERENCES Aerolinea(codigo_icao),
    origen VARCHAR(100),
    destino VARCHAR(100),
    fecha DATE,
    hora_salida TIME,
    hora_llegada TIME,
    estado VARCHAR(30)
);

CREATE TABLE Boleto (
    id_boleto INTEGER PRIMARY KEY,
    codigo_vuelo VARCHAR(20) REFERENCES Vuelo(codigo_vuelo),
    precio NUMERIC(10,2)
);

CREATE TABLE Area (
    id_area INTEGER PRIMARY KEY,
    capacidad INTEGER
);

CREATE TABLE Area_equipaje (
    id_area INTEGER PRIMARY KEY REFERENCES Area(id_area)
);

CREATE TABLE Area_comercial (
    id_area INTEGER PRIMARY KEY REFERENCES Area(id_area)
);

CREATE TABLE Area_embarque (
    id_area INTEGER PRIMARY KEY REFERENCES Area(id_area)
);

CREATE TABLE Area_seguridad (
    id_area INTEGER PRIMARY KEY REFERENCES Area(id_area)
);

CREATE TABLE Equipaje (
    id_boleto INTEGER REFERENCES Boleto(id_boleto),
    nro_equipaje INTEGER,
    id_area INTEGER REFERENCES Area_equipaje(id_area),
    peso_kg NUMERIC(5,2),
    dimension VARCHAR(50),
    estado VARCHAR(30),
    PRIMARY KEY (id_boleto, nro_equipaje)
);

CREATE TABLE Pista (
    numero_pista INTEGER PRIMARY KEY,
    longitud INTEGER,
    estado VARCHAR(30)
);

CREATE TABLE Puerta_embarque (
    numero_puerta INTEGER PRIMARY KEY,
    id_area INTEGER REFERENCES Area_embarque(id_area),
    estado VARCHAR(30)
);

CREATE TABLE Empleado (
    dni_empleado VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    cargo VARCHAR(50),
    turno VARCHAR(30)
);

CREATE TABLE Asignado_puerta (
    codigo_vuelo VARCHAR(20) REFERENCES Vuelo(codigo_vuelo),
    numero_puerta INTEGER REFERENCES Puerta_embarque(numero_puerta),
    PRIMARY KEY (codigo_vuelo, numero_puerta)
);

CREATE TABLE Asignado_empleado (
    id_area INTEGER PRIMARY KEY REFERENCES Area(id_area),
    dni_empleado VARCHAR(20) REFERENCES Empleado(dni_empleado)
);

CREATE TABLE Usa_pista (
    codigo_vuelo VARCHAR(20) REFERENCES Vuelo(codigo_vuelo),
    numero_pista INTEGER REFERENCES Pista(numero_pista),
    PRIMARY KEY (codigo_vuelo, numero_pista)
);

CREATE TABLE Realiza (
    codigo_vuelo VARCHAR(20) REFERENCES Vuelo(codigo_vuelo),
    matricula VARCHAR(20) REFERENCES Avion(matricula),
    PRIMARY KEY (codigo_vuelo, matricula)
);