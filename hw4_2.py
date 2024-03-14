# Python Core
# Модуль 4
# домашнє завдання 2
# Лопатін Євген

from pathlib import Path

with open('cats.txt', 'w') as fh:
    fh.write('60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n60b90c2e13067a15887e1ae3,Barsik,2\n60b90c3b13067a15887e1ae4,Simon,12\n60b90c4613067a15887e1ae5,Tessi,5') 
    

def get_cats_info(path):
    cats_info = []
    try:
        with open('cats.txt', 'r', encoding='utf-8') as file:
            for line in file: 
                cat_list = line.strip().split(',') # Розділяємо рядки по комі та відокремлюємо id, кличку та вік котів
                cat_dict = {'id': cat_list[0], 'name': cat_list[1], 'age': int(cat_list[2])}  # створюємо словник котів
                cats_info.append(cat_dict)  # вносимо в словник всі знайденні значення котів

    except FileNotFoundError: # виключаємо помилку шляху
        print("Файл не знайдено. Запровадьте коректний шлях до файлу.")
        return None
    except Exception as e: # виключаємо інші помилки
        print("Сталася помилка:", str(e))
        return None
      
    return cats_info

result = get_cats_info("cats.txt") # вводимо змінну результату по функції, яка бере шлях файлу
print(result) # виводимо словник на екран терміналу