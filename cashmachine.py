while True:
    for attempt in range(1, 4):
        pincode = int(input('Введите пин-код:'))
        if pincode == 1234:
            print('\nПин-код верный. Держите ваши деньжули!')
            break
        print('Неверный пин-код. Осталось попыток:', 3 - attempt)
    else:
        print('\nВаша карта заблокирована. Уходи, проходимец.')
    print('Следующий клиет, здравствуйте!')
