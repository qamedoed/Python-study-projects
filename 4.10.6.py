n = int(input("Введите количество чисел: "))
max_sum = 0
max_num = 0
for _ in range(n):
    num = int(input("Введите число: "))
    digit_sum = 0
    temp = num
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    if digit_sum > max_sum:
        max_sum = digit_sum
        max_num = num
print(f"Число {max_num} имеет максимальную сумму цифр: {max_sum}")