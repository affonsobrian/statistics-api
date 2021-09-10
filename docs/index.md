# statistics-api

[![Build Status](https://travis-ci.org/affonsobrian/statistics-api.svg?branch=master)](https://travis-ci.org/affonsobrian/statistics-api)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

API that stores statistics of posts.

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

# Run tests

```bash
python manage.py test
```

# API Docs

- [Authentication](api/authentication.md)
- [Users](api/users.md)
- [Posts](api/posts.md)
- [Posts History](api/posts_history.md)