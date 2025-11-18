Assignment 11: Polymorphic Calculator API with Robust CI/CD

This project implements a simple, extendable calculator API using FastAPI, PostgreSQL (via SQLAlchemy), and a fully automated CI/CD pipeline enforced by GitHub Actions and Trivy security scanning.

The core technical focus is demonstrating SQLAlchemy's Single-Table Polymorphic Inheritance for database modeling and establishing a robust testing framework that handles complex dependency loading.



⚙️ Key Technologies

Backend: FastAPI, Python 3.10

ORM/Database: SQLAlchemy 2.0, PostgreSQL (via Docker Service)

Testing: Pytest, coverage, Playwright (for E2E)

CI/CD: GitHub Actions, Docker Buildx, Trivy Security Scanner

✨ Polymorphic Model Design

The application uses SQLAlchemy's Single-Table Polymorphism for the calculation feature.

AbstractCalculation (Mixin): Defines all shared attributes (id, user_id, inputs, result, etc.) using @declared_attr.cascading. This ensures all subclasses are mapped to the single table.

Calculation (Base Model): Inherits from Base and the AbstractCalculation Mixin. It serves as the base mapper and defines the discriminator column (polymorphic_on = 'type').

Subclasses (Addition, Subtraction, etc.): Each subclass defines its unique operation (get_result()) and its unique polymorphic identity (e.g., 'addition').

This structure allows all calculation records to be stored in one table while maintaining type-specific business logic.

🏃 Getting Started (Local Development)

Prerequisites

Docker (for running PostgreSQL service)

Python 3.10+

Setup

Clone the Repository:

git clone [REPOSITORY_URL]
cd assignment11


Create and Activate Virtual Environment:

python -m venv venv
source venv/bin/activate


Install Dependencies:

pip install -r requirements.txt
playwright install


Start Database (via Docker Compose):

docker-compose up -d postgres


Note: Ensure your database connection details in app/core/config.py match the docker-compose.yml service environment variables.

Run Migrations (if using Alembic): (Command based on your setup, typically alembic upgrade head)

Run FastAPI:

uvicorn main:app --reload


🧪 Running Tests

All tests, including unit tests for the core logic, integration tests for the polymorphic models, and E2E tests, can be run using the following command:

pytest tests/ --cov=app --junitxml=test-results/junit.xml


🔐 CI/CD & Security Policy

The ci_cd.yml pipeline enforces a three-stage workflow:

test: Runs all unit, integration, and E2E tests against a dedicated PostgreSQL service (via GitHub Actions Services).

security: Builds the application image and runs Trivy to scan the image and all dependencies for CRITICAL and HIGH severity vulnerabilities. The pipeline fails if any are found.

deploy: If both test and security pass, the Docker image is built and pushed to Docker Hub.Assignment 11: Polymorphic Calculator API with Robust CI/CD

This project implements a simple, extendable calculator API using FastAPI, PostgreSQL (via SQLAlchemy), and a fully automated CI/CD pipeline enforced by GitHub Actions and Trivy security scanning.

The core technical focus is demonstrating SQLAlchemy's Single-Table Polymorphic Inheritance for database modeling and establishing a robust testing framework that handles complex dependency loading.

📦 Project Structure

.
├── .github/workflows/
│   └── ci_cd.yml       # Full CI/CD pipeline (Test -> Security -> Deploy)
├── app/
│   ├── core/           # Configuration management
│   ├── models/         # SQLAlchemy Models (User, AbstractCalculation, Subclasses)
│   │   ├── calculation.py    # Defines Polymorphic Calculation model
│   │   └── user.py           # Defines User model
│   ├── operations/     # Core business logic (add, subtract, etc.)
│   ├── database.py     # SQLAlchemy engine, Base, and session setup
│   └── main.py         # FastAPI application entry point
├── tests/
│   ├── unit/
│   │   └── test_calculator.py
│   └── integration/
│       └── test_calculation.py   # Tests Polymorphic Factory and Subclasses
├── Dockerfile          # Used for application image building
└── requirements.txt


⚙️ Key Technologies

Backend: FastAPI, Python 3.10

ORM/Database: SQLAlchemy 2.0, PostgreSQL (via Docker Service)

Testing: Pytest, coverage, Playwright (for E2E)

CI/CD: GitHub Actions, Docker Buildx, Trivy Security Scanner

✨ Polymorphic Model Design

The application uses SQLAlchemy's Single-Table Polymorphism for the calculation feature.

AbstractCalculation (Mixin): Defines all shared attributes (id, user_id, inputs, result, etc.) using @declared_attr.cascading. This ensures all subclasses are mapped to the single table.

Calculation (Base Model): Inherits from Base and the AbstractCalculation Mixin. It serves as the base mapper and defines the discriminator column (polymorphic_on = 'type').

Subclasses (Addition, Subtraction, etc.): Each subclass defines its unique operation (get_result()) and its unique polymorphic identity (e.g., 'addition').

This structure allows all calculation records to be stored in one table while maintaining type-specific business logic.

🏃 Getting Started (Local Development)

Prerequisites

Docker (for running PostgreSQL service)

Python 3.10+

Setup

Clone the Repository:

git clone [REPOSITORY_URL]
cd assignment11


Create and Activate Virtual Environment:

python -m venv venv
source venv/bin/activate


Install Dependencies:

pip install -r requirements.txt
playwright install


Start Database (via Docker Compose):

docker-compose up -d postgres


Note: Ensure your database connection details in app/core/config.py match the docker-compose.yml service environment variables.

Run Migrations (if using Alembic): (Command based on your setup, typically alembic upgrade head)

Run FastAPI:

uvicorn main:app --reload


🧪 Running Tests

All tests, including unit tests for the core logic, integration tests for the polymorphic models, and E2E tests, can be run using the following command:

pytest tests/ --cov=app --junitxml=test-results/junit.xml


🔐 CI/CD & Security Policy

The ci_cd.yml pipeline enforces a three-stage workflow:

test: Runs all unit, integration, and E2E tests against a dedicated PostgreSQL service (via GitHub Actions Services).

security: Builds the application image and runs Trivy to scan the image and all dependencies for CRITICAL and HIGH severity vulnerabilities. The pipeline fails if any are found.

deploy: If both test and security pass, the Docker image is built and pushed to Docker Hub.