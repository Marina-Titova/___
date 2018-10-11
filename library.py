"""
Titova Marina
email: marina_titova19@mail.ru
phone: 89137594419
"""


class Book:

    id_ = 0
    class_instance = []

    def __init__(self, name, author, publisher, year, pages, illustration, price, copy):
        Book.id_ += 1
        self.id_ = Book.id_
        self.name = name
        self.author = author
        self.publisher = publisher
        self.year = year
        self.pages = pages
        self.illustration = illustration
        self.price = price
        self.copy = copy
        self.h_m_t = 0
        self.class_instance.append(self)

    def __str__(self):
        book = '\nНазвание книги: ' + self.name + '\nАвторы: ' + self.author + \
               '\nИздательство: ' + self.publisher + '\nГод издания: ' + str(self.year) + \
               '\nКоличество страниц: ' + str(self.pages) + '\nКоличество иллюстраций: ' + str(self.illustration) +\
               '\nСтоимость: ' + str(self.price) + '\nКоличество экземпляров книги: ' + str(self.copy) + \
               '\nКоличество студентов, которым выдавалась книга: ' + str(self.h_m_t)
        return book

    def __repr__(self):
        return self.__str__()

    @classmethod
    def popular_author(cls, year):
        author_dict = dict()
        for book in cls.class_instance:
            if book.author in author_dict.keys():
                author_dict[book.author] += book.h_m_t
            else:
                author_dict[book.author] = book.h_m_t
        major = max(list(author_dict.values()))
        for author in author_dict.keys():
            if author_dict[author] == major:
                return 'Самый популярный автор в ' + str(year) + ' году - ' \
                       + author + ' Кол-во выданых книг: ' + str(major)
                

class Student:

    class_instance = []

    def __init__(self, name, book_id, dates):
        self.name = name
        self.book_id = int(book_id)
        self.dates = dates.split(';')
        self.class_instance.append(self)
        
    @classmethod
    def books_issued_for_year(cls, year):
        for stud in cls.class_instance:
            for book in Book.class_instance:
                if int(stud.dates[0][-4:]) == year and book.id_ == stud.book_id:
                    book.h_m_t += 1
        return Book.popular_author(year)

    @classmethod
    def bookworm(cls):
        stud_dict = dict()
        for stud in cls.class_instance:
            if stud.name in stud_dict.keys():
                stud_dict[stud.name] += 1
            else:
                stud_dict[stud.name] = 1
        major = max(list(stud_dict.values()))
        for name in stud_dict.keys():
            if stud_dict[name] == major:
                return 'Самый злостный читатель - ' + name + '. Кол-во выданых книг: ' + str(major)


def main():
    with open('books.txt') as f:
        for line in f.readlines():
            Book(*line.split(','))
    with open('students.txt') as f:
        for line in f.readlines():
            Student(*line.split(','))
        
    while True:
        command = int(input('1. Узнать самого популярного автора за год\n'
                            '2. Узнать самого злостного читателя\n3. Выход\n'))
        if command == 1:
            year = int(input('Введите год (предлагается ввести "2018", так как в базе есть данные только за 2018 год): '))
            print(Student.books_issued_for_year(year))
        if command == 2:
            print(Student.bookworm())
        if command == 3:
            break


if __name__ == '__main__':
    main()
