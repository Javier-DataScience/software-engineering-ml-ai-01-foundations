class Book:
    """Parent class."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"{self.title} - {self.author}")


class PrintedBook(Book):
    """Child class."""

    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def display_info(self):
        print(
            f"Printed Book: {self.title} - {self.author} ({self.pages} pages)"
        )


class EBook(Book):
    """Child class."""

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