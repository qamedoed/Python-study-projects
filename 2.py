width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))
print(" " + "-" * (width - 2))
for _ in range(height - 2):
    print("|" + " " * (width - 2) + "|")
print(" " + "-" * (width - 2))

width = int(input("Введите ширину рамки: "))
height = width // 2
print(" " + "-" * (width - 2))
for _ in range(height - 2):
    print("|" + " " * (width - 2) + "|")
print(" " + "-" * (width - 2))