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

    def display_pages(self):
        print(f"Pages: {self.pages}")


def main():
    book = PrintedBook(
        "Clean Code",
        "Robert C. Martin",
        464,
    )

    book.display_info()
    book.display_pages()


if __name__ == "__main__":
    main()
