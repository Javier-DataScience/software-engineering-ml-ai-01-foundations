from abc import ABC, abstractmethod


class Book(ABC):
    """Abstract parent class."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display_info(self):
        """Every type of book must implement this method."""
        pass


class PrintedBook(Book):

    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def display_info(self):
        print(
            f"Printed Book: {self.title} - {self.author} ({self.pages} pages)"
        )


class EBook(Book):

    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def display_info(self):
        print(
            f"EBook: {self.title} - {self.author} ({self.file_size} MB)"
        )


def main():

    library = [
        PrintedBook("Clean Code", "Robert C. Martin", 464),
        EBook("Python Crash Course", "Eric Matthes", 12),
    ]

    for book in library:
        book.display_info()


if __name__ == "__main__":
    main()