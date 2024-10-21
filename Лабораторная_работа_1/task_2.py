symbol = 4 # Вес символа

line = 25 # Кол-во символов в строке
line_weight = symbol * line # Вес строки в байтах

page = 50 # Кол-во строк на странице
page_weight = page * line_weight # Вес страницы в байтах

book = 100 # Кол-во страниц в книге
book_weight = book * page_weight # Вес книги в байтах

diskette = 1.44 # Объем дискеты в Мб
diskette_in_bytes = diskette * pow(1024, 2) # Объем дискеты в байтах

amount = int(diskette_in_bytes / book_weight) # Допустимое кол-во книг на дискете

print("Количество книг, помещающихся на дискету:", amount)
