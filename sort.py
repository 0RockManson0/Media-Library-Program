"""Universal sorting functions for media library management"""
import editor

def quicksort(arr, low, high, compare_func):
    """General-purpose quicksort using Hoare's method."""
    if low < high:
        pi = partition(arr, low, high, compare_func)
        quicksort(arr, low, pi, compare_func)
        quicksort(arr, pi + 1, high, compare_func)

def partition(arr, low, high, compare_func):
    """Partition an array for quicksort using Hoare's method."""
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while compare_func(arr[i], pivot) < 0:
            i += 1

        j -= 1
        while compare_func(arr[j], pivot) > 0:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]

# Используем функции из editor.py
def load_tracks(filename="audiotracks.txt"):
    """Reading data from file using editor module."""
    return editor.read_db()

def print_tracks(tracks):
    """Print the list of tracks using editor module."""
    if tracks:
        # Добавляем заголовок для правильного отображения
        header = ["Исполнитель", "Название трека", "Альбом",
                  "Год выпуска", "Длительность", "Количество прослушиваний"]
        if len(tracks[0]) != 6 or tracks[0][0] != "Исполнитель":
            tracks = [header] + tracks
        editor.display_db(tracks)

# Функции фильтрации теперь работают с данными из editor.py
def filter_tracks_by_artist(tracks, artist_name):
    """Filter tracks by artist name (case-insensitive)."""
    # Пропускаем заголовок если он есть
    if len(tracks) > 0 and len(tracks[0]) == 6 and tracks[0][0] == "Исполнитель":
        data_start = 1
    else:
        data_start = 0

    filtered_tracks = [
        track for track in tracks[data_start:]
        if track[0].lower() == artist_name.lower()
    ]

    if not filtered_tracks:
        print(f"Исполнитель '{artist_name}' не найден в списке треков.")
        return []

    # Возвращаем с заголовком для совместимости
    if data_start == 1:
        return [tracks[0]] + filtered_tracks
    else:
        # Создаем заголовок если его нет
        header = ["Исполнитель", "Название трека", "Альбом",
                  "Год выпуска", "Длительность", "Количество прослушиваний"]
        return [header] + filtered_tracks

def filter_tracks_by_year(tracks, start_year, end_year):
    """Filter tracks by a range of years."""
    # Пропускаем заголовок если он есть
    if len(tracks) > 0 and len(tracks[0]) == 6 and tracks[0][0] == "Исполнитель":
        data_start = 1
        header = tracks[0]
    else:
        data_start = 0
        header = ["Исполнитель", "Название трека", "Альбом",
                  "Год выпуска", "Длительность", "Количество прослушиваний"]

    filtered_tracks = []
    for track in tracks[data_start:]:
        try:
            year = int(track[3])
            if start_year <= year <= end_year:
                filtered_tracks.append(track)
        except ValueError:
            continue

    if not filtered_tracks:
        return []

    return [header] + filtered_tracks

# Comparison functions for different sorting requirements
def compare_sort_1(track1, track2):
    """
    Sort by: artist (ascending) + year of release (descending) + number of plays (descending)
    """
    # Сравниваем исполнителя (по возрастанию)
    artist1, artist2 = track1[0], track2[0]
    if artist1 != artist2:
        return -1 if artist1 < artist2 else 1

    # Сравниваем год (по убыванию)
    try:
        year1 = int(track1[3])
        year2 = int(track2[3])
        if year1 != year2:
            return 1 if year1 < year2 else -1
    except ValueError:
        pass

    # Сравниваем количество прослушиваний (по убыванию)
    try:
        plays1 = int(track1[5])
        plays2 = int(track2[5])
        return 1 if plays1 < plays2 else -1 if plays1 > plays2 else 0
    except ValueError:
        return 0

def compare_sort_2(track1, track2):
    """
    Sort by: album (descending) + track title (ascending)
    """
    # Сравниваем альбом (по убыванию)
    album1, album2 = track1[2], track2[2]
    if album1 != album2:
        return 1 if album1 < album2 else -1

    # Сравниваем название трека (по возрастанию)
    title1, title2 = track1[1], track2[1]
    return -1 if title1 < title2 else 1 if title1 > title2 else 0

def compare_sort_3(track1, track2):
    """
    Sort by: year of release (descending) + artist (ascending)
    """
    # Сравниваем год (по убыванию)
    try:
        year1 = int(track1[3])
        year2 = int(track2[3])
        if year1 != year2:
            return 1 if year1 < year2 else -1
    except ValueError:
        pass

    # Сравниваем исполнителя (по возрастанию)
    artist1, artist2 = track1[0], track2[0]
    return -1 if artist1 < artist2 else 1 if artist1 > artist2 else 0

def main_sort_1():
    """List all audio recordings sorted by: artist (ascending) + year (descending) + plays (descending)"""
    tracks = load_tracks()
    if len(tracks) <= 1:  # Check if database is empty, considering header
        print("База данных пуста. Добавьте хотя бы одну запись.")
        return
    if tracks:
        # Сортируем только данные, без заголовка
        if len(tracks[0]) == 6 and tracks[0][0] == "Исполнитель":
            data = tracks[1:]  # Пропускаем заголовок
            header = tracks[0]
        else:
            data = tracks
            header = ["Исполнитель", "Название трека", "Альбом",
                      "Год выпуска", "Длительность", "Количество прослушиваний"]

        quicksort(data, 0, len(data) - 1, compare_sort_1)
        print_tracks([header] + data)

def main_sort_2():
    """List all audio recordings of a specific artist sorted by: album (descending) + track title (ascending)"""
    tracks = load_tracks()
    if len(tracks) <= 1:
        print("База данных пуста. Добавьте хотя бы одну запись.")
        return
    artist_name = input("Введите имя исполнителя: ")

    if artist_name.lower() == 'назад':
        return
    if artist_name.lower() == 'выход':
        exit()

    tracks = load_tracks()
    artist_tracks = filter_tracks_by_artist(tracks, artist_name)

    if artist_tracks:
        # Сортируем только данные, без заголовка
        if len(artist_tracks[0]) == 6 and artist_tracks[0][0] == "Исполнитель":
            data = artist_tracks[1:]  # Пропускаем заголовок
            header = artist_tracks[0]
        else:
            data = artist_tracks
            header = ["Исполнитель", "Название трека", "Альбом",
                      "Год выпуска", "Длительность", "Количество прослушиваний"]

        quicksort(data, 0, len(data) - 1, compare_sort_2)
        print_tracks([header] + data)

def main_sort_3():
    """List all audio recordings released between years N1 and N2 sorted by: year (descending) + artist (ascending)"""
    tracks = load_tracks()
    if len(tracks) <= 1:
        print("База данных пуста. Добавьте хотя бы одну запись.")
        return

    while True:
        try:
            start_year = input("Введите начальный год: ")
            if start_year.lower() == 'назад':
                return
            if start_year.lower() == 'выход':
                exit()
            start_year = int(start_year)

            end_year = input("Введите конечный год: ")
            if end_year.lower() == 'назад':
                return
            if end_year.lower() == 'выход':
                exit()
            end_year = int(end_year)

            break
        except ValueError:
            print('Неверный ввод. Пожалуйста, введите корректные годы.')
            continue

    filtered_tracks = filter_tracks_by_year(tracks, start_year, end_year)

    if filtered_tracks:
        # Сортируем только данные, без заголовка
        if len(filtered_tracks[0]) == 6 and filtered_tracks[0][0] == "Исполнитель":
            data = filtered_tracks[1:]  # Пропускаем заголовок
            header = filtered_tracks[0]
        else:
            data = filtered_tracks
            header = ["Исполнитель", "Название трека", "Альбом",
                      "Год выпуска", "Длительность", "Количество прослушиваний"]

        quicksort(data, 0, len(data) - 1, compare_sort_3)
        print_tracks([header] + data)
    else:
        print("Нет треков, выпущенных в указанном диапазоне лет.")




