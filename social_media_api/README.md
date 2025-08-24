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

Endpoints

GET /api/posts/ — list (paginated, search=, ordering=created_at|-created_at)

POST /api/posts/ — create (auth)

GET /api/posts/{id}/ — retrieve

PUT/PATCH /api/posts/{id}/ — update (owner only)

DELETE /api/posts/{id}/ — delete (owner only)

GET /api/comments/ — list (paginated, post=<post_id>, search=, ordering=)

POST /api/comments/ — create (auth)

GET /api/comments/{id}/ — retrieve

PUT/PATCH /api/comments/{id}/ — update (owner only)

DELETE /api/comments/{id}/ — delete (owner only)