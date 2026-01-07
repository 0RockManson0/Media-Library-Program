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
        while compare_tracks(arr[i], pivot) < 0 and i < high: # Добавлена проверка i < high
            i += 1

        j -= 1
        while compare_tracks(arr[j], pivot) > 0 and j > low: # Добавлена проверка j > low
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]

def compare_tracks(track1, track2):
    """Функция сравнения треков для сортировки."""
    if track1[0] != track2[0]:
        return 1 if track1[0] > track2[0] else -1
    elif track1[3] != track2[3]:
        return int(track2[3]) - int(track1[3])
    else:
        try:
            return int(track2[5]) - int(track1[5])
        except ValueError:
            print(f"Ошибка: Некорректное значение прослушиваний: track1={track1[5]}, track2={track2[5]}")
            return 0  # Возвращаем нейтральное значение при ошибке

def load_tracks(filename="audiotracks.txt", encoding="utf-8"):
    """Чтение данных из файла."""
    tracks = []
    try:
        with open(filename, 'r', encoding=encoding) as f:
            next(f) #Пропускаем строку заголовка
            for line in f:
                track_data = line.strip().split(',')
                tracks.append(track_data)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
        return []
    return tracks

def print_tracks(tracks):
    """Вывод списка треков."""
    for track in tracks:
        print(','.join(track))

# Основная часть
tracks = load_tracks()
if tracks:
    quicksort(tracks, 0, len(tracks) - 1)
    print_tracks(tracks)
