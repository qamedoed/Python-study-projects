size = int(input('Введите размер сетки:'))
for row in range(size):
    for col in range(size):
        if row<col:
            print(0, end = ' ')
        elif row>col:
            print(2, end = ' ')
        else:
            print(1, end = ' ')
    print()
    
for row in range(20):
    for col in range(50):
        if row == 9:
            print('-', end = '')
        elif col == row + 29:
            print('\\', end = '')
        elif col == -row + 19:
            print('/', end = '')
        elif col == 24:
            print('|', end = '')
        else:
            print(' ', end='')
    print()
     