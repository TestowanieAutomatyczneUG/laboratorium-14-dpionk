from src.Author import Author
from src.ISBNnumber import ISBNnumber


class Book:
    def __init__(self, title, author, isbn):
        if type(title) is not str or title ==  "":
            raise ValueError("Podano błędny tytuł")
        if not isinstance(author, Author):
            raise ValueError("Podano błędnego autora")
        if not ISBNnumber().check(isbn):
            raise ValueError("Podano błędny ISBN numer")
        self.title = title
        self.author = author
        self.isbn = isbn