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

    def check_value(self, value: Any, name: str,) -> None:
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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
