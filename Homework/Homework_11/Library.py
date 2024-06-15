class Book:
    def __init__(self, title, author, pages, ISBN):
        self.title = title
        self.author = author
        self.pages = pages
        self.ISBN = ISBN
        self.is_reserved = False
        self.is_taken = False
        self.username_take = None


class User:
    def __init__(self, username):
        self.username = username

    def reserve_book(self, book):
        if book.is_reserved:
            if book.username_take == self.username:
                return 'You are already reserved this book'
            return 'Book is already reserved'
        if book.is_taken:
            if book.username_take == self.username:
                return 'You are already taken this book'
            return 'Book is already taken'

        book.is_reserved = True
        book.username_take = self.username
        return 'Book is reserved by: ' + self.username

    def take_book(self, book):
        if book.is_taken:
            if book.username_take == self.username:
                return 'You are already taken this book'
            return 'Book is already taken'
        if book.is_reserved:
            if book.username_take == self.username:
                book.is_reserved = False
                book.is_taken = True
                return 'Book is yours: ' + self.username
            return 'Book is already reserved'
        book.is_taken = True
        book.username_take = self.username
        return 'Book is yours: ' + self.username

    def return_book(self, book):
        if book.is_taken:
            if book.username_take == self.username:
                book.is_taken = False
                book.username_take = None
                return 'Thank you for returning this book'
            return 'It\'s not your book'
        if book.is_reserved:
            if book.username_take == self.username:
                return 'You cannot return book that is reserved by you'
            return 'You cannot return book reserved by another user'
        return 'You cannot return book that was not taken'


book1 = Book('Fahrenheit 451', 'Ray Bradbury', 224, '9780307475312')
book2 = Book('The First Days', 'Rhiannon Frater', 331, '9785196581699')
book3 = Book('Dead of Night', 'Jonathan Maberry', 358, '9741271522013')
book4 = Book('Dead City', 'Joe McKinney', 288, '9785171598236')

user1 = User('Steve Smith')
user2 = User('John Silver')

assert user1.reserve_book(book1) == 'Book is reserved by: Steve Smith'
assert user1.take_book(book1) == 'Book is yours: Steve Smith'
assert user2.return_book(book1) == 'It\'s not your book'
