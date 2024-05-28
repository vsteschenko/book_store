from rest_framework.test import APITestCase 
from django.urls import reverse
from store.models import Book, UserBookRelation
from store.serializers import BookSerializer
from django.contrib.auth.models import User
import json

class BooksApiTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username="test_username")
        self.book_1 = Book.objects.create(name='book 1', price="25.00", author_name="Author 1", owner=self.user)
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

class BookRelationTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_username',)
        self.user2 = User.objects.create(username='test_username2',)
        self.book_1 = Book.objects.create(name='Test book 1', price=25, author_name='Author 1', owner=self.user)
        self.book_2 = Book.objects.create(name='Test book 2', price=55, author_name='Author 5')

    def test_like(self):
        url = reverse('userbookrelation-detail', args=(self.book_1.id, ))
        data = {
                "like": True,
            }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.patch(url, data=json_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        relation = UserBookRelation.objects.get(user=self.user, book=self.book_1)
        self.assertTrue(relation.like)

        data = {
                "in_bookmarks": True,
            }
        json_data = json.dumps(data)
        response = self.client.patch(url, data=json_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        relation = UserBookRelation.objects.get(user=self.user, book=self.book_1)
        self.assertTrue(relation.in_bookmarks)
        
    def test_rate(self):
        url = reverse('userbookrelation-detail', args=(self.book_1.id, ))
        data = {
                "rate": 3,
            }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.patch(url, data=json_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        relation = UserBookRelation.objects.get(user=self.user, book=self.book_1)
        self.assertTrue(relation.rate)
    
    def test_rate_wrong(self):
        url = reverse('userbookrelation-detail', args=(self.book_1.id, ))
        data = {
                "rate": 6,
            }
        json_data = json.dumps(data)
        self.client.force_login(self.user)
        response = self.client.patch(url, data=json_data, content_type='application/json')
        self.assertEqual(response.status_code, 200, response.data)
        relation = UserBookRelation.objects.get(user=self.user, book=self.book_1)
        self.assertTrue(relation.rate)