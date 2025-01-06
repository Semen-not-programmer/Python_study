from typing import Union
from typing import Any

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    """
    Класс описывает параметры книги
    """

    def __init__(self,
                 id_: int,
                 name: str,
                 pages: int) -> None:
        """
        Инизиализация входных данных
        id_ - идентификатор книги,
        name - название,
        pages - количество страниц
        """
        self.check_type(id_, 'id_', int)
        self.check_value(id_, 'id_')
        self.id_ = id_

        self.check_type(name, 'name', str)
        self.name = name

        self.check_type(pages, 'pages', int)
        self.check_value(pages, 'pages')
        self.pages = pages

    def check_type(self,
                   value: Any, name: str,
                   type_check: Union[type, tuple]) -> None:
        """
        Метод проверяет соответствие входных типов данных требуемым значениям
        value - входное значение
        name - имя переменной (для оформления)
        type_check - требуемый тип или кортеж требуемых типов
        """
        if not isinstance(value, type_check):
            raise TypeError(
                f'Переменная {name} может принимать только '
                f'значения типа {type_check}')

    def check_value(self, value: Any, name: str, ) -> None:
        """
        Метод проверяет, положительны ли значения входных данных
        value - входное значение
        name - имя переменной (для оформления)
        """
        if value < 0:
            raise TypeError(
                f'Переменная {name} может принимать только '
                f'положительные значения')

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id_={self.id_}, name=' \
               f'{self.name!r}, pages={self.pages!r})'


class Library:
    ID_ = 0

    def __init__(self, books=None) -> None:
        """
        Инизиализация входных данных
        books - список элементов класса Book
        id_books - словарь соответсвия порядкового номера книги в классе
                   Library и порядкового номера в классе Book
        """
        if books is None:
            self.books = []
            self.id_books = {}
        else:
            self.books = books
            self.id_books = dict()
            for i in range(len(self.books)):
                self.id_books[self.books[i].id_] = i
                self.increase_id()

    @classmethod
    def increase_id(cls):
        cls.ID_ += 1

    def get_next_book_id(self) -> int:
        return self.__class__.ID_ + 1

    def get_index_by_book_id(self, id_) -> int:
        try:
            return self.id_books[id_]
        except KeyError:
            return "Книги с запрашиваемым id не существует"


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(
        empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"],
             pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
    # print(library_with_books.get_index_by_book_id(3))
