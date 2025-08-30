# api/views.py
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class TestView(APIView):
    def get(self, request):
        return Response({
            "message": "API is working!",
            "status": "success"
        })