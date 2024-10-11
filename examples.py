def draw_rectangle(width, height):
    # Верхняя и нижняя границы рамки
    horizontal_border = '+' + '-' * (width - 2) + '+'

    # Вертикальные границы рамки
    vertical_border = '|' + ' ' * (width - 2) + '|'

    # Рисуем верхнюю границу
    print(horizontal_border)

    # Рисуем вертикальные границы
    for _ in range(height - 2):
        print(vertical_border)

    # Рисуем нижнюю границу
    if height > 1:
        print(horizontal_border)

# Запрашиваем у пользователя ширину и высоту рамки
width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))

# Проверяем, что ширина и высота больше 1
if width < 2 or height < 2:
    print("Ширина и высота должны быть больше 1.")
else:
    draw_rectangle(width, height)
