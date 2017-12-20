#BOOKSTORES
class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.authors = []
        self.Books = []
    
    # Adding Books
    def add_book(self, book):
        self.Books.append(book)
    
    # Display all Books
    def get_books(self):
        return self.Books
    
    # Search Books by Title/Author
    def search_books(self, title=None, author=None):
        result = []
        if title != None: 
            for Book in self.Books:
                if title.lower() in Book.title.lower():
                    result.append(Book)

            return result
            
        if author != None:
            for Book in self.Books:
                if author.name.lower() in Book.author.name.lower():
                    result.append(Book)

            return result
    
#AUTHORS
class Author(object):
    def __init__(self, name, nation):
        self.name = name
        self.nationality = nation
        self.books = []
        
    def get_books(self):
        return self.books


#BOOKS
class Book(object):
    def __init__(self, name, author):
        self.title = name
        self.author = author
        self.author.books.append(self)
        
