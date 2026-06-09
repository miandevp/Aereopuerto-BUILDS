
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
- [ ] Create the PostgreSQL database
- [ ] Implement all tables
- [ ] Add constraints
- [ ] Define relationships
- [ ] Validate the schema

---

## Phase 4 — Data Generation
- [ ] Generate synthetic data
- [ ] Create datasets with:
  - [ ] 1,000 records
  - [ ] 10,000 records
  - [ ] 100,000 records
  - [ ] 1,000,000 records
- [ ] Export SQL dumps

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
- [ ] Compare execution plans using `EXPLAIN ANALYZE`

---

## Phase 7 — Performance Lab (Frontend)
- [ ] Build a simple web interface
- [ ] Allow execution of benchmark queries
- [ ] Display execution times
- [ ] Compare indexed vs non-indexed performance
- [ ] Visualize results with charts

---

## Phase 8 — Deployment
- [ ] Publish the source code on GitHub
- [ ] Deploy the application
- [ ] Configure cloud infrastructure
- [ ] Document the deployment process

---

# Technology Stack

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
- PostgreSQL `EXPLAIN ANALYZE`

## Version Control
- Git
- GitHub

## Cloud (Optional)
- AWS EC2
- AWS RDS
- AWS S3

---

# System Architecture

```text
Browser
    ↓
HTML + Bootstrap + JavaScript
    ↓
Flask API
    ↓
PostgreSQL
```

## Future Cloud Architecture

```text
Browser
    ↓
S3 (Frontend)
    ↓
EC2 (Flask Backend)
    ↓
RDS (PostgreSQL)
```