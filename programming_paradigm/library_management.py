class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False
    def return_book(self):
        """Return a book by title."""
        for book in self.__books:
            if book.title == title and book.is_checked_out:
                book.is_checked_out = False

class Library:
    def __init__(self):
        self.__books = []
    def add_book(self, book):
        """Add a book to the library."""
        self.__books.append(book)
    def list_available_books(self):
        """list all available books in the library."""
        for book in self.__books:
            if not book.is_checked_out:
                print(f"{book.title} by {book.author}")
    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self.__books:
            if book.title == title and not book.is_checked_out:
                book.is_checked_out = True
    