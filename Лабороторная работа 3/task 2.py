# TODO Напишите функцию find_common_participants
def f(str_1, str_2, q = ', '):
    return sorted(list(set(str_2.split(q)).intersection(set(str_1.split(q)))))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(f(participants_first_group,participants_second_group, q = '|'))