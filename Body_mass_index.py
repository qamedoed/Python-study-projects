height = float(input('Какой у Вас рост?'))
weight = float(input('Какой у Вас вес?'))
bmi = weight / height ** 2
print('Ваш индекс массы тела:', bmi)

if bmi < 18.5:
    print('У Вас недостаточная масса тела')
elif bmi < 25:
    print('Ваша масса тела в норме')
elif bmi < 30:
    print('У Вас избыточная масса тела')
else:
    print('У Вас ожирение!')