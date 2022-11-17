print('-----------------')
print('"Крестики-Нолики"')
print('-----------------')
print(' ')
print('Правила ввода координат:')
print('------------------------')
print('* 1-ая координата - строка.')
print('* 2-ая координата - столбец.')
print('* Между координатами ставится пробел.')
print(' ')
field = [[' ']*3 for i in range(3)]


def zone():
    print('  | 0 | 1 | 2 |')
    print('---------------')
    for i, row in enumerate(field):
        str_row = f"{i} | {' | '.join(map(str, row))} |"
        print(str_row)
        print('---------------')
    print()


def check_size():
    while True:
        dots = input('Ваш ход:').split()

        if len(dots) != 2:
            print('Введите ДВЕ координаты!')
            continue

        x, y = dots

        if not(x.isdigit()) or not(y.isdigit()):
            print('Введите числа!')
            continue

        x, y = int(x), int(y)

        if 2 < x or x < 0 or 2 < y or y < 0:
            print('Координаты вне диапазона')
            continue

        if field[x][y] != ' ':
            print('Клетка занята!')
            continue

        return x, y


def check_win():
    win_comb = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for comb in win_comb:
        symbols = []
        for s in comb:
            symbols.append(field[s[0]][s[1]])
        if symbols == ['X', 'X', 'X']:
            print('Выиграл Крестик!')
            return True
        if symbols == ['0', '0', '0']:
            print('Выиграл Нолик!')
            return True
    return False


go = 0
while True:
    go += 1
    zone()
    if go % 2 == 1:
        print('Ходит Крестик')
    else:
        print('Ходит Нолик')

    x, y = check_size()

    if go % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if check_win():
        break

    if go == 9:
        print('Ничья')
        break
