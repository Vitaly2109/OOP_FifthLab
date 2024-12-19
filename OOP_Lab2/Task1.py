class Publication:
    def __init__(self):
        self.title = ""
        self.price = 0.0

    def getdata(self):
        self.title = input("Введите название книги: ")
        self.price = float(input("Введите цену книги: "))

    def putdata(self):
        print(f"Название: {self.title}")
        print(f"Цена: {self.price}")

class Book(Publication):
    def __init__(self):
        Publication.__init__(self)
        self.pages = 0

    def getdata(self):
        Publication.getdata(self)
        self.pages = int(input("Введите количество страниц: "))

    def putdata(self):
        Publication.putdata(self)
        print(f"Количество страниц: {self.pages}")

class Type(Publication):
    def __init__(self):
        Publication.__init__(self)
        self.time_in_minutes = 0

    def getdata(self):
        Publication.getdata(self)
        self.time_in_minutes = int(input("Введите продолжительность записи (в минутах): "))

    def putdata(self):
        Publication.putdata(self)
        print(f"Время записи (минуты): {self.time_in_minutes}")

print("Введите информацию для книги:")
book = Book()
book.getdata()
print("\nИнформация о книге:")
book.putdata()

print("\nВведите информацию для аудиокниги:")
audiobook = Type()
audiobook.getdata()
print("\nИнформация об аудиокниге:")
audiobook.putdata()
