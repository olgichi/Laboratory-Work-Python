# TODO Найдите количество книг, которое можно разместить на дискете
disk_volume = 1.44 # размер в мб
n_pages = 100
n_line = 50
n_symb = 25
symb_volume = 4 # размер в байтах

book_volume = n_pages*n_line*n_symb*symb_volume
count_books = int((disk_volume*1024*1024)//book_volume)
# или можно было бы сделать так:
count_books = round((disk_volume*1024*1024)//book_volume)
print("Количество книг, помещающихся на дискету:", count_books)
