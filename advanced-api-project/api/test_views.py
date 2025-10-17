from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User
from datetime import datetime


class BookListViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass', email='user@test.com')
        self.client.login(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

        #create sample authors
        author1 = Author.objects.create(name="William S. Vincent")
        author2 = Author.objects.create(name="Daniel Roy Greenfeld")
        author3 = Author.objects.create(name="Mark Lutz")

        # Create sample books
        Book.objects.create(title="Django for Beginners", author=author1, publication_year=2018)
        Book.objects.create(title="Two Scoops of Django", author=author2, publication_year=2019)
        Book.objects.create(title="Learning Python", author=author3, publication_year=2013)

    def test_list_books(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_filter_books_by_author(self):
        response = self.client.get('/books/', {'author': 'William S. Vincent'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Django for Beginners")

    def test_search_books_by_title(self):
        response = self.client.get('/books/', {'search': 'Django'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_books_by_published_date(self):
        response = self.client.get('/books/', {'ordering': 'publication_date'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['title'], "Two Scoops of Django")

    def test_create_book(self):
        author4 = Author.objects.create(name="Brett Slatkin")
        new_book_data = {
            'title': "Effective Python",
            'author': author4,
            'publication_year': 2015
        }
        response = self.client.post('/books/create/', new_book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, "Effective Python")

    def test_update_book(self):
        book = Book.objects.first()
        updated_data = {
            'title': "Django for Professionals",
            'author': book.author,
            'publication_year': book.publication_year,
        }
        response = self.client.put(f'/books/update/{book.id}/', updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.title, "Django for Professionals")

    def test_delete_book(self):
        book = Book.objects.first()
        response = self.client.delete(f'/books/delete/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)