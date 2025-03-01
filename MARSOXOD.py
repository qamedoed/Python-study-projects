max_x = 15
max_y = 20

x = 8
y = 10

while True:
    print(f"Марсоход находится на позиции {x}, {y}, введите команду:")
    command = input().strip().upper()

    if command == 'W':
        if y < max_y:
            y += 1
        else:
            print("Марсоход уперся в северную стену!")
    elif command == 'S':
        if y > 1:
            y -= 1
        else:
            print("Марсоход уперся в южную стену!")
    elif command == 'A':
        if x > 1:
            x -= 1
        else:
            print("Марсоход уперся в западную стену!")
    elif command == 'D':
        if x < max_x:
            x += 1
        else:
            print("Марсоход уперся в восточную стену!")
    else:
        print("Неизвестная команда! Используйте только W, A, S, D.")