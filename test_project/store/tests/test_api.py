from rest_framework.test import APITestCase 
from django.urls import reverse
from store.models import Book
from store.serializers import BookSerializer

class BooksApiTestCase(APITestCase):
    def  test_get(self):
        book_1 = Book.objects.create(name='Three body problem', price="25.00")
        book_2 = Book.objects.create(name='Crime and Punishment', price="35.00")
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BookSerializer([book_1, book_2], many=True).data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer_data, response.data)