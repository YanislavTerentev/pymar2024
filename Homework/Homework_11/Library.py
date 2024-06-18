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
                print('You are already reserved this book')
                return False
            print('Book is already reserved')
            return False
        if book.is_taken:
            if book.username_take == self.username:
                print('You are already taken this book')
                return False
            print('Book is already taken')
            return False
        book.is_reserved = True
        book.username_take = self.username
        print('Book is reserved by: ' + self.username)
        return True

    def take_book(self, book):
        if book.is_taken:
            if book.username_take == self.username:
                print('You are already taken this book')
                return False
            print('Book is already taken')
            return False
        if book.is_reserved:
            if book.username_take == self.username:
                book.is_reserved = False
                book.is_taken = True
                print('Book is yours: ' + self.username)
                return True
            print('Book is already reserved')
            return False
        book.is_taken = True
        book.username_take = self.username
        print('Book is yours: ' + self.username)
        return True

    def return_book(self, book):
        if book.is_taken:
            if book.username_take == self.username:
                book.is_taken = False
                book.username_take = None
                print('Thank you for returning this book')
                return True
            print('It\'s not your book')
            return False
        if book.is_reserved:
            if book.username_take == self.username:
                print('You cannot return book that is reserved by you')
                return False
            print('You cannot return book reserved by another user')
            return False
        print('You cannot return book that was not taken')
        return False


book1 = Book('Fahrenheit 451', 'Ray Bradbury', 224, '9780307475312')
book2 = Book('The First Days', 'Rhiannon Frater', 331, '9785196581699')
book3 = Book('Dead of Night', 'Jonathan Maberry', 358, '9741271522013')
book4 = Book('Dead City', 'Joe McKinney', 288, '9785171598236')

user1 = User('Steve Smith')
user2 = User('John Silver')

assert user1.reserve_book(book1), "error"
assert user1.take_book(book1), "error"
assert not user2.return_book(book1), "error"
