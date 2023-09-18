import random
HELP = """
help - напечатать справку по программе.
add - добавить задачу в справку (название задачи запрашиваем у пользователя.
show - напечатать все добавленные задачи.
random - добавлять случайную задачу на дату Сегодня"""

tasks = {

}

def add_todo (date,task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = [task]
    print("Задача ", task, "добавлена на дату", date)


RANDOM_TASKS = ["Погулять", "Поесть", "Поспать","Погладить кота"]

run = True

while run:
    command = input ("Введите комманду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения задач: ")
        if date in tasks:
            for task in tasks[date]:
                print('-', task)
        else:
            print("Такой даты нет")
    elif command == "add":
        date = input("Введите дату:")
        task = input("Введите название задачи:")
        add_todo(date, task)
    elif command == "random":
        task = random.choice (RANDOM_TASKS)
        add_todo("Сегодня", task)
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная комманда")
        break

print("До свидания!")

