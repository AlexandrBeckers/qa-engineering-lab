# QA Engineering Lab

A personal engineering project for learning and practicing modern Quality Assurance Automation.

The main goal of this repository is to build a production-like QA Automation Framework from scratch and gain hands-on experience with automation testing, infrastructure, CI/CD and engineering best practices.

---

## Goals

- Build a scalable QA Automation Framework
- Learn UI, API and Database testing
- Practice Message Broker testing (Kafka, RabbitMQ)
- Work with Docker and Docker Compose
- Configure CI/CD with GitHub Actions
- Generate Allure Reports
- Follow engineering best practices

---

## Technology Stack

### Languages

- Python 3.14

### Testing

- Pytest
- Requests

### API

- REST API

### Databases

- PostgreSQL

### Infrastructure

- Docker
- Docker Compose
- Linux CLI

### Code Quality

- Ruff

### Version Control

- Git
- GitHub

---

## Current Implementation

### API Automation

- Reusable API Client based on `requests.Session`
- Configurable request timeout
- Default HTTP headers
- Centralized API Endpoints layer
- API Service layer
- API smoke tests
- Pytest fixtures for reusable test components

### Framework Architecture

- Layered project structure
- Separation of API Client, Endpoints and API Services
- Centralized project configuration
- Reusable testing infrastructure

### Development Workflow

- Feature branches
- Pull Request workflow
- Dockerized backend for testing

---

## Repository Structure

```text
qa-engineering-lab/
│
├── framework/
│   ├── api/
│   ├── clients/
│   ├── config/
│   ├── endpoints/
│   ├── pages/
│   └── utils/
│
├── tests/
│   ├── api/
│   ├── database/
│   ├── messaging/
│   ├── performance/
│   └── ui/
│
├── external/
│   └── ecommerce/
│
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## Existing Tests

Currently implemented:

- API Client initialization
- Configuration validation
- Products API smoke test

---

## Running Tests

Run all tests:

```bash
pytest
```

Run static analysis:

```bash
ruff check .
```

---

## Roadmap

- API response models (Pydantic)
- Authentication layer
- Database validation
- Negative API testing
- UI Automation (Playwright)
- Kafka testing
- RabbitMQ testing
- Allure Reports
- GitHub Actions CI/CD

---

## Project Status

🚧 Actively developing a production-like QA Automation Framework.

Current focus:

- REST API automation
- Framework architecture
- Clean code
- Test infrastructure
