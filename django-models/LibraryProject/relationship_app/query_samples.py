import os
import sys
import django

#  Add the root project directory (where manage.py is) to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Query all books by a specific author (e.g., Author with id=1)
    author = Author.objects.get(id=1)
    print(f"Books by {author.name}:")
    for book in author.books.all():
        print(f" - {book.title}")

    # List all books in a library (e.g., Library with id=1)
    library = Library.objects.get(id=1)
    print(f"\nBooks in library '{library.name}':")
    for book in library.books.all():
        print(f" - {book.title}")

    # Retrieve the librarian for a library
    librarian = library.librarian
    print(f"\nLibrarian of '{library.name}': {librarian.name}")

if __name__ == '__main__':
    run_queries()
