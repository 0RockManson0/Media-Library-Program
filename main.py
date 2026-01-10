""".

Реализовать удобное меню для запуска сортировки
и редактирования базы данных
"""

from editor import *
from Rept_1 import *
from Rept_2 import *
from Rept_3 import *

records = read_db()

if not records:
    print("\nБаза данных пуста")
    demo_choice = input("Создать демо-данные? (да/нет): ").lower()
    if demo_choice in ['да', 'д', 'yes', 'y']:
        records = create()
        write_db(records)
        print(f"Создано {len(records)} демо-записей")
    else:
        title = [["Исполнитель,Название трека,Альбом,Год "
                  "выпуска,Длительность,Количество прослушиваний"]]
        write_db(title)
        print("Создана пустая медиатека")
    display_db(records)
    print("Данные сохранены. Повторно запустите код чтобы увидеть изменения!")

while True:
    print("\nМеню:")
    print("1. Показать базу данных")
    print("2. Меню редактора")
    print("3. Меню создания отчётов")
    print("Для выхода из программы введите 'выход'.")
    choice = input("Выберите действие: ")

    if choice.lower() == "выход":
        break
    if choice == '1':
        display_db(db)
    elif choice == '2':
        while True:
            print("\nМеню редактора:")
            print("1. Показать базу данных")
            print("2. Добавить запись")
            print("3. Удалить запись")
            print("4. Редактировать запись")
            print("Для выхода из программы введите 'выход'.")
            print("Чтобы вернуться обратно введите 'назад'")
            choice = input("Выберите действие: ")
            if choice.lower() == "назад":
                break
            if choice.lower() == "выход":
                exit()
            if choice == '1':
                display_db(db)
            elif choice == '2':
                add_record()
            elif choice == '3':
                delete_record()
            elif choice == '4':
                edit_record()
            else:
                print("Такой команды не существует")
    elif choice == '3':
        while True:
            print("\nМеню создания отчётов:")
            print("1. Полный список всех учеников, отсортированный"
                  " по следующему ключу: класс (по возрастанию)"
                  " + фамилия (по возрастанию).")
            print("2. Список всех аудиозаписей конкретного исполнителя,"
                  " отсортированный по следующему ключу: альбом (по убыванию)"
                  " + название трека (по возрастанию).")
            print("3. Список всех аудиозаписей, выпущенных в "
                  "период с N1 до N2 года,"
                  " отсортированный по следующему ключу: год"
                  " выпуска (по убыванию)"
                  " + исполнитель (по возрастанию).")
            print("Для выхода из программы введите 'выход'.")
            print("Чтобы вернуться обратно введите 'назад'")
            choice = input("Выберите действие: ")
            if choice.lower() == "назад":
                break
            if choice.lower() == "выход":
                exit()
            elif choice == '1':
                main_sort_1()
            elif choice == '2':
                main_sort_2()
            elif choice == '3':
                main_sort_3()
    else:
        print("Такой команды не существует")
