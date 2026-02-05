# Parent class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Displays only title and author
    def display_book_details(self):
        print("Title:", self.title)
        print("Author:", self.author)


# Child class inheriting from Book
class IssuedBook(Book):
    def __init__(self, title, author, issued_to, issued_date):
        super().__init__(title, author)
        self.issued_to = issued_to
        self.issued_date = issued_date

    # Displays issued book details
    def display_issued_book_details(self):
        # Calling parent class method using inheritance
        self.display_book_details()
        print("Issued To:", self.issued_to)
        print("Issued Date:", self.issued_date)


# Creating an object of IssuedBook
issued_book = IssuedBook(
    "Python Programming",
    "Guido van Rossum",
    "Pavitra",
    "05-02-2026"
)

# Displaying all details
issued_book.display_issued_book_details()