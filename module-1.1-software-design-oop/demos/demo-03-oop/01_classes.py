class Book:
    """A simple class representing a book."""

    def __init__(self, title, author):
        self.title = title
        self.author = author


def main():
    book1 = Book("The Pragmatic Programmer", "Andrew Hunt")
    book2 = Book("Clean Code", "Robert C. Martin")

    print(book1)
    print(book2)


if __name__ == "__main__":
    main()
