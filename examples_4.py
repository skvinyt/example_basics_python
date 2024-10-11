def generate_pit(depth):
    for i in range(depth):
        # Левая часть ямы
        left_part = ''.join(str(depth - j) for j in range(i + 1))

        # Количество точек
        dots = '.' * (2 * (depth - i - 1))

        # Правая часть ямы
        right_part = ''.join(str(depth - j) for j in range(i, -1, -1))

        # Собираем строку
        line = left_part + dots + right_part

        # Выводим строку
        print(line)

# Запрашиваем у пользователя глубину ямы
N = int(input("Введите глубину ямы: "))

# Генерируем яму
generate_pit(N)
