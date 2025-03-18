x = float(input("Введите число: "))

first_decimal_digit = int(x * 10) % 10

print("Первая цифра после десятичной точки:", first_decimal_digit)