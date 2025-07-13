# Create Book

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# <Book: 1984 by George Orwell (1949)>


# Retrieve Book

```python
book = Book.objects.get(title="1984")
book.title        # '1984'
book.author       # 'George Orwell'
book.publication_year  # 1949



# Update Book Title

```python
book.title = "Nineteen Eighty-Four"
book.save()
book
# <Book: Nineteen Eighty-Four by George Orwell (1949)>



# Delete Book

```python
book.delete()
Book.objects.all()
# <QuerySet []>
