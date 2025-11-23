import random

import os


try:
    os.mkdir('C:/Users/Айзирек/OneDrive/Рабочий стол/второй курс/python/game_stats') 
    print('Папка для сохранения статистики успешно создана!')
except:
    print('Папка для сохранения статистики уже есть!')
def all_same(lst):
    if not lst:
        return False    
    first = lst[0]
    for item in lst:
        if item != first:
            return False
    return True    
def create_board(size):
    board = []
    for i in range(size):
        strr = []
        for a in range(size):
            strr.append(' ')
        board.append(strr)
    return board
def show_board(board):
    size = len(board)
    print('\n  '+' '.join(str(i) for i in range(size)))
    for i in range(size):
        print(f'{i} '+' '.join(board[i]))
    print()
def check_win(board):
    size= len(board)
    for strr in board:
        if strr[0] != ' ' and all_same(strr):
            return strr[0]
    for column in range(size):
        c = []
        for strr in range(size):
            c.append(board[strr][column])
        if c[0] != ' ' and all_same(c):
            return c[0]
    diagonal1= []
    diagonal2= []
    for i in range(size):
        diagonal1.append(board[i][i])
        diagonal2.append(board[i][size-1-i])
    if diagonal1[0] != ' ' and all_same(diagonal1):
        return diagonal1[0]
    if diagonal2[0] != ' ' and all_same(diagonal2):
        return diagonal2[0]
    return None
def full_board(board):
        for strr in board:
            for cell in strr:
                if cell == ' ':
                    return False
        return True
def player_step(board, player):
        size= len(board)
        while True:
            try:
                print(f' Ход игрока {player}')
                strr= int(input('Введите номер строки - '))
                column = int(input('Введите номер столбца - '))
                if strr < 0 or strr >= size or column < 0 or column >= size:
                    print(f'Число должно быть больше 0, но меньше {size-1}')
                elif board[strr][column] != ' ':
                    print('Эта клетка уже заполнена!')
                else:
                    return strr, column
            except ValueError:
                print('Ошибка введите числа!')
def random_step(board):
        size = len(board)
        free_cells = []
        for i in range(size):
            for j in range(size):
                if board[i][j] == ' ':
                    free_cells.append((i, j))
        return random.choice(free_cells)
def save_stats(winner, size, mode):
    try:
        stat = 'C:/Users/Айзирек/OneDrive/Рабочий стол/второй курс/python/game_stats/stats.txt'
        with open(stat, 'a', encoding = 'utf-8') as file:
            if winner == 'Ничья':
                file.write(f'Ничья, поле - {size}x{size}')
            else:
                file.write(f'Победитель {winner} поле {size}x{size}, режим - {mode}')
        print('Ствтистика сохранена!')
    except:
        print('Ошибка при сохранении статистики.')
def game():
    print('КРЕСТИКИ-НОЛИКИ')
    while True:
        try:
            size = int(input('Размер поля (например 3) - '))
            if size >= 3:
                break
            else:
                print('Минимальный размер 3')
        except ValueError:
            print('Ошибка, надо ввести число!')
    print('\n1 - игра с другом')
    print('2 - игра с роботом')
    while True:
        try:
            choice= int(input('Ваш выбор - '))
            if choice == 1 or choice == 2:
                break
            else:
                print('Такого режима нет')
        except:
            print('Ошибка, введите число')
    if choice == 1:
        mode = 'С другом'
    else:
        mode = 'С ботом'
    if random.randint(0,1) == 0:
        cur_player = 'X'
    else:
        cur_player = 'O'
    print(f'\nПервым ходит - {cur_player}')
    board= create_board(size)
    while True:
        print(f'\nРежим - {mode}')
        show_board(board)

        if mode == 'С другом' or cur_player == 'X':
            strr, column= player_step(board, cur_player)
        else:
            print('Бот думает')
            strr, column= random_step(board)
        board[strr][column]= cur_player
        winner= check_win(board)
        if winner:
            show_board(board)
            print(f'{winner} Победил!')
            save_stats(winner, size, mode)
            break
        if full_board(board):
            show_board(board)
            print('Ничья!')
            save_stats('Ничья!', size, mode)
            break
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player= 'X'
def menu():
    while True:
        print('\n МЕНЮ')
        print('1 - Новая игра.')
        print('2 - Выход')
        try:
            choice = int(input('Ваш выбор - '))
            if choice == 1:
                game()
                while True:
                    print('\n1 - Играть снова.')
                    print('2 - Назад в меню.')
                
                    try:
                        again = int(input('Ваш выбор - '))
                        if again == 1:
                            game()
                        elif again == 2:
                            break
                        else:
                            print('Выберите 1 или 2.')
                    except ValueError:
                        print('Ошибка, введите число')
            elif choice == 2:
                print('До свидания!')
                break
            else:
                print('Введите 1 или 2.')
        except:
            print('Ошбика, введите число!')
menu()