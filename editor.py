
# Имя файла
FILENAME = 'audiotracks.csv'

# Функция для чтения базы данных
def read_db():
    with open(FILENAME, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return [line.strip().split(',') for line in lines]

# Функция для записи базы данных
def write_db(data):
    with open(FILENAME, 'w', encoding='utf-8') as file:
        for row in data:
            file.write(','.join(row) + '\n')

# Функция для отображения базы данных
def display_db(data):
    print("Исполнитель,Название трека,Альбом,Год выпуска,Длительность,Количество прослушиваний")
    for idx, row in enumerate(data[1:], start=1):
        row = ','.join(row)
        print(f"{idx}: {row}")

# Функция для добавления записи
def add_record():
    new_record_str = input("Введите запись (исполнитель, название трека, альбом, год выпуска, длительность, количество прослушиваний): ")
    new_record = new_record_str.split(',')

    if len(new_record) != 6:
        print("Ошибка: Введите все 6 значений (исполнитель, название трека, альбом, год, длительность, прослушивания).")
        return

    try:
        year = int(new_record[3])
        if not (1000 <= year <= 2026):  #проверка на диапазон
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
    display_db(db)
    index = int(input("Введите номер записи для удаления: "))
    if 1 <= index < len(db):
        db.pop(index)
        write_db(db)
    print("Запись успешно удалена")

# Функция для редактирования записи
def edit_record():
    display_db(db)
    index = int(input("Введите номер записи для редактирования: "))
    if 1 <= index < len(db):
        field = int(input("Какой ключ редактировать? (1 - Исполнитель, 2 - Название трека, 3 - Альбом, 4 - Год выпуска, 5 - Длительность, 6 - Количество прослушиваний): "))
        new_value = input("Введите новое значение: ")
        db[index][field - 1] = new_value
        write_db(db)

# Основная часть программы
db = read_db()

while True:
    print("\nМеню:")
    print("1. Показать базу данных")
    print("2. Добавить запись")
    print("3. Удалить запись")
    print("4. Редактировать запись")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        display_db(db)
    elif choice == '2':
        add_record()
    elif choice == '3':
        delete_record()
    elif choice == '4':
        edit_record()
    elif choice == '5':
        break
    else:
        print("Такой команды не существует")



