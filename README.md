# Airport Database Project – Jorge Chávez International Airport

Proyecto desarrollado para el curso de Bases de Datos.

El objetivo es diseñar, implementar y evaluar una base de datos relacional que represente el funcionamiento del Aeropuerto Internacional Jorge Chávez utilizando PostgreSQL.

---

# Project Roadmap

## Phase 1 — Requirements & Design
- [x] Define the problem domain (Airport Jorge Chávez)
- [x] Gather requirements
- [x] Identify entities and relationships
- [x] Create the Entity–Relationship (E/R) model
- [x] Define semantic rules

---

## Phase 2 — Relational Modeling
- [x] Transform the E/R model into a relational model
- [x] Define primary keys (PK)
- [x] Define foreign keys (FK)
- [x] Specify integrity constraints
- [x] Build the data dictionary

---

## Phase 3 — Database Implementation
- [x] Create the PostgreSQL database
- [x] Implement all tables
- [x] Add constraints
- [x] Define relationships
- [x] Validate the schema

---

## Phase 4 — Data Generation
- [x] Generate synthetic data
- [x] Export CSV datasets

Supported dataset sizes:

- 1,000
- 10,000
- 100,000
- 1,000,000
- 2,000,000

---

## Phase 5 — Query Development
- [ ] Implement the required SQL queries
- [ ] Create user views
- [ ] Validate query correctness

---

## Phase 6 — Indexing & Optimization
- [ ] Identify critical queries
- [ ] Execute benchmarks without indexes
- [ ] Create indexes
- [ ] Execute benchmarks with indexes
- [ ] Compare execution plans using EXPLAIN ANALYZE

---

## Phase 7 — Performance Lab (Frontend)
- [ ] Build a web interface
- [ ] Execute benchmark queries
- [ ] Display execution times
- [ ] Compare indexed vs non-indexed performance
- [ ] Visualize execution statistics

---

## Phase 8 — Deployment
- [ ] Publish source code on GitHub
- [ ] Deploy application
- [ ] Configure cloud infrastructure
- [ ] Document deployment

---

# Technologies

## Database

- PostgreSQL

## Backend

- Python
- Flask

## Frontend

- HTML
- Bootstrap
- JavaScript

## Data Generation

- Python
- Faker

## Performance Analysis

- PostgreSQL
- EXPLAIN ANALYZE

## Version Control

- Git
- GitHub

---

# Project Structure

```
Data/
│
├── aerolineas.csv
├── areas.csv
├── pasajeros.csv
├── vuelos.csv
├── ...
│
DataBase/
│
├── aerolinea1m.py
├── pasajero1m.py
├── vuelo1m.py
├── reserva1m.py
├── ...
│
Tablas/
│
└── tablas.sql

README.md
```

---

# Database Schema

The SQL schema is located in:

```
Tablas/tablas.sql
```

---

# Synthetic Data Generation

Each table has its own Python generator.

Run them in the following order:

```
1. aerolinea1m.py
2. area1m.py
3. empleado1m.py
4. pasajero1m.py
5. pista1m.py

6. areacomercial1m.py
7. areaembarque1m.py
8. areaequipaje1m.py
9. areaseguridad1.py

10. avion1m.py
11. vuelo1m.py

12. puerta_embarque1m.py

13. reserva1m.py

14. boleto1m.py

15. equipaje1m.py

16. asignado_e1m.py
17. asignado_p1m.py
18. usa1m.py
19. realiza1m.py
```

This order respects all foreign key dependencies.

Configuración actual (1M)

Según tus scripts, tienes aproximadamente:

Tabla	Cantidad (1M)
Aerolinea	1,000
Area	1,000
Area_comercial	250
Area_embarque	250
Area_equipaje	250
Area_seguridad	250
Empleado	100,000
Pasajero	2,000,000
Pista	1,000
Puerta_embarque	1,000
Avion	10,000
Vuelo	2,000,000
Reserva	2,000,000
Boleto	2,000,000
Equipaje	2,000,000
Asignado_empleado	1,000
Asignado_puerta	2,000,000
Usa_pista	2,000,000
Realiza	2,000,000

---


Archivo	Cambiar
pasajero1m.py	TOTAL_PASAJEROS
vuelo1m.py	TOTAL_VUELOS
reserva1m.py	TOTAL_RESERVAS
boleto1m.py	TOTAL_BOLETOS
equipaje1m.py	TOTAL_EQUIPAJES
asignado_p1m.py	TOTAL_ASIGNACIONES
usa1m.py	TOTAL_USOS



# PostgreSQL Import Order

After generating the CSV files, import them into PostgreSQL in the following order:

```
1. Aerolinea
2. Area
3. Empleado
4. Pasajero
5. Pista

6. Area_comercial
7. Area_embarque
8. Area_equipaje
9. Area_seguridad

10. Avion
11. Vuelo

12. Puerta_embarque

13. Reserva

14. Boleto

15. Equipaje

16. Asignado_empleado
17. Asignado_puerta
18. Usa_pista
19. Realiza
```

Importing in another order may produce foreign key constraint errors.

---

# System Architecture

```
Browser
      ↓
HTML + Bootstrap + JavaScript
      ↓
Flask API
      ↓
PostgreSQL
```

---

# Future Cloud Architecture

```
Browser
      ↓
Amazon S3
      ↓
AWS EC2 (Flask)
      ↓
PostgreSQL RDS
```

---

# Authors

Computer Science Project

Airport Database — Jorge Chávez International Airport