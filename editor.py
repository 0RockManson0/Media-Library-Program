# Имя файла
FILENAME = 'audiotracks.csv'

# Функция для чтения базы данных
def read_db():
    try:
        with open(FILENAME, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return [line.strip().split(',') for line in lines]
    except FileNotFoundError:
        return []

# Функция для записи базы данных
def write_db(data):
        with open(FILENAME, 'w', encoding='utf-8') as file:
            for row in data:
                file.write(','.join(row) + '\n')

def display_db(data):
    print("Исполнитель,Название трека,Альбом,Год выпуска,Длительность,Количество прослушиваний")
    for idx, row in enumerate(data[1:], start=1):
        row = ','.join(row)
        print(f"{idx}: {row}")

# Функция для добавления записи
def add_record():
    print("Для выхода в меню введите 'назад'. Для выхода из программы введите 'выход'.")
    new_record_str = input("Введите запись (исполнитель, название трека, альбом, год выпуска, длительность, количество прослушиваний): ")

    if new_record_str.lower() == "назад":
        return
    if new_record_str.lower() == "выход":
        exit() #завершение программы

    new_record = new_record_str.split(',')

    if len(new_record) != 6:
        print("Ошибка: Введите все 6 значений (исполнитель, название трека, альбом, год, длительность, прослушивания).")
        return

    try:
        year = int(new_record[3])
        if not (1000 <= year <= 2026):
            print("Ошибка: Год выпуска должен состоять из 4 цифр и быть в разумном диапазоне.")
            return

        long = new_record[4]
        minutes, seconds = map(int, long.split(':'))
        if not (0 <= minutes <= 59 and 0 <= seconds <= 59):
            print("Ошибка: Некорректный формат или значение длительности (MM:SS).")
            return

        listenning = int(new_record[5])
    except ValueError:
        print("Ошибка: Год выпуска и Количество прослушиваний должны быть целыми числами, формат длительности MM:SS.")
        return

    if new_record in db:
        print("Такая запись уже существует в базе данных.")
        return

    db.append(new_record)
    write_db(db)
    print("Запись успешно добавлена")


# Функция для удаления записи
def delete_record():
    print("Для выхода в меню введите 'назад'. Для выхода из программы введите 'выход'.")

    display_db(db) #показать базу данных
    record_del = input("Введите номера записей для удаления через пробел или диапазон (например, 2-5): ") #ввод данных

    if record_del.lower() == "назад":
        return
    if record_del.lower() == "выход":
        exit()

    try:
        if '-' in record_del:
            start, end = map(int, record_del.split('-')) #разделить введенные строчки по -
            indices_to_delete = list(range(start, end + 1)) #сформировать список индексов

        else:
            indices_to_delete = [int(i) for i in record_del.split()] #создать список

        indices_to_delete.sort(reverse=True)  # Удалять с конца, чтобы не нарушить нумерацию

        for index in indices_to_delete: #удаление записей
            if 1 <= index < len(db): #проверить наличие записи в базе
                db.pop(index)
                print(f"Запись {index} успешно удалена")
            else:
                print(f"Записи с номером {index} не существует")

        write_db(db) #записать
        print("Удаление завершено.")

    except ValueError:
        print("Ошибка: Неверный формат ввода.")


# Функция для редактирования записи
def edit_record():
    print("Для выхода в меню введите 'назад'. Для выхода из программы введите 'выход'.")

    display_db(db)
    record_edit = input("Введите номер записи для редактирования: ")

    if record_edit.lower() == "назад":
        return
    if record_edit.lower() == "выход":
        exit()

    try:
        index = int(record_edit)
        if not (0 <= index < len(db)):  # Проверка, что номер записи существует
            print("Ошибка: Такой записи нет")
            return

        field = input("Какой ключ редактировать? (1 - Исполнитель, 2 - Название трека, 3 - Альбом, 4 - Год выпуска, 5 - Длительность, 6 - Количество прослушиваний): ")

        if field.lower() == "назад":
            return
        if field.lower() == "выход":
            exit()

        field = int(field) - 1  # Индекс поля начинается с 0
        if not (0 <= field <= 5): # Проверка валидности ключа
            print("Ошибка: Неверный номер поля.")
            return

        new_value = input("Введите новое значение: ")

        # Дополнительные проверки значения в зависимости от поля
        if field == 3:  # Год выпуска
            try:
                year = int(new_value)
                if not (1000 <= year <= 2026):
                    print("Ошибка: Год выпуска должен состоять из 4 цифр и быть в разумном диапазоне.")
                    return
            except ValueError:
                print("Ошибка: Год выпуска должен быть целым числом.")
                return
        elif field == 4:  # Длительность трека
            try:
                minutes, seconds = map(int, new_value.split(':'))
                if not (0 <= minutes <= 59 and 0 <= seconds <= 59):
                    print("Ошибка: Некорректный формат или значение длительности (MM:SS).")
                    return
            except ValueError:
                print("Ошибка: Некорректный формат длительности (MM:SS).")
                return
        elif field == 5: # Количество прослушиваний:
            try:
                listenning = int(new_value)
            except ValueError:
                print("Ошибка: Количество прослушиваний должно быть целым числом.")
                return

        db[index][field] = new_value
        write_db(db)
        print("Запись успешно отредактирована!")

    except ValueError:
        print("Ошибка: Неверный формат номера записи.")

# Основная часть программы
db = read_db()

while True:
    print("\nМеню:")
    print("1. Показать базу данных")
    print("2. Добавить запись")
    print("3. Удалить запись")
    print("4. Редактировать запись")
    print("Для выхода из программы введите 'выход'.")

    choice = input("Выберите действие: ")

    if choice.lower() == "выход":
        break

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
