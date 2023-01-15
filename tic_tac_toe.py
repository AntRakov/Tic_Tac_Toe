'''
    Крестики нолики v1.0
    Создано: Jan 15 2023.
    GitHub: https://github.com/AntRakov/Tic_Tac_Toe.git

'''

# массив игрового поля
playing_field = list(range(1, 10))

# массив выигрышных комбинаций
victory_fields = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 6), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


# функция показа игрового поля
def show_field():
    print('\n' + '+---' * 3 + '+')
    for i in range(3):
        print('| ' + str(playing_field[0 + i * 3]) + ' | ' + str(playing_field[1 + i * 3]) + ' | ' + str(
            playing_field[2 + i * 3]), end=' ')
        print('|\n' + '+---' * 3 + '+')


# функция ввода пользователем значения в игровое поле
def user_input(playersXO):
    while True:
        game_map_number = input(f'Player {playersXO} enter the number of the playing field ')
        if not (game_map_number in '123456789'):  # проверка диапазона ячеек
            print('You have entered the wrong value of the playing field. Please try again')
            continue
        game_map_number = int(game_map_number)
        if str(playing_field[game_map_number - 1]) in 'XO':  # проверка занятых ячеек
            print('This field is already taken. Choose a free cell ')
            continue
        playing_field[game_map_number - 1] = playersXO
        break


# функция проверки выигрышных комбинаций
def victory_check():
    for i in victory_fields:
        if playing_field[i[0] - 1] == playing_field[i[1] - 1] == playing_field[i[2] - 1]:
            return playing_field[i[0] - 1]
    else:
        return False


# основная функция программы
def main():
    counter = 0
    while True:
        show_field()
        if counter % 2 == 0:
            user_input('X')
        else:
            user_input('O')
        if counter > 4:  # проверяем победителя
            winner = victory_check()
            if winner:
                show_field()
                print(f'Congratulations {winner} is winner!!!')
                break
        counter += 1
        if counter > 8:
            show_field()
            print('Draw')
            break


main()
