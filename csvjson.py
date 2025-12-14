import csv
import os

def task1_animals():
    with open('animals.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        print('Животные, обитающие в лесу:')
        for row in reader:
            if 'Лес' in row.get('Среда обитания'):
                print(f"{row.get('Животное')}")
def task2():
    try:
        with open('csv_file.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            print('Сотрудники старше 30 лет:')
            for row in reader:
                try:
                    age = int(row.get('Возраст'))
                    if age > 30:
                        print(f"{row.get('Имя')}")
                except (ValueError, TypeError):
                    continue
    except FileNotFoundError:
        print('Файл csv_file.csv не найден\n')
def create_files():
    animals_data = [
        ['Животное', 'Среда обитания'],
        ['Медведь', 'Лес'],
        ['Заяц', 'Лес'],
        ['Крокодил', 'Река'],
        ['Лиса', 'Лес'],
        ['Волк', 'Лес'],
        ['Пингвин', 'Антарктида'],
        ['Белка', 'Лес'],
    ]
    with open('animals.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(animals_data)
    print('Создан файл animals.csv.')
    employees_data = [
        ['Имя', 'Возраст', 'Город', 'Должность'],
        ['Иван', '35', 'Москва', 'Разработчик'],
        ['Мария', '28', 'Санкт-Петербург', 'Дизайнер'],
        ['Алексей', '42', 'Новосибирск', 'Менеджер'],
        ['Елена', '31', 'Казань', 'Аналитик'],
        ['Дмитрий', '25', 'Екатеринбург', 'Тестировщик'],
        ['Ольга', '38', 'Москва', 'Архитектор'],
        ['Сергей', 'не указан', 'Сочи', 'Консультант'],
        ['Анна', '45', 'Калининград', 'Директор']
    ]
    with open('csv_file.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(employees_data)
    print("Создан файл csv_file.csv")
create_files()
task1_animals()
task2()