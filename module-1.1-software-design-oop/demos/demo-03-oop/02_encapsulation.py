class Book:
    """A book with protected data."""

    def __init__(self, title, author):
        self._title = title
        self._author = author

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def set_title(self, title):
        if len(title) > 0:
            self._title = title
        else:
            print("Title cannot be empty.")

    def display_info(self):
        print(f"{self._title} - {self._author}")


def main():
    book = Book("Clean Code", "Robert C. Martin")

    book.display_info()

    book.set_title("The Pragmatic Programmer")

    book.display_info()


if __name__ == "__main__":
    main()