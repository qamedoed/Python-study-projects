import math

V_earth = 1.08321 * 10 ** 12  

R = float(input("Введите радиус теоретически возможной планеты: "))

V_planet = (4 / 3) * math.pi * R ** 3

ratio = round(V_earth / V_planet, 3)

if ratio > 1:
    print(f"Объём планеты Земля больше в {ratio} раз")
else:
    print(f"Объём планеты Земля меньше в {round(1 / ratio, 3)} раз")