class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for library_book in self.books:
            if book.title == library_book.title and book.author == library_book.author:
                self.books.remove(book)

    def search_books(self, search_string):
        results = []
        for book in self.books:
            if (
                search_string.lower() in book.title.lower() or search_string.lower() in book.author.lower()
            ):
                results.append(book)

        return results
