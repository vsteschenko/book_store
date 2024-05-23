from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    filterset_fields = ['price']
    search_fields = ['name', 'author_name']
    ordering_field = ['price', 'author_name', 'id']

def auth(request):
    return render(request, 'oauth.html')