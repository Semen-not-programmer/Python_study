# TODO Найдите количество книг, которое можно разместить на дискете
capacity = 1.44 * (1024) ** 2
amount_pages = 100
amount_strings = 50
amount_symbols = 25
symbo_veight = 4

amount_books = int(capacity // (amount_pages * amount_symbols * amount_strings * symbo_veight))

print("Количество книг, помещающихся на дискету:", amount_books)
