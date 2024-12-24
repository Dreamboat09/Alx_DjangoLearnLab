import mysql.connector
from .models import Book, Author, Library, Librarian

try:
    mydb = mysql.connector.connect(
        host = 'localhost'
        user = 'root'
        passwd = 'dreamboat'
        database = 'bookDB'
        )
    
    mycursor = mydb.cursor
    
    def book_by_author(author_name):
        try:
            authors = Author.objects.get(author_name)
            books = Book.objects.filter(Author=authors)
            return books
        except books.DoesNotExist:
            return[]
            
    def book_in_a_library(library_name):
        try:
            Librarys = Library.objects.get(library_name)
            books = Book.objects.filter(Library=Librarys)
            return books
        except books.DoesNotExist:
            return []
        
    def libarian_by_library(library_name):
        try:
            Librarys = Library.objects.get(library_name)
            Librarians = Librarian.objects.filter(Library=Librarys)
            return Librarians
        except Librarians.DoesNotExist:
            return []
            
    
except:
    mydb = mysql.connector.error
    print('error')
    
finally:
    if mydb = mysql.connector.connect
        mycursor.close()
        mydb.close
    
    else:
        print('error')
        
     