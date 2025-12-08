# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
lines = 50
sim = 25
bytes = 4
volume = 1.44

book = pages * lines * sim * bytes
volume_in_bytes = volume * 1024**2

count = volume_in_bytes / book
print("Количество книг, помещающихся на дискету:", int(count))