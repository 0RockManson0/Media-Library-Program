
def read_audiotracks(filename):
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
    return [track for track in tracks if track[0] == artist_name]



filename = 'audiotracks.txt'
artist_name = input("Введите имя исполнителя: ")
tracks = read_audiotracks(filename)
artist_tracks = filter_tracks_by_artist(tracks, artist_name)
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
        while compare_tracks(arr[i], pivot) < 0: # Убрали i < high, т.к. это уже условие выхода из цикла.
            i += 1

        j -= 1
        while compare_tracks(arr[j], pivot) > 0: # Убрали j > low, т.к. это уже условие выхода из цикла.
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

    # Сначала сравниваем альбомы по убыванию.
    if album1 > album2:
        return -1
    elif album1 < album2:
        return 1
    else: # если альбомы равны
        # Сравниваем названия треков по возрастанию.
        if title1 < title2:
            return -1
        elif title1 > title2:
            return 1
        else:
            return 0


def main():
    quicksort(artist_tracks, 0, len(artist_tracks) - 1)
    tracks = artist_tracks

    quicksort(tracks, 0, len(tracks) - 1) # Запускаем сортировку

    for track in tracks: # Выводим отсортированный массив.
        print(','.join(track))
main()

