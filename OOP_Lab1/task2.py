class Book:
    def __init__(self, author, title, book_type):
        self.author = author
        self.title = title
        self.book_type = book_type

    def display(self):
        print(self.author, self.title, self.book_type)
class Library:
    def __init__(self):

        self.books = []

    def add_book(self, book):

        self.books.append(book)

    def show_books(self):

        for book in self.books:
            book.display()

def main():
    library = Library()
    book1 = Book("Лев Толстой", "Война и мир", "художественная")
    book2 = Book("Дональд Кнут", "Искусство программирования", "техническая")
    book3 = Book("Мария Парр", "Вратарь и море", "художественная")
    book4 = Book("Эндрю Таненбаум", "Операционные системы", "техническая")
    book5 = Book("Мария Парр", "Вафельное сердце", "художественная")
    book6 = Book("Фёдор Достоевский", "Преступление и наказание", "художественная")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)
    library.add_book(book6)
    print("Автор     Название     Тип")
    library.show_books()

# Запуск программы
if __name__ == "__main__":
    main()
