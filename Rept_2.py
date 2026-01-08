"""Отсортировать медиатеку.

Список всех аудиозаписей конкретного исполнителя, отсортированный по
следующему ключу: альбом (по убыванию) + название трека (по возрастанию).
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


def filter_tracks_by_artist(tracks, artist_name):
    """.

    Функция фильтрует список треков по имени исполнителя,
    делая сравнение нечувствительным к регистру.
    """
    filtered_tracks = [
        track for track in tracks
        if track[0].lower() == artist_name.lower()
    ]
    if not filtered_tracks:
        print(f"Исполнитель '{artist_name}' не найден в списке треков.")
        return []

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
    album1 = track1[2]
    album2 = track2[2]
    title1 = track1[1]
    title2 = track2[1]

    if album1 > album2:
        return -1
    elif album1 < album2:
        return 1
    else:
        if title1 < title2:
            return -1
        elif title1 > title2:
            return 1
        else:
            return 0


def main_sort_2():
    """Основной модуль."""
    filename = 'audiotracks.txt'
    artist_name = input("Введите имя исполнителя: ")
    if artist_name.lower() == 'назад':
        return
    if artist_name.lower() == 'выход':
        exit()
    tracks = read_audiotracks(filename)
    artist_tracks = filter_tracks_by_artist(tracks, artist_name)
    quicksort(artist_tracks, 0, len(artist_tracks) - 1)
    tracks = artist_tracks

    quicksort(tracks, 0, len(tracks) - 1)

    for track in tracks:
        print(','.join(track))
