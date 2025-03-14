count = int(input("Введите количество чисел: "))
prime_count = 0
for _ in range(count):
    num = int(input("Введите число: "))
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_count += 1
print("Количество простых чисел в последовательности:", prime_count)