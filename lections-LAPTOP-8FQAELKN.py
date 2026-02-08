from datetime import datetime
#from functools import reduce
#from functools import reduce
#numbers=[1, 2, 3, 4, 5]

#def ab(x):
#  return x*2

#result=map(ab, numbers)
#print(list(result))

#add=map(lambda x: x*2, numbers)
#print(list(add))

#def ch(x):
 #   return x%2 == 0

#result=filter(ch, numbers)
#print(list(result))

#filt=filter(ch,numbers)
#print(list(result))

#def add(x, y):
    #return x+y
#print(result)

#list1 = [1, 2, 3, 4, 5]
#list = ['a', 'b', 'c', 'd', 'e']
#result = zip(list1, list)
#print(list(result))

#lambda аргкменты:выражение
#add = lambda x,y:x+y
#print(add(5,6))

#people=[('мария', 34), ('анастасия', 23), ('артем', 7)]

#sorted_people=sorted(people, key=lambda people: people[1])
#print(list(sorted_people))


#sorted_people1=sorted(people, key=lambda people: people[0])
#list.reverse(sorted_people)
#print(list(sorted_people1))
#students = [
 #   {"name": "Alice", "grades": [85, 92, 78]},
  #  {"name": "Bob", "grades": [65, 70, 80]},
   # {"name": "Charlie", "grades": [95, 88, 92]}
#]
#def calculate_average(grades):
 #   return sum(grades) / len(grades)

#students = [
 #   {"name": "Alice", "grades": [85, 92, 78]},
  #  {"name": "Bob", "grades": [65, 70, 80]},
   # {"name": "Charlie", "grades": [95, 88, 92]}
#]


#top_students = list(filter(lambda s: calculate_average(s["grades"]) > 80, students))

#for student in top_students:
 #   avg = calculate_average(student["grades"])
  #  print(f"{student['name']}: {avg:.2f}")


############################################



#file=open('example.txt', 'w')
#file.write('привет мир')
#file.close()

#with open('test.txt', 'w', encoding= 'utf-8')as file:
#    file.write('Привет мир\n')
    


#with open('test.txt', 'a', encoding= 'utf-8')as file:
#    file.write('Привет Андрей\n')

#with open('test.txt', 'r', encoding= 'utf-8')as file:
#    content=file.read()
#    print(content)

#with open('test.txt', 'r', encoding= 'utf-8')as file:
#    line1=file.read()
#    line2=file.read()
#   print(f'Первая строка {line1.strip()}')
#    print(f'Вторая строка {line2.strip()}')
#with open('test.txt', 'r', encoding= 'utf-8')as file:
#    data=file.readlines()
#    for i, line in enumerate(data,1):
#        print(f'Строка{i}:{line.strip()}')




#with open('test.txt', 'r', encoding= 'utf-8')as file:
#    data=list(file)
#    print(data)


#with open('test.txt', 'r+', encoding= 'utf-8')as file:
#    file.write('Как дела?\n')
#    line=['маша', 'коля', 'миша']
#    file.writelines(line)
#try:
#    with open('ex.txt','r') as f:
#       content=f.read()
#       print(content)
#except FileNotFoundError:
#   print('Файл не найден')
#except PermissionError:
#    print('Нет права доступа к файлу')
#finally:
#    print('Работа с файлами завершена')






#with open ('test.txt', 'r+', encoding= 'cp1251') as file:
#    file.write('1234567890asdfg')
#    file.seek(5)
#    data=file.read(1)
#    print(data)


# with open ('test.txt', 'r+b') as file:
#    file.write(b'1234567890asdfg')
#    file.seek(-4,2)
#    data=file.read(1)
#    print(data)

# with open ('test.txt', 'r+b') as file:
#    data=file.read(5)
#    print(data)



#from datetime import datetime

#def nast():
#    mood=input("Какое у тебя сегодня настроение?")
#    date_time=datetime.now()
#    date_str=date_time.strftime("%d/%m/%Y, %H:%M:%S")

#    with open('file.txt','a',encoding='utf-8') as file_n:
#        m=f'[{date_str}] Настроение: {mood}\n'
#        file_n.write(m)
#    print('Настроение сегодня')

#nast()
                                


# import random




# def phrase():
#     try:
#         with open('quotes.txt', 'r', encoding='utf-8') as file:
#             quotes = file.readlines()
        
#         if quotes:
#             r_quote = random.choice(quotes).strip()
#             print(f"Случайная цитата: {r_quote}")
#         else:
#             print("Файл с цитатами пуст")
            
#     except FileNotFoundError:
#         with open('quotes.txt', 'w', encoding='utf-8') as file:
#             sample_quotes = [
#         'Возможности не приходят сами — вы создаёте их',
#         'Неудача — это возможность начать заново, но уже более мудро',
#         'Всегда смотрите на солнце — и тени будут позади вас',
#         'Обстоятельства часто можно изменить, изменив своё отношение к ним',
#         'Лучше поздно, чем никогда'
#     
# phrase()
####### 1 
# def date():
#     day = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
#     today = datetime.today().weekday()
#     return day[today]
# print(date())

# ####### 2 
# import datetime

# def today_date():
#     date_time = datetime.datetime.today()
#     date_str = date_time.strftime("%d/%m/%Y")
#     week = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
#     week_name = week[date_time.weekday()]
#     print(f'Дата - {date_str}')
#     print(f'День недели - {week_name}')
#     return week_name
# today_date()

# ###### 3 
# def second_to_day(seconds):
#     sd=24*60*60
#     days=seconds/sd
#     return days
# print(second_to_day(1296000))


# ##### 4
# def a(l, text):
#     strc=text[:l]
#     return strc
# print(a(5, 'Строка'))

# ###### 5 
# def zodiac(month, day):
#     if d>21

import os
import shutil
# print(os.getcwd())
# print(os.listdir())
# print(os.listdir('way to folder'))

#os.mkdir('C:\Users\Айзирек\OneDrive\Рабочий стол\второй курс\python>') #создание новой директории

# print(os.listdir('C:\Users\Айзирек\OneDrive\Рабочий стол\второй курс\python>'))



# dir-'C:/Users/Айзирек/OneDrive/Рабочий стол/второй курс/python'
# old=os.path.join(dir, 'python')
# new=os.path.join(dir, 'NewExample')
# os.rename(old, new)
# print(os.listdir(dir))

# print(os.rmdir('C:/Users/Айзирек/OneDrive/Рабочий стол/второй курс/NewExample'))






# 08.12.2025 цсв
# import csv
# test_csv=[
#     ['Имя', 'Возраст', 'Город'],
#     ['Анна', '34', 'Москва'],
#     ['Петр', '34', 'Москва']
  
# ]
# with open ('test_data_csv', 'w', encoding='utf-8', newline='') as file:#удаляет лишние пробелы
#     writer=csv.writer(file)
#     writer.writerows(test_csv)
     
# with open ('test_data_csv', 'r', encoding='utf-8') as file:#удаляет лишние пробелы
#     reader=csv.reader(file)
#     for row_num, row in enumerate(reader, 1):
#         print(f'Строка {row_num}: {row}')
#         print(f'Строка {type(row)}') #ПОСТРОЧНОЕ ЧТЕНИЕ СЛОВАРЯ
     
# with open ('test_data_csv', 'r', encoding='utf-8') as file:#удаляет лишние пробелы
#     reader=csv.DictReader(file)
#     for i in reader:
#         print(f'{i['Имя']}, Возраст: {i['Возраст']}, Город: {i['Город']}')
     
# import json
# test_json={
#     'Имя': 'Анна', 
#     'Возраст': 30,
#     'Москва': 'Москва',
# }
# with open ('test_data_json', 'w', encoding='utf-8') as file:
#     json.dump(test_json, file, ensure_ascii=False, indent=2)     #кодировка, записывающая в корректом виде,в ином случае представляет в кодировке ютф16 пробелы две штуки
# #чтение файла

# with open ('test_data_json', 'r', encoding='utf-8') as jsonfile:
#     data=json.load(jsonfile)
#     print(f'Данные: {data}')
#     print(f'Тип: {data}')
#     print(f'Имя: {data}')
#     print(f'Возраст: {data}')
#     print(f'Город: {data}')





#12.01.2026 ОБЪЕКТНО-ОРИЕНТИРОВАННОЕ ПРОГРАММИРОВАНИЕ

# class Book: #с заглавной буквы
#     def __init__(self, ): #конструктор автоматически вызывается при создании нового объекта класса
#         pass

# class Book: #с заглавной буквы
#     def __init__(self, name): 
#         self.name=name


# class Book: #с заглавной буквы
#     def __init__(self, name, author): #ссылка на текущий экземпляр класса, в других яхыках - this
#         self.name=name
#         self.author=author

# class Book:
#     raiting=5 #Добавление атрибута

#     def __init__(self, name, author, raiting): #ссылка на текущий экземпляр класса, в других яхыках - this
#         self.name=name
#         self.author=author
#         self.is_reading=False
#         self.raiting=raiting
# book=Book('Иван', "Иванов Иван")
# print(book.is_reading)

# #Изменение атрибута
# book.is_reading=True
# book.name='Николай'
# print(book.name, book.is_reading)

# #self помогает обращаться к объектам класса


# class Book:
#     def __init__(self, name, author, year): #ссылка на текущий экземпляр класса, в других яхыках - this
#         self.name=name
#         self.author=author
#         self.year=year
#     def book_info(self):
#         print(f'Название - {self.name}, Автор - {self.author}, Год - {self.year}')
# book1=Book('Война и мир', 'Л. Н. Толстой', 1990)
# book2=Book('Преступление и наказание', 'Ф. М. Достоевский', 1991)
# book3=Book('Отцы и дети', 'Тургенев', 1901)

# print(book1.book_info())
# print(book2.book_info())
# print(book3.book_info())

# class Student:
#     def __init__(self, name, surname, age):
#         self.name=name
#         self.surname=surname
#         self.age=age
#     def student_info(self):
#         print(f'Привет, я ={self.name} {self.surname}, мне {self.age} лет')
# student1=Student('Иванов', 'Иван', 15)
# student2=Student('Петров', 'Петр', 17)
    
# student1.student_info()
# student2.student_info()

# (26.01.2026)

# class BankAccount:
#     def __init__(self, acc_number, acc_owner, balance):
#         self.__acc_number=acc_number #__приватность
#         self.__balance=balance
#         self.__acc_owner=acc_owner
#     def get_acc_number(self):
#         return self.get_acc_number
#     def get_acc_owner(self):
#         return self.get_acc_owner
#     def get_balance(self):
#         return self.get_balance

#     def deposit(self, amount):
#         if amount>0:
#             self.__balance+=amount
#             return True
        
#     def withdraw(self, amount):
#         if 0< amount <=self.__balance:
#             self.__balance-=amount
#             return True
#         return False
#     def info(self):
#         print(self.__acc_number)
#         print(self.__acc_owner)
#         print(self.__balance)
# bank1=BankAccount(12345677, "Игорь Синяк", 1000)
# bank1.deposit(500)
# bank1.withdraw(300)
# bank1.info()





# class Student:
#     def __init__(self, name):
#         self.__name=name
#         self.__grades=[]
#     def get_name(self):
#         return self.__name
#     def get_grades(self):
#         return self.__grades
#     def add_grade(self, grade):
#         if isinstance(grade, (int, float)) and 1 <=grade<=5:
#             self.__grades.append(grade)
#             return True
#         return False
#     def get_average(self):
#         if not self.__grades:
#             return 0
#         return sum(self.__grades)/len(self.__grades)
#     def info(self):
#         print(self.__grades)
#         print(self.__name)
#         print(self.get_average())
# student1=Student("Чередниченко Юрий")
# student2=Student("Власова Милана")
# student1.add_grade(5)
# student1.add_grade(5)
# student2.add_grade(5)
# student2.add_grade(5)           

# student1.info()
# student2.info()

# # Создайте класс Car, который представляет автомобиль с полной защитой данных через механизмы инкапсуляции.

# Требования к классу:

# 1. Приватные атрибуты:
#    - _model (строка) - модель автомобиля
#    - _year (целое число) - год выпуска
#    - _mileage (целое число) - пробег в километрах
#    - _fuel_level (вещественное число) - уровень топлива в литрах

# 2. Публичные методы:
#    - drive(km) - проехать заданное расстояние в км
#      * Проверяет, достаточно ли топлива для поездки
#      * Расход топлива: 10 литров на 100 км (0.1 л/км)
#      * Если топлива достаточно, увеличивает пробег и уменьшает уровень топлива
#      * Возвращает строку с результатом операции

#    - refuel(liters) - заправить автомобиль
#      * Проверяет, что количество литров положительное
#      * Увеличивает уровень топлива
#      * Возвращает строку с результатом операции

#    - get_info() - получить информацию об автомобиле
#      * Возвращает форматированную строку с моделью, годом, пробегом и уровнем топлива
#     #

# class Car:
#     def __init__(self, year, model, milage, fuel_level):
#         self.__model=model 
#         self.__year=year
#         self.__mileage=milage
#         self.__fuel_level=fuel_level

#     def gett_model(self):
#         return self.__model
    
#     def gett_yaer(self):
#         return self.__year
    
#     def gett_milage(self):
#         return self.__mileage
    
#     def gett_fuel_level(self):
#         return self.__fuel_level
    
#     def drive(self, km):
#         if km>0 and self.__fuel_level>=km*0.1:
#             self.__mileage+=km
#             self.__fuel_level-=km-0.1
#             return km
#     def refuel(self, litr):
#         if litr>-0:
#             self.__fuel_level+=litr
#         return litr
#     def info(self):
#         return self.__model, self.__fuel_level, self.__mileage
# car=Car("dsfsdfdaf", 2005)
# car



#02.02.2026
# from abc import ABC, abstractmethod
# class Product:
#     def __init__(self, name, price):
#         self.name=name
#         self.price=price
#     @abstractmethod
#     def discount_price(self):
#         pass
# class Promo(Product):
#     def discount_price(self):
#         return self.price*0.8
# class Promox2(Product):
#     def discount_price(self):
#         return self.price*0.4
    
# phone=[Promo('Айфон 15', 1000000), Promox2('Айфон 17', 150000)] 
# for ph in phone:
#     print(ph.discount_price())       

class Duck:
    def __init__(self, name):
        self.name=name
    def make_sound(self):
        return "Кря-кря"
    def swim(self):
        return "Утка плавает"
    
class Dog:
    def __init__(self, name):
        self.name=name
    def make_sound(self):
        return "Гав гав"
    def run(self):
        return "Собака бегает"
    
class Fish:
    def __init__(self, name):
        self.name=name
    def swim(self):
        return "Рыба плавает"
    
class Robot:
    def __init__(self, name):
        self.name=name
    def make_sound(self):
        return "Бип бип"
    def swim(self):
        return "Робот гуляет"

def make_sound_animal(animal):
    if hasattr(animal, "make_sound"): #Есть ли сторковая функция
        return animal.make_sound()
    else:
        return f"Животное не издает звуков"

animals=[Duck("Дональд дак"), Dog("Николай"), Fish("Максим"), Robot("Марина")]

def swim_animal(animal):
    if hasattr (animal, "swim"):
        return animal.swim()
    else:
        return f"Животное не плавает"

for animal in animals:
    print(make_sound_animal(animal))

for an in animals:
    print(swim_animal(animal))

# from abc import abstractmethod
# class Pay:
#     def __init__(self, summa, sp_pay):
#         self.summa=summa
#         self.sp_pay=sp_pay
#     @abstractmethod
#     def price_pay(self):
#         pass

# class Nal_pas(Pay):
#     def price_pay(self):
#         return self.summa-(self.summa*0.01)
    
# class Pr_pas(Pay):
#     def price_pay(self):
#         return self.summa-(self.summa*0.03)
    
# sp=[Nal_pas(4000, "Наличные"), Pr_pas(4000, "Перевод") ]

# for i in sp:
#     print(i.price_pay())
