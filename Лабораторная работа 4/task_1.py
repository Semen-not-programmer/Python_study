import doctest
from typing import Union
from typing import Any


class Properties:
    """
    Класс описывает сторение тела человека и задаёт его уровень фикической активности
    Является родительским для класса Calories
    """
    def __init__(self,
                 mass: Union[int, float],
                 expenditure: Union[int, float]) -> None:
        """
        Инициализация входных данных
        mass - масса чаловека [кг]
        expenditure - расход калорий [ккал/час*кг]
        """
        self._mass = mass
        self._expenditure = expenditure

    @staticmethod
    def checking(value: Any, name: str,
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

    @staticmethod
    def is_positive(value: Union[int, float]) -> None:
        if value < 0:
            raise ValueError('Выражение может принимать только положительные значения')

    def __str__(self):
        return f"Расход {self._expenditure} ккал/час. Масса {self._mass} кг"

    def __repr__(self):
        return f"{self.__class__.__name__}(mass={self._mass!r}, expenditure={self._expenditure!r})"

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value):
        self.checking('mass', value, (int, float))
        self.is_positive(value)
        self._mass = value

    @property
    def expenditure(self):
        return self._expenditure

    @expenditure.setter
    def expenditure(self, value):
        self.checking('expenditure', value, (int, float))
        self.is_positive(value)
        self._expenditure = value


class Calories (Properties):
    """
    Класс, описывающий запас калорий вследствие употребления пищи и
    деятельности
    Допускает трату калорий при прохождении времени, изменение основных
    параметров
    Выводит значения основных параметров
    Наследует атрибуты mass и expenditure
    """
    def __init__(self,
                 calories: Union[int, float],
                 mass: Union[int, float],
                 expenditure: Union[int, float]) -> None:
        """
        Инициализация входных данных
        calories - начальное значение запаса калорий [ккал]
        mass - масса чаловека [кг]
        expenditure - расход калорий [ккал/час*кг]
        """
        super().__init__(mass, expenditure)
        self._calories = calories
        # Исходное время
        self._time = 0

    def spend_time(self,
                   delta_time: Union[int, float]) -> None:
        """
        Метод рассчитывает прошедшее за время работы программы время
        delta_time - прошедшее время [час]
        >>> d = Calories(4000, 50, 6)
        >>> d.spend_time(0.5)
        >>> d.calories
        3850.0
        >>> d.time
        0.5
        """
        self.checking(delta_time, 'expenditure', (int, float))
        if delta_time < 0:
            raise ValueError(f'Прошедшее время {delta_time} не может быть '
                             'отрицательным')
        self._time += delta_time
        self._calories -= delta_time * self._expenditure * self._mass

    def change_work(self,
                    new_expenditure: Union[int, float]) -> None:
        """
        Изменение стандартного расхода калорий
        new_expenditure - значение нового расхода калорий [ккал/час*кг]
        >>> d = Calories(4000, 50, 6)
        >>> d.change_work(10)
        >>> d.expenditure
        10
        """
        self.checking(new_expenditure, 'new_expenditure', (int, float))
        self._expenditure = new_expenditure

    def work(self,
             work_expenditure: Union[int, float],
             work_time: Union[int, float]) -> None:
        """
        Расчитывает затраты на соывершение работы с заданными параметрами
        work_expenditure - расход калорий на килограмм во время работы
        [ккал/час*кг]
        work_time - продолжительность работы [час]
        >>> d = Calories(4000, 50, 6)
        >>> d.work(10, 3)
        >>> d.calories
        2500
        >>> d.time
        3
        """
        self.checking(work_expenditure, 'work_expenditure', (int, float))
        self.checking(work_time, 'work_time', (int, float))
        self._calories -= work_expenditure * work_time * self._mass
        self._time += work_time

    def eat(self,
            new_calories: Union[int, float]):
        """
        Модуль, отвечающий за пополнение калорий
        >>> d = Calories(4000, 50, 6)
        >>> d.eat(100)
        >>> d.calories
        4100
        """
        self.checking(new_calories, 'new_calories', (int, float))
        self._calories += new_calories

    def output(self) -> None:
        """
        Вывод требуемых параметров
        """
        output_dict = {'Запас калорий' if self._calories >= 0
                       else 'Недостаток калорий': self._calories,
                       'Расход калорий в час на килограмм': self._expenditure,
                       'Прошедшее время': self._time}
        for name, data in output_dict.items():
            print(f'{name}: {data}')

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        self.checking('calories', value, (int, float))
        self.is_positive(value)
        self._calories = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self.checking('time', value, (int, float))
        self.is_positive(value)
        self._time = value

    def __str__(self):  # Можно добавить последний параметр после вызова str родительского класса
        q = super().__str__()
        return f"Калории {self._calories} ккал. {super().__str__()}"

    def __repr__(self): # Нужно вставить calories в середину repr
        return f"{self.__class__.__name__}(calories={self._calories!r}, mass={self._mass!r}, expenditure={self._expenditure!r})"


if __name__ == "__main__":
    doctest.testmod()
    t_1 = Calories(3000, 80, 200)
    print(t_1)
    print(repr(t_1))

    t_2 = Properties(60, 30)
    print(t_2)
    print(repr(t_2))

