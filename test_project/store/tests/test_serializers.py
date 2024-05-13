from django.test import TestCase
from store.models import Book
from store.serializers import BookSerializer

class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Three body problem', price="25.00")
        book_2 = Book.objects.create(name='Crime and Punishment', price="35.00")
        data = BookSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Three body problem',
                'price': '25.00'
            }, 
            {
                'id': book_2.id,
                'name': 'Crime and Punishment',
                'price': '35.00'
            }
        ]
        self.assertEqual(expected_data, data)