# Python Core
# Модуль 4
# домашнє завдання 1
# Лопатін Євген

from pathlib import Path

with open('salary.txt', 'w') as fh:
    fh.write('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000') 
    

def total_salary(path):
    total_salary = 0  # Вводимо змінну загальної ЗП
    count = 0         # Вводимо змінну загальної кількості працівників

    try:
        with open('salary.txt', 'r', encoding='utf-8') as file:
            for line in file: 
                name, salary = line.strip().split(',') # Розділяємо рядки по комі та відокремлюємо ім'я працівника та цифру ЗП 
                salary = float(salary) # Конвертуємо змінну salary в число float
                total_salary += salary # Сумуємо всі числа ЗП
                count += 1 # Сумуємо кількість працівників
    except FileNotFoundError: # виключаємо помилку шляху
        print("Файл не знайдено. Запровадьте коректний шлях до файлу.")
        return None
    except Exception as e: # виключаємо інші помилки
        print("Сталася помилка:", str(e))
        return None

    
    average_salary = total_salary / count if count > 0 else 0 # розраховуємо середню ЗП

    return total_salary, average_salary

result = total_salary("salary.txt") # вводимо змінну результату по функції, яка бере шлях файлу
if result:
    total, average = result
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")