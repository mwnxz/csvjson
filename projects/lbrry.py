import json
import os
from datetime import datetime
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self._name = name
    
    @abstractmethod
    def get_info(self):
        pass

class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
        self.__status = "доступна"
    
    @property
    def title(self):
        return self.__title
    
    @property
    def author(self):
        return self.__author
    
    @property
    def status(self):
        return self.__status
    
    def borrow(self):
        if self.__status == "доступна":
            self.__status = "выдана"
            return True
        return False
    
    def return_book(self):
        if self.__status == "выдана":
            self.__status = "доступна"
            return True
        return False
    
    def get_info(self):
        return f"{self.__title} - {self.__author} ({self.__status})"
    
class User(Person):
    def __init__(self, name):
        super().__init__(name)
        self.__borrowed_books = []
    
    @property
    def borrowed_books(self):
        return self.__borrowed_books
    
    def take_book(self, book):
        if book.borrow():
            self.__borrowed_books.append(book.title)
            return True
        return False
    
    def return_book(self, book):
        if book.title in self.__borrowed_books and book.return_book():
            self.__borrowed_books.remove(book.title)
            return True
        return False
    
    def get_info(self):
        return f"Пользователь: {self._name}"
    
    def print_my_books(self):
        if self.__borrowed_books:
            print("\nВаши книги:")
            for i, title in enumerate(self.__borrowed_books, 1):
                print(f"{i}. {title}")
        else:
            print("\nУ вас нет книг")

class Librarian(Person):
    def __init__(self, name):
        super().__init__(name)
    
    def get_info(self):
        return f"Библиотекарь: {self._name}"

class Library:
    def __init__(self):
        self.__books = []
        self.__users = []
        self.__librarians = []
        self.__load_data()
    
    def __load_data(self):

        try:
            with open('books.txt', 'r', encoding='utf-8') as file:
                books_data = json.load(file)
                for data in books_data:
                    book = Book(data['title'], data['author'])
                    if data['status'] == 'выдана':
                        book.borrow()
                    self.__books.append(book)
        except FileNotFoundError:
            print("Файл books.txt не найден. Создана новая библиотека.")
        
        try:
            with open('users.txt', 'r', encoding='utf-8') as file:
                users_data = json.load(file)
                for data in users_data:
                    user = User(data['name'])
                    user._User__borrowed_books = data['borrowed_books']
                    self.__users.append(user)
        except FileNotFoundError:
            print("Файл users.txt не найден.")
    
    def save_data(self):

        books_data = []
        for book in self.__books:
            books_data.append({
                'title': book.title,
                'author': book.author,
                'status': book.status
            })
        
        with open('books.txt', 'w', encoding='utf-8') as file:
            json.dump(books_data, file, ensure_ascii=False, indent=2)
        
        users_data = []
        for user in self.__users:
            users_data.append({
                'name': user._name,
                'borrowed_books': user.borrowed_books
            })
        
        with open('users.txt', 'w', encoding='utf-8') as file:
            json.dump(users_data, file, ensure_ascii=False, indent=2)
        
        print("Данные сохранены!")
    
    def add_book(self, title, author):
        for book in self.__books:
            if book.title == title and book.author == author:
                return "Книга уже существует"
        
        new_book = Book(title, author)
        self.__books.append(new_book)
        return "Книга успешно добавлена"
    
    def remove_book(self, title):
        for i, book in enumerate(self.__books):
            if book.title == title:
                if book.status == "выдана":
                    return "Книга выдана, нельзя удалить"
                del self.__books[i]
                return "Книга удалена"
        return "Книга не найдена"
    
    def register_user(self, name):
        for user in self.__users:
            if user._name == name:
                return "Пользователь уже существует"
        
        new_user = User(name)
        self.__users.append(new_user)
        return "Пользователь зарегистрирован"
    
    def show_all_users(self):
        if not self.__users:
            print("\nНет пользователей")
            return
        
        print("\nВсе пользователи:")
        for i, user in enumerate(self.__users, 1):
            print(f"{i}. {user._name}", end="")
            if user.borrowed_books:
                print(f" (взял книг: {len(user.borrowed_books)})")
            else:
                print()
    
    def show_all_books(self):
        if not self.__books:
            print("\nНет книг")
            return
        
        print("\nВсе книги:")
        for i, book in enumerate(self.__books, 1):
            print(f"{i}. {book.get_info()}")
    
    def get_available_books(self):
        available = []
        for book in self.__books:
            if book.status == "доступна":
                available.append(book)
        return available
    
    def find_book(self, title):
        for book in self.__books:
            if book.title == title:
                return book
        return None
    
    def find_user(self, name):
        for user in self.__users:
            if user._name == name:
                return user
        return None
    
    def find_librarian(self, name):
        for lib in self.__librarians:
            if lib._name == name:
                return lib
        return None
    
    def add_librarian(self, name):
        librarian = Librarian(name)
        self.__librarians.append(librarian)

def librarian_menu(library, librarian):
    print(f"\nДобро пожаловать, {librarian._name}!")
    
    while True:
        
        print("МЕНЮ БИБЛИОТЕКАРЯ")
        print("1. Добавить новую книгу")
        print("2. Удалить книгу")
        print("3. Зарегистрировать пользователя")
        print("4. Список всех пользователей")
        print("5. Список всех книг")
        print("6. Выйти")
        
        choice = input("Выберите действие: ").strip()
        
        if choice == "1":
            title = input("Название книги: ").strip()
            author = input("Автор: ").strip()
            result = library.add_book(title, author)
            print(f"\n{result}")
        
        elif choice == "2":
            title = input("Название книги для удаления: ").strip()
            result = library.remove_book(title)
            print(f"\n{result}")
        
        elif choice == "3":
            name = input("Имя нового пользователя: ").strip()
            result = library.register_user(name)
            print(f"\n{result}")
        
        elif choice == "4":
            library.show_all_users()
        
        elif choice == "5":
            library.show_all_books()
        
        elif choice == "6":
            print("Выход из меню библиотекаря...")
            break
        
        else:
            print("Неверный выбор!")

def user_menu(library, user):
    print(f"\nДобро пожаловать, {user._name}!")
    
    while True:
        
        print("МЕНЮ ПОЛЬЗОВАТЕЛЯ")
        print("1. Доступные книги")
        print("2. Взять книгу")
        print("3. Вернуть книгу")
        print("4. Мои книги")
        print("5. Выйти")
        
        choice = input("Выберите действие: ").strip()
        
        if choice == "1":
            books = library.get_available_books()
            if books:
                print("\nДоступные книги:")
                for i, book in enumerate(books, 1):
                    print(f"{i}. {book.get_info()}")
            else:
                print("\nНет доступных книг")
        
        elif choice == "2":
            books = library.get_available_books()
            if not books:
                print("\nНет доступных книг")
                continue
            
            print("\nДоступные книги:")
            for i, book in enumerate(books, 1):
                print(f"{i}. {book.title} - {book.author}")
            
            try:
                num = int(input("\nНомер книги: "))
                if 1 <= num <= len(books):
                    book = books[num-1]
                    if user.take_book(book):
                        print(f"\nВы взяли книгу: {book.title}")
                    else:
                        print("\nКнига уже выдана!")
                else:
                    print("Неверный номер!")
            except:
                print("Ошибка ввода!")
        
        elif choice == "3":
            if not user.borrowed_books:
                print("\nУ вас нет книг для возврата")
                continue
            
            user.print_my_books()
            try:
                num = int(input("\nНомер книги для возврата: "))
                if 1 <= num <= len(user.borrowed_books):
                    title = user.borrowed_books[num-1]
                    book = library.find_book(title)
                    if book and user.return_book(book):
                        print(f"\nВы вернули книгу: {title}")
                    else:
                        print("\nОшибка возврата!")
                else:
                    print("Неверный номер!")
            except:
                print("Ошибка ввода!")
        
        elif choice == "4":
            user.print_my_books()
        
        elif choice == "5":
            print("Выход из меню пользователя...")
            break
        
        else:
            print("Неверный выбор!")

def main():
    print("БИБЛИОТЕЧНАЯ СИСТЕМА")
    now = datetime.now()
    print(f"Дата: {now.strftime('%d/%m/%Y')}")
    print(f"Время: {now.strftime('%H:%M')}")
    
    library = Library()
    if not library.find_librarian("библиотекарь"):
        library.add_librarian("библиотекарь")
    
    while True:
        print("ВХОД В СИСТЕМУ")
        print("1. Библиотекарь")
        print("2. Пользователь")
        print("3. Выход")
        
        role = input("Выберите роль (1-3): ").strip()
        
        if role == "1":
            name = input("Ваше имя: ").strip()
            librarian = library.find_librarian(name)
            if librarian:
                librarian_menu(library, librarian)
                library.save_data()
            else:
                print("Библиотекарь не найден! Доступен только 'библиотекарь'")
        
        elif role == "2":
            name = input("Ваше имя: ").strip()
            user = library.find_user(name)
            
            if user:
                user_menu(library, user)
                library.save_data()
            else:
                print("Пользователь не найден!")
                reg = input("Хотите зарегистрироваться? (да/нет): ").lower()
                if reg == 'да':
                    result = library.register_user(name)
                    print(result)
                    if "успешно" in result.lower():
                        user = library.find_user(name)
                        user_menu(library, user)
                        library.save_data()
        
        elif role == "3":
            print("\nСохранение данных...")
            library.save_data()
            print("До свидания!")
            break
        
        else:
            print("Неверный выбор!")
if __name__ == "__main__":
    main()