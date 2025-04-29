# Core Django Project Architecture

This repository provides a well-structured and scalable architecture for Django projects. It is designed to meet the needs of enterprise-grade applications while maintaining clean and modular code organization.


## Overview

This Django architecture is designed for **scalable, clean, and enterprise-grade development**, incorporating:

- Service and repository pattern
- Modular app organization
- API versioning
- Separate environment configurations
- Dockerized deployment for dev/staging/prod
- Integrated test framework and pre-commit hooks
- Common shared logic (utils, enums, constants, base models)
- Project-level fixtures, asset management, pgAdmin support

```bash

core/
├── config/                                  # Django core settings and startup
│   ├── __init__.py
│   ├── asgi.py
│   ├── wsgi.py
│   ├── urls.py                              # Root URL configuration
│   └── settings/                            # Environment-based settings
│       ├── __init__.py
│       ├── base.py                          # Shared settings
│       ├── local.py                         # Local development settings
│       └── production.py                    # Production settings
├── apps/                                    # All Django apps go here
│   ├── __init__.py
│   ├── user/                                # Sample app (repeat this structure)
│   │   ├── __init__.py
│   │   ├── models/
|   │   |    ├── __init__.py
│   │   |    ├── user.py
│   │   ├── services/                        # Business logic layer
│   │   │   ├── __init__.py
│   │   │   └── user_service.py
│   │   ├── repositories/                    # Data access layer
│   │   │   ├── __init__.py
│   │   │   └── user_repository.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── v1/                          # Versioned API
│   │   │       ├── __init__.py
│   │   │       └── urls.py
│   │   ├── views/
│   │   │       ├── __init__.py
│   │   │       └── user_view.py
│   │   ├── serializers/
│   │   │       ├── __init__.py
│   │   │       └── user_serializer.py
│   │   ├── enums.py                         # Custom enums for this app
│   │   ├── constants.py                     # Static values/constants
│   │   ├── utils.py                         # App-level helper functions
│   │   ├── management/
│   │   │   ├── __init__.py
│   │   │   └── commands/                    # Custom Django management commands
│   │   │       ├── __init__.py
│   │   │       └── seed_user.py
│   │   ├── fixtures/                        # JSON fixtures for test/demo data
│   │   │   └── user_fixture.json
│   │   └── tests/                           # Unit tests for this app
│   │       ├── __init__.py
│   │       ├── test_models.py
│   │       ├── test_views.py
│   │       └── test_services.py
├── common/
│   ├── __init__.py
│   ├── base_model.py               # Abstract base model
│   ├── services/
│   │   ├── __init__.py
│   │   └── email_service.py
│   ├── validators/
│   │   └── __init__.py
│   ├── exceptions/
│   │   └── __init__.py
│   ├── enums/
│   │   └── __init__.py
│   ├── constants/
│   │   └── __init__.py
│   ├── helpers/
│   │   └── __init__.py
│   ├── utils.py
│   └── base_repository.py
├── templates/                               # Shared templates (if applicable)
│   └── base.html
├── static/                                  # Static files
│   └── css/
├── media/                                   # Media file uploads
├── assets/                                  # Additional frontend/static assets
│   ├── images/
│   ├── fonts/
│   └── svg/
├── compose/                                 # Docker-specific configurations
│   ├── local/
│   │   ├── django/
│   │   │   ├── Dockerfile                   # Local dev Dockerfile
│   │   │   └── entrypoint.sh                # Entrypoint script
│   │   ├── pgadmin/
│   │   │   └── Dockerfile
│   │   └── env/
│   │       └── django.env
│   ├── staging/
│   │   ├── django/
│   │   │   └── Dockerfile
│   │   └── env/
│   │       └── django.env
│   ├── production/
│   │   ├── django/
│   │   │   └── Dockerfile
│   │   └── env/
│   │       └── django.env
├── docker-compose.yml                       # Local development
├── docker-compose.override.yml              # Override for local only
├── docker-compose.staging.yml               # Staging environment
├── docker-compose.prod.yml                  # Production environment
|
├── requirements/                            # Environment-based Python deps
│   ├── base.txt
│   ├── local.txt
│   └── production.txt
|
├── .env.dev                                 # Local .env file
├── .env.staging                             # Staging .env
├── .env.production                          # Production .env
|
├── .pre-commit-config.yaml                  # Code quality tools config
├── pyproject.toml                           # black, mypy, isort, etc.
├── pytest.ini                               # Pytest config
├── manage.py
├── README.md
└── Makefile                                 # Common dev commands
```


## App Layout Standards

Each app follows this structure:

```
apps/
└── your_app/
    ├── services/           # Business logic
    ├── repositories/       # Data access layer
    ├── api/v1/             # Versioned API views and serializers
    ├── enums.py            # Custom enums
    ├── constants.py        # Static values
    ├── utils.py            # App-level helpers
    ├── fixtures/           # App-specific JSON fixtures
    ├── management/         # Custom management commands
    └── tests/              # Unit tests by layer
```


## Code Quality & Tooling

Pre-commit tools:

- `black` — Code formatting
- `flake8` — Linting
- `mypy` — Type checking
- `isort` — Import sorting

Config files:

- `.pre-commit-config.yaml`
- `pyproject.toml`

Install hooks:

```bash
pre-commit install
```





### Architecture Design by

This architecture was thoughtfully designed to support **enterprise-level Django projects**, prioritizing clean code separation, modular development, and a smooth onboarding experience for both solo developers and teams.


- **Name:** *Kawsar A.Foysal*  
- **GitHub:** [github.com/iamfoysal](https://github.com/iamfoysal)   
- **Role:** Software Engineer | Django Expert | System Designer

### 🤝 Contributors

We welcome and appreciate every contributor who helps improve this project. Your code, documentation, testing, or feedback all matter.

To contribute:

1. Fork the repository
2. Create a branch for your feature/bugfix
3. Submit a pull request with clear description

### ⭐ Show Your Support

If you find this project helpful:

- **Star it on GitHub** to show your appreciation  
- **Share it** with other Django developers or teams  
- **Contribute** ideas, features, bug reports, or improvements  

> Your support helps keep this project alive and evolving for the community!

---
