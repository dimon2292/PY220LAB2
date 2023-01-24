from typing import Optional


class Book:
    def __init__(self, id, name, pages):
        self.id = id
        self.name = name
        self.pages = pages

    def __repr__(self):
        return f"Book(id = {self.id}, name = {self.name}, pages = {self.pages})"

    def __str__(self):
        return f"Книга {self.name}"


book1 = Book(id=10, name='test_name_1', pages=200)
book2 = Book(id=50, name='Python', pages=700)
book3 = Book(id=106, name='Python', pages=700)


class Library:
    def __init__(self, *attr_: Optional[Book]):
        self.books = []
        if attr_:
            self.books.append(attr_)

    def get_next_book_id(self) -> int:
        """
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку
        :return: идентификатор последней книги увеличенный на 1.
        """

        if not self.books:
            self.ident = 1
            return self.ident
        if self.books:
            self.tuple_ = self.books[0]
        index = 0
        id_last_book = 0
        for i, j in enumerate(self.tuple_):
            if i > index:
                index = i
                id_last_book = j.id
        return id_last_book + 1

    def get_index_by_book_id(self, ident=None) -> int:
        """
       Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.
       :param ident: идентификатор книги
       :return: натуральное число
       """
        self.tuple_ = self.books[0]
        for i, j in enumerate(self.tuple_):
            if j.id == ident:
                return f"индекс данной книги в списке: {i}"

    def __str__(self):
        return f"в этой библиотеке есть книги {self.books}"


Library1 = Library(book1, book2, book3)

print(Library1.get_index_by_book_id(106))
