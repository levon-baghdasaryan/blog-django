# Blog Project

## Tech Stack
* Python 3.11
* Django 4.2
* MySql

## Installation
1. `cp .env.example .env` - create .env file
2. `python -m venv venv` - create environment file
3. `venv\Scripts\activate` (OS) or `venv\bin\activate`(Mac/Linux) - activate the environment
4. `pip install -r requirements/prod.txt` - install the project stack
5. `pip install -r requirements/dev.text` - install the stack for development
6. `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'` - generate a secret key and assign to SECRET_KEY on .env
7. Edit .env file

## Other
* Run `flake8` to format the code (usually before commit)