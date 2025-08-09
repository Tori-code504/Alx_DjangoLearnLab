# Book API Endpoints

## Public Endpoints
- `GET /api/books/` → List all books
- `GET /api/books/<id>/` → Retrieve book by ID

## Authenticated Endpoints
- `POST /api/books/create/` → Create new book
- `PUT /api/books/<id>/update/` → Update book
- `DELETE /api/books/<id>/delete/` → Delete book

### Permissions
- Read (List, Detail) → Open to all users
- Write (Create, Update, Delete) → Requires authentication

### Notes
- Uses DRF generic views (`ListAPIView`, `RetrieveAPIView`, `CreateAPIView`, `UpdateAPIView`, `DestroyAPIView`)
- Custom validation on `publication_year` ensures no future years

# Filtering, Search & Ordering in Book API

## Filtering
- `GET /api/books/?title=<title>` → Filter by exact title
- `GET /api/books/?author=<author_id>` → Filter by author ID
- `GET /api/books/?publication_year=<year>` → Filter by year

## Search
- `GET /api/books/?search=<query>` → Searches in title and author name

## Ordering
- `GET /api/books/?ordering=title` → Ascending order by title
- `GET /api/books/?ordering=-publication_year` → Descending order by publication year
