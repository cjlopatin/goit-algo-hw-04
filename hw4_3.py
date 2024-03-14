# Python Core
# Модуль 4
# домашнє завдання 3 (необовязкове)
# Лопатін Євген

# імпоортуємо модулі
import os
import sys
from pathlib import Path
from colorama import Fore, Style

def visual_structure(directory): # створюємо основну функцію візуалізації
    try:
        directory_path = Path(directory) # створюємо змінну для перевірки та дій зі шляхом
        if directory_path.exists() and directory_path.is_dir(): # перевіряємо на тип та нявність папки
            print(Fore.BLUE + f"Ваша основна папка для візуалізації: \n 📁 {directory}") # створюємо батьківський меседж з зображенням батьківської папки
            visual_inside(directory_path) # викликаємо наступну функцію візуалізації вмісту папки
        else:
            print(Fore.RED + "Помилка: такої папки не існує.") # виводимо помилку
    except Exception as e:
        print(Fore.RED + f"Помилка: {str(e)}" + Style.RESET_ALL) # інші помилки за описом помилки

def visual_inside(directory_path, indent=4): # створюємо другорядну функцію візуалізації з відступом 4 від батьківської папки
    for item in directory_path.iterdir(): # ітеруємся по вмісту папки
        if item.is_dir(): # перевіряємо на влкденість іншими папками
            print(Fore.GREEN + f"{' ' * indent}📂 {item.name}") # візуалізуємо вміст папки іншим зеленим коліром, додаємо зображення папки
            visual_inside(item, indent + 4) # рекурсуємо функцію з відступом + 4
        else:
            print(Fore.YELLOW + f"{' ' * indent}📜 {item.name}" + Style.RESET_ALL) # всі елементи внутрі папки, що не є папками позначаємо іконкою та жовтим кольором

if __name__ == "__main__": # додатково перевіряємо правильний виклик скрипту та чи є що викликати
    if len(sys.argv) > 2 : # в конспекті написано ставити >1, але в мене робить тільки після 2. 
        print(Fore.RED + "Помилка: ви не передали аргумент як шлях до папки візуалізації, або папку неможливо візуалізувати. Використайте команду: python назва_скрипту.py /шлях/до/вашої/директорії" + Style.RESET_ALL)
    else:
        directory_path = sys.argv[1]
        visual_structure(directory_path)
        
# Ось таке вийшло: https://drive.google.com/file/d/1UoLc3hxU7lzyMWdtjV2qxuCqgPQtsVoQ/view?usp=drive_link

