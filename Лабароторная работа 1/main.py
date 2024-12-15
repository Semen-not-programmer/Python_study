# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union
from typing import Any
from math import sqrt


class Trek:
    """
    Класс, описывающий положение человека относительно начала
    системы коодринат
    Подразуменает изменение положение человека
    Возвращает расстояния относительно различных точек
    Выводит значения основных параметров
    """
    def __init__(self,
                 origin_x: Union[int, float],
                 origin_y: Union[int, float]) -> None:
        """
        Инизиализация входных данных
        origin_x - составляющая x положения человека
        origin_y - составляющая y положения человека
        """
        #Проверка входных данных
        self.checking(origin_x, 'origin_x', (int, float))
        self.origin_x = origin_x
        self.checking(origin_y, 'origin_y', (int, float))
        self.origin_y = origin_y

    def checking(self,
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

    def local_distance(self,
                       local_x: Union[int, float],
                       local_y: Union[int, float]) -> float:
        """
        Возвращает положение человека относительно положения другой точки
        local_x - составляющая x точки отсчёта
        local_y - составляющая y точки отсчёта

        >>> t = Trek(4, 3)
        >>> t.local_distance(3, 3)
        1.0
        """

        distance = sqrt((self.origin_x - local_x) ** 2 +
                        (self.origin_y - local_y) ** 2)
        return distance

    def global_distance(self) -> float:
        """
        Возвращает положение человека относительно начала координат
        >>> t = Trek(4, 3)
        >>> t.global_distance()
        5.0
        """
        distance = self.local_distance(0, 0)
        return distance

    def walk(self,
             walk_x: Union[int, float],
             walk_y: Union[int, float]) -> None:
        """
        Перемещение человека на заданные составляющие в координаткой плоскости
        walk_x - перемежение по оси x
        walk_y - перемежение по оси y
        >>> t = Trek(4, 3)
        >>> t.walk(-2, 6)
        >>> t.origin_x
        2
        >>> t.origin_y
        9
        >>> t.walk(0.5, 0.1)
        >>> t.origin_x
        2.5
        >>> t.origin_y
        9.1
        """
        self.checking(walk_x, 'walk_x', (int, float))
        self.checking(walk_y, 'walk_y', (int, float))
        self.origin_x += walk_x
        self.origin_y += walk_y

    def output(self) -> None:
        """
        Вывод требуемых параметров
        """
        output_dict = {'Cоставляющая x': self.origin_x,
                       'Cоставляющая y': self.origin_y}
        for name, data in output_dict.items():
            print(f'{name}: {data}')


class Calories:
    """
    Класс, описывающий запас калорий вследствие употребления пищи и
    деятельности
    Допускает трату калорий при прохождении времени, изменение основных
    параметров
    Выводит значения основных параметров
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
        self.checking(calories, 'calories', (int, float))
        self.calories = calories
        self.checking(mass, 'mass', (int, float))
        self.mass = mass
        self.checking(expenditure, 'expenditure', (int, float))
        self.expenditure = expenditure
        # Исходное время
        self.time = 0

    def checking(self,
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
        self.time += delta_time
        self.calories -= delta_time * self.expenditure * self.mass

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
        self.expenditure = new_expenditure

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
        self.calories -= work_expenditure * work_time * self.mass
        self.time += work_time

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
        self.calories += new_calories

    def output(self) -> None:
        """
        Вывод требуемых параметров
        """
        output_dict = {'Запас калорий' if self.calories >= 0
                       else 'Недостаток калорий' : self.calories,
                       'Расход калорий в час на килограмм': self.expenditure,
                       'Прошедшее время': self.time}
        for name, data in output_dict.items():
            print(f'{name}: {data}')


class Graduate:
    """
    Класс, отвечающий за учёт оценок учеников
    """
    def __init__(self,
                 name: str,
                 grades: list[Union[int, float]] = []) -> None:
        """
        Инициальзация входных данных
        name - имя студента
        grades - массив его оценок
        """
        self.checking(name, 'name', str)
        self.name = name
        for i in grades:
            self.checking(i, 'grades', (int, float))
            if i > 5 or i < 1:
                raise ValueError('Оценка должна принадлежать диапазону от 1 '
                                 'до 5')
        self.grades = grades

    def checking(self,
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

    def average(self) -> float:
        """
        Счёт среднего балла
        >>> e = Graduate('Q', [3,5,1,2,5,5])
        >>> e.average()
        1.4
        """
        count = 0
        summ = 0
        for i, value in enumerate(self.grades):
            summ += value
            count += i
        average = summ / count
        return average

    def add(self, new_grades: list[Union[int, float]]) -> None:
        """
        Добавление оценок
        >>> e = Graduate('Q', [3,5,1])
        >>> e.add([5,3,1])
        >>> e.grades
        [3, 5, 1, 5, 3, 1]
        """
        for i in new_grades:
            self.checking(i, 'new_grades', (int, float))
            if i > 5 or i < 1:
                raise ValueError('Оценка должна принадлежать диапазону от 1 '
                                 'до 5')
        for i in new_grades:
            self.grades.append(i)

    def output(self) -> None:
        """
        Вывод требуемых параметров
        """
        output_dict = {'Имя ученика': self.name,
                       'Список оценок': self.grades,}
        for name, data in output_dict.items():
            print(f'{name}: {data}')

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()


