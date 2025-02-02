class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @staticmethod
    def is_positive(value):
        if value < 0:
            raise ValueError

    @staticmethod
    def is_instance(value, type_):
        if not isinstance(value, type_):
            raise TypeError

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.is_instance(value, str)
        self._name = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self.is_instance(value, str)
        self._author = value


class PaperBook (Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        self.is_instance(value, int)
        self.is_positive(value)
        self._pages = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"


class AudioBook (Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, value):
        self.is_instance(value, int)
        self.is_positive(value)
        self._duration = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"


t_1 = Book('Фауст', 'Гёте')
print(t_1)
print(repr(t_1))
print()

t_2 = PaperBook('Репка', 'Народ', 4)
print(t_2)
print(repr(t_2))
print()

t_3 = AudioBook('Пиковая дама', 'Чайковский', 30)
print(t_3)
print(repr(t_3))
t_3.duration = 40
print(repr(t_3))
