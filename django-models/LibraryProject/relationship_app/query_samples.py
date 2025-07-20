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
    # Query all books by a specific author using the author's name
    author_name = "Jane Austen"
    author = Author.objects.get(name=author_name)
    print(f"Books by {author.name}:")
    books = Book.objects.filter(author=author)
    for book in books:
        print(f" - {book.title}")

    # List all books in a library by name
    library_name = "Main Library"  # Replace with a real library name in your DB
    library = Library.objects.get(name=library_name)
    print(f"\nBooks in library '{library.name}':")
    for book in library.books.all():
        print(f" - {book.title}")

    # Retrieve the librarian for a library
    librarian = library.librarian
    print(f"\nLibrarian of '{library.name}': {librarian.name}")


    library_name = "My Library" 
    library = Library.objects.get(name=library_name)
    print(f"\nBooks in library '{library.name}':")
    for book in library.books.all():
        print(f" - {book.title}")

    # Retrieve the librarian for a library
    librarian = library.librarian
    print(f"\nLibrarian of '{library.name}': {librarian.name}")

if __name__ == '__main__':
    run_queries()
