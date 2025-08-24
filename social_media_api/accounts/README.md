# Social Media API

A Django REST Framework API with custom user authentication.

## Features
- Custom user model with `bio`, `profile_picture`, `followers`.
- Token-based authentication.
- Endpoints for register, login, and profile management.

## Setup
```bash
git clone <repo>
cd social_media_api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
