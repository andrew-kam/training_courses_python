import random


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# Функция для отображения игрового поля
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Функция для ввода хода игрока
def player_turn():
    position = input("Введите номер позиции, куда хотите походить (от 1 до 9): ")
    position = int(position) - 1
    board[position] = "X"


# Функция для хода компьютера
def computer_turn():
    position = random.randint(0, 8)
    while board[position] != "-":
        position = random.randint(0, 8)
    board[position] = "O"


# Функция для проверки победной ситуации
def check_win():
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"
    if row1 or row2 or row3 or col1 or col2 or col3 or diag1 or diag2:
        return True
    else:
        return False


# Функция для проверки ничьи
def check_tie():
    for item in board:
        if item == "-":
            return False
    return True


# Основная программа
def main():
    display_board()
    while True:
        player_turn()
        display_board()
        if check_win():
            print("Ты победил!")
            break
        if check_tie():
            print("Ничья!")
            break
        computer_turn()
        display_board()
        if check_win():
            print("Компьютер победил!")
            break
        if check_tie():
            print("Ничья!")
            break


main()
