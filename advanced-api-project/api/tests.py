from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user for authenticated requests
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create an author
        self.author = Author.objects.create(name="J.K. Rowling")

        # Create a book
        self.book = Book.objects.create(
            title="Harry Potter",
            publication_year=1997,
            author=self.author
        )

        # Endpoints
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', args=[self.book.id])
        self.delete_url = reverse('book-delete', args=[self.book.id])

    # --- CRUD Tests ---

    def test_list_books(self):
        """Test listing books is accessible to anyone"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_single_book(self):
        """Test retrieving a single book by ID"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Harry Potter")

    def test_create_book_requires_authentication(self):
        """Test creating a book without authentication is denied"""
        data = {
            "title": "New Book",
            "publication_year": 2000,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """Test creating a book with authentication"""
        self.client.login(username="testuser", password="testpass")
        data = {
            "title": "New Book",
            "publication_year": 2000,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book_authenticated(self):
        """Test updating a book with authentication"""
        self.client.login(username="testuser", password="testpass")
        data = {"title": "Updated Book", "publication_year": 1999, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book_authenticated(self):
        """Test deleting a book with authentication"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # --- Filtering, Searching, Ordering Tests ---

    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url, {'title': 'Harry Potter'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get(self.list_url, {'search': 'Harry'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_order_books_by_publication_year(self):
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

