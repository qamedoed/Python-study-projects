file_size = int(input("Укажите размер файла для скачивания: "))
speed = int(input("Какова скорость вашего соединения: "))

downloaded = 0
seconds = 0

while downloaded < file_size:
    seconds += 1
    downloaded += speed
    
    if downloaded > file_size:
        downloaded = file_size
    
    percent = int((downloaded / file_size) * 100)
    
    print(f"Прошло {seconds} сек. Скачано {downloaded} из {file_size} Мб ({percent}%)")

print(f"Скачивание завершено за {seconds} сек.")