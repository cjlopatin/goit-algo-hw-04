# Python Core
# Модуль 4
# домашнє завдання 4
# Лопатін Євген


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    count = 1
    while True:
        if name in contacts:
            name = name.split("_")[0]
            name = f'{name}_{count}'
            count += 1
        else:
            break
    contacts[name] = phone
    return "Контакт добавлений."

def change_contact(args, contacts):
    name, phone = args
    if not name in contacts:
        raise ValueError("Contact")
    contacts[name] = phone
    return "Контакт оновлений."

def all_contact(contacts):
    return contacts

def phone_contact(args, contacts):
    name = args[0]
    return contacts[name] 

   
def main():
    contacts = {}
    print("Вас вітає штучний асистент!\n Вам доступні наступні команди:\n привітальна команда hello \n команда для додавання користувача: add --тут вводиться імя-- --тут вводиться телефон--\n команда для зміни телефону користувача: change --тут вводиться імя-- --тут вводиться новий телефон-- \n команда для виведення телефону за іменем: phone --тут вводиться імя-- \n команда для виводу всіх збережених контактів: all \n для завершення розмови використовуйте команди close або exit ")
    while True:
        user_input = input("Введіть відповідну команду для продовження, або введіть exit для виходу): ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("До побачення!")
            break

        elif command == "hello":
            print("Як я можу Вам допомогти?")
        
        elif command == "add":
            print(add_contact(args, contacts))
            
        elif command == "change":
            print(change_contact(args, contacts))
            
        elif command == "phone":
            print(phone_contact(args, contacts))
            
        elif command == "all":
            print(all_contact(contacts))
        
        else:
            print("Неправильна команда: введіть правильну команду для продовження, або введіть exit для виходу.")

if __name__ == "__main__":
    main()
