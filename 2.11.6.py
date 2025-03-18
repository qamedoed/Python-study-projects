import math

n = int(input("Введите кол-во чисел: "))

for _ in range(n):
    num = float(input("Введите число: "))
    
    if num > 0:
        x = math.ceil(num)  
        result = math.log(x)  
        print(f"x = {x} log(x) = {result}")
    else:
        x = math.floor(num)  
        result = math.exp(x)  
        print(f"x = {x} exp(x) = {result}")