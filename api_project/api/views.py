'''Authentication Setup:
- Token-based auth enabled via `rest_framework.authentication.TokenAuthentication`.
- All API endpoints require authentication by default (IsAuthenticated).
- Users obtain tokens via: POST /api/auth/token/ (username + password)
- Include token in headers for access: Authorization: Token <token>
'''

from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[IsAuthenticated]


