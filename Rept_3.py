"""Отсортировать медиатеку.

Список всех аудиозаписей, выпущенных в период с N1 до N2 года, отсортированный
по следующему ключу: год выпуска (по убыванию) + исполнитель (по возрастанию).
Использовать метод Хоара
"""


def read_audiotracks(filename):
    """Чтение данных из файла."""
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    tracks = []
    for line in lines[1:]:
        parts = line.strip().split(',')
        if len(parts) >= 6:
            artist = parts[0].strip()
            title = parts[1].strip()
            album = parts[2].strip()
            year = parts[3].strip()
            duration = parts[4].strip()
            listens = parts[5].strip()
            tracks.append((artist, title, album, year, duration, listens))
    return tracks


def filter_tracks_by_year(tracks, start_year, end_year):
    """Фильтрует треки по диапазону лет."""
    filtered_tracks = []
    for track in tracks:
        year = int(track[3])
        if start_year <= year <= end_year:
            filtered_tracks.append(track)
    return filtered_tracks


def quicksort(arr, low, high):
    """Реализация быстрой сортировки (Хоара)."""
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi)
        quicksort(arr, pi + 1, high)


def partition(arr, low, high):
    """Разбиение массива (схема Хоара)."""
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while compare_tracks(arr[i], pivot) < 0:
            i += 1

        j -= 1
        while compare_tracks(arr[j], pivot) > 0:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def compare_tracks(track1, track2):
    """Функция сравнения треков для сортировки."""
    year1 = int(track1[3])
    year2 = int(track2[3])
    artist1 = track1[0]
    artist2 = track2[0]
    if year1 != year2:
        return year2 - year1
    else:
        return (artist1 > artist2) - (artist1 < artist2)


def main_sort_3():
    """Основной модуль."""
    filename = 'audiotracks.txt'
    tracks = read_audiotracks(filename)
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
            print('Неправильный ввод. Введите числа')
            continue
    filtered_tracks = filter_tracks_by_year(tracks, start_year, end_year)
    if filtered_tracks:
        quicksort(filtered_tracks, 0, len(filtered_tracks) - 1)
        for track in filtered_tracks:
            print(','.join(track))
    else:
        print("Нет треков, выпущенных в указанном диапазоне лет.")
