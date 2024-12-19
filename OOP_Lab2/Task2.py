class Publication:
    title: str
    price: float
    def getdata(self):
        self.title = input("название книги: ")
        self.price = float(input("цена книги: "))
    def putdata(self):
        print(f"название: {self.title}")
        print(f"цена: {self.price}")
class Sales:
    def __init__(self):
        self.sales = [0.0, 0.0, 0.0]
    def getdata(self):
        print("продажи за последние три месяца:")
        for i in range(3):
            self.sales[i] = int(input(f"продажи за месяц {i+1}: "))
    def putdata(self):
        print("продажи за последние три месяца:")
        for i in range(3):
            print(f"месяц {i+1}: {self.sales[i]}")
class Book(Publication, Sales):
    def __init__(self):
        Sales.__init__(self)
        self.pages = 0
    def getdata(self):
        Publication.getdata(self)
        self.pages = int(input("введите количество страниц: "))
        Sales.getdata(self)
    def putdata(self):
        Publication.putdata(self)
        print(f"количество страниц: {self.pages}")
        Sales.putdata(self)
class Type(Publication, Sales):
    def __init__(self):
        Sales.__init__(self)
        self.time = 0
    def getdata(self):
        Publication.getdata(self)
        self.time = int(input("продолжительность записи (минуты): "))
        Sales.getdata(self)
    def putdata(self):
        Publication.putdata(self)
        print(f"время записи (минуты): {self.time}")
        Sales.putdata(self)
print("введите информацию для книги:")
book = Book()
book.getdata()
print("\nинформация о книге:")
book.putdata()
print("\nвведите информацию для аудиокниги:")
audiobook = Type()
audiobook.getdata()
print("\nинформация об аудиокниге:")
audiobook.putdata()