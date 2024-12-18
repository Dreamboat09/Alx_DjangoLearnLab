import mysql.connector
import .models

try:
    mydb = mysql.connector.connect(
        host = 'localhost'
        user = 'root'
        passwd = 'dreamboat'
    )
    
    mycursor = mydb.cursor
    
    findbyauthor = Book.objects.filter(Author)
    
    allbook = Book.object.all
    
    librarian =  Library.object(Librarian)
    
    
except: 
    mydb = mysql.connector.error
    print('error')
    
finally:
    if mydb = mysql.connector.connect:
        mycursor.close()
        mydb.close
    
    else:
        print('error')
        
     