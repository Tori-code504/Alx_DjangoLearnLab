from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# List all books
class BookListView(generics.ListAPIView):
    """
    Retieves a list of all books
    Accessible to anyone(no authentication required).
    """ 
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

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


