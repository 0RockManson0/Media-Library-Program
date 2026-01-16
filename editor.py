"""Программа редактор.

Создать программу, которая считывает файл с записями и позволяет:
1 - Демонстрировать базу данных
2 - Добавлять новые записи
3 - Удалять старые записи
4 - Редактировать существующие записи
Примечание: на любом этапе можно выйти из программы
должна быть возможность откатиться на один этап назад
(если это возможно)
"""

FILENAME = 'audiotracks.txt'


def create():
    """Создает 35 демо-записей для тестирования."""
    return [
        ["Исполнитель,Название трека,Альбом,Год выпуска,"
         "Длительность,Количество прослушиваний"],
        ["Кино,Группа крови,Группа крови,1988,4:20,4800"],
        ["Руки Вверх,18 мне уже,Руки вверх,1997,4:04,4300"],
        ["Звери,Лето,На ощупь,2019,3:45,2900"],
        ["Billie Eilish, Bad Guy, When We All Fall Asleep. Where"
         " Do We Go?, 2019, 3:14, 2200000"],
        ["Баста, Моя игра, Баста 1, 2006, 4:31, 107000"],
        ["Руки Вверх, Крошка моя, Сделай ещё громче!, 1998, 3:43,"
         " 100000000"],
        ["Imagine Dragons, Believer, Evolve,2017, 3:24, 1900000"],
        ["Звери, До скорой встречи!, Когда мы вместе никто не круче, 2005,"
         " 5:09, 140000000"],
        ["Ed Sheeran, Shape of You, ÷, 2017, 3:53, 1500000"],
        ["Billie Eilish, everything i wanted, When We All Fall Asleep. Where "
         "Do We Go?, 2019, 3:14, 1600000000"],
        ["Баста, Мама, Баста 1, 2006, 4:14, 26000000"],
        ["Руки Вверх, Чужие губы, Сделай ещё громче!, 1998, 4:02, 3100000"],
        ["Imagine Dragons, Thunder, Evolve,2017, 3:08, 1000000000"],
        ["Звери, Рома извини, Когда мы вместе никто не круче, 2005, 3:46,"
         " 22600000"],
        ["Кино,В наших глазах,Группа крови,1988,3:35,446000"],
        ["Billie Eilish, BLUE, Hit Me Hard and Soft, 2024, 5:43, "
         "140000000"],
        ["Баста, Выпускной (Медлячок), Баста 5, 2016, 5:44, 17000000"],
        ["Руки Вверх, Алёшка, Здравствуй это я, 2000, 3:25, 4300000"],
        ["Ed Sheeran, Perfect, ÷, 2017, 4:42, 3000000000"],
        ["Кино,Кукушка,Чёрный альбом,1990,6:27,9800000"],
        ["Imagine Dragons, Enemy, Arcane League of Legends,2022,3:34,"
         "123000000"],
        ["Ed Sheeran, Shivers, =, 2021, 3:58, 1300000000"],
        ["Звери,Районы-кварталы, Районы-кварталы, 2004, 4:35, "
         "14400000"],
        ["Кино,Стук (Одно лишь слово),Звезда по имени Солнце,1989,3:40,"
         "4350000"],
        ["Ed Sheeran, Bad Habits, =, 2021, 4:01, 1140000000"],
        ["Billie Eilish, LUNCH, Hit Me Hard and Soft, 2024, 3:22, 134000000"],
        ["Баста, Мои разбитые мечты, Баста 5, 2016, 5:27, 13200000"],
        ["Imagine Dragons, Radioactive, Night Visions,2012,4:22,1342000000"],
        ["Кино,Звезда по имени Солнце,Звезда по имени Солнце,1989,3:46,"
         "12550000"],
        ["Руки Вверх, Ай-яй-яй, Здравствуй это я, 2000, 3:49, 14300000"],
        ["Звери,Всё что касается, Районы-кварталы, 2004, 3:30, 121000000"],
        ["Ed Sheeran, Perfect Duet, Perfect Duet, 2017, 4:19, 123000000"],
        ["Billie Eilish, Hotline Bling (Liquid Memoirs bootleg), party favor,"
         " 2018, 2:09, 890000000"],
        ["Баста, Где ты теперь и с кем, Где ты теперь и с кем, 2023,"
         " 2:44, 16720000"],
        ["Imagine Dragons, Demons, Night Visions,2012,3:57,1649900000"]
    ]


def read_db():
    """Функция для чтения базы данных."""
    try:
        with open(FILENAME, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return [line.strip().split(',') for line in lines]
    except FileNotFoundError:
        return []


def write_db(data):
    """Функция для записи базы данных."""
    with open(FILENAME, 'w', encoding='utf-8') as file:
        for row in data:
            file.write(','.join(row) + '\n')


def display_db(data):
    """Функция для демонстрации данных."""
    # Получаем ширину каждого столбца на основе самой длинной строки в этом столбце
    column_widths = [max(len(str(item)) for item in column) for column in
                     zip(*data)]

    # Выводим заголовок с выравниванием по ширине столбцов
    header = data[0]
    formatted_header = " | ".join(
        f"{header[i]:<{column_widths[i]}}" for i in range(len(header)))
    print(formatted_header)

    # Выводим разделительную линию
    print("-" * len(formatted_header))

    # Выводим данные с выравниванием по ширине столбцов
    for idx, row in enumerate(data[1:], start=1):
        formatted_row = " | ".join(
            f"{row[i]:<{column_widths[i]}}" for i in range(len(row)))
        print(f"{idx}: {formatted_row}")



def add_record():
    """Функция для добавления записи."""
    print("Для выхода в меню введите 'назад'. Для выхода из"
          "программы введите 'выход'.")
    new_record_str = input("Введите запись (исполнитель,"
                           "название трека, альбом, год выпуска,"
                           "длительность, количество прослушиваний): ")

    if new_record_str.lower() == "назад":
        return
    if new_record_str.lower() == "выход":
        exit()

    new_record = new_record_str.split(',')

    if len(new_record) != 6:
        print("Ошибка: Введите все 6 значений (исполнитель,"
              "название трека, альбом, год, длительность, прослушивания).")
        return

    try:
        year = int(new_record[3])
        if not (1000 <= year <= 2026):
            print("Ошибка: Год выпуска должен состоять из 4 цифр"
                  "и быть в разумном диапазоне.")
            return

        long = new_record[4]
        minutes, seconds = map(int, long.split(':'))
        if not (0 <= minutes <= 59 and 0 <= seconds <= 59):
            print("Ошибка: Некорректный формат или значение"
                  "длительности (MM:SS).")
            return

        int(new_record[5])
    except ValueError:
        print("Ошибка: Год выпуска и Количество прослушиваний"
              "должны быть целыми числами, формат длительности MM:SS.")
        return

    if new_record in db:
        print("Такая запись уже существует в базе данных.")
        return

    db.append(new_record)
    write_db(db)
    print("Запись успешно добавлена")


def delete_record():
    """Удаляет запись из базы данных."""
    if len(db) <= 1:  # Проверка пустой базы данных (учитываем заголовок)
        print("База данных пуста. Добавьте хотя бы одну запись.")
        return

    print("Для выхода в меню введите 'назад'."
          " Для выхода из программы введите 'выход'.")

    display_db(db)
    record_del = input("Введите номера записей для удаления"
                       " через пробел или"
                       " диапазон (например, 2-5): ")

    if record_del.lower() == "назад":
        return
    if record_del.lower() == "выход":
        exit()

    try:
        if '-' in record_del:
            start, end = map(int, record_del.split('-'))
            indices_to_delete = list(range(start, end + 1))

        else:
            indices_to_delete = [int(i) for i in record_del.split()]

        indices_to_delete.sort(reverse=True)

        for index in indices_to_delete:
            if 1 <= index < len(db):
                db.pop(index)
                print(f"Запись {index} успешно удалена")
            else:
                print(f"Записи с номером {index} не существует")

        write_db(db)
        print("Удаление завершено.")

    except ValueError:
        print("Ошибка: Неверный формат ввода.")


def edit_record():
    """Редактирует запись в базе данных."""
    if len(db) <= 1:  # Проверка пустой базы данных (учитываем заголовок)
        print("База данных пуста. Добавьте хотя бы одну запись.")
        return

    print("Для выхода в меню введите 'назад'."
          " Для выхода из программы введите 'выход'.")

    display_db(db)
    record_edit = input("Введите номер записи для редактирования: ")

    if record_edit.lower() == "назад":
        return
    if record_edit.lower() == "выход":
        exit()

    try:
        index = int(record_edit)
        if not (0 <= index < len(db)):
            print("Ошибка: Такой записи нет")
            return

        field = input("Какой ключ редактировать? (1 - Исполнитель,"
                      "2 - Название трека, 3 - Альбом, 4 - Год выпуска,"
                      "5 - Длительность, 6 - Количество прослушиваний): ")

        if field.lower() == "назад":
            return
        if field.lower() == "выход":
            exit()

        field = int(field) - 1
        if not (0 <= field <= 5):
            print("Ошибка: Неверный номер поля.")
            return

        new_value = input("Введите новое значение: ")

        if field == 3:
            try:
                year = int(new_value)
                if not (1000 <= year <= 2026):
                    print("Ошибка: Год выпуска должен состоять"
                          " из 4 цифр и быть в разумном диапазоне.")
                    return
            except ValueError:
                print("Ошибка: Год выпуска должен быть целым числом.")
                return
        elif field == 4:
            try:
                minutes, seconds = map(int, new_value.split(':'))
                if not (0 <= minutes <= 59 and 0 <= seconds <= 59):
                    print("Ошибка: Некорректный формат или"
                          " значение длительности (MM:SS).")
                    return
            except ValueError:
                print("Ошибка: Некорректный формат"
                      " длительности (MM:SS).")
                return
        elif field == 5:
            try:
                int(new_value)
            except ValueError:
                print("Ошибка: Количество прослушиваний"
                      " должно быть целым числом.")
                return

        db[index][field] = new_value
        write_db(db)
        print("Запись успешно отредактирована!")

    except ValueError:
        print("Ошибка: Неверный формат номера записи.")


db = read_db()
