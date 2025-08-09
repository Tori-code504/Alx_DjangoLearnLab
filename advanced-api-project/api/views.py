from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# List all books
class BookListView(generics.ListAPIView):
    """
    Retieves a list of all books with support for:
    - Filtering by title, author, and publication_year
    - Searching in title and author name
    - Ordering by title or publication_year
    Accessible to anyone(no authentication required).
    """ 
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Enable filtering, search, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering fields (exact match)
    filterset_fields = ['title', 'author', 'publication_year']

    # Search fields (partial match)
    search_fields = ['title', 'author__name']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']

    # Default ordering
    ordering = ['title']

    def get_queryset(self):
        queryset = Book.objects.all()
        year = self.request.query_params.get('year')
        if year:
            queryset = queryset.filter(publication_year=year)
        return queryset


# Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves details of a single book by its primary key (ID)
    Accessible to anyone
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Create a new book
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book 
    Restricted to authenticated users
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    Updates details of an existing book
    Restricted to authenticated users
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Delete an existing book
class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes an existing book
    Restricted to authenticated users
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

from rest_framework.permissions import BasePermission


