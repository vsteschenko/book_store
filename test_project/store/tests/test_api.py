from rest_framework.test import APITestCase 
from django.urls import reverse
from store.models import Book
from store.serializers import BookSerializer

class BooksApiTestCase(APITestCase):

    def setUp(self):
        self.book_1 = Book.objects.create(name='book 1', price="25.00", author_name="Author 1")
        self.book_2 = Book.objects.create(name='book 2', price="35.00", author_name="Author 5")
        self.book_3 = Book.objects.create(name='book Author 1', price="35.00", author_name="Author 2")

    def test_get(self):
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BookSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('book-list')
        response = self.client.get(url, data={"search": "Author 1"})
        serializer_data = BookSerializer([self.book_1, self.book_3], many=True).data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer_data, response.data)