def guess_number():
    start = 1
    finish = 100
    count = 0

    while start <= finish:
        count += 1
        n = (start + finish) // 2
        print(f"Твоё число равно, меньше или больше, чем число {n}? (1 — равно, 2 — больше, 3 — меньше)")
        answer = int(input())

        if answer == 1:
            print(f"Число угадано за {count} попыток!")
            break
        elif answer == 2:
            start = n + 1
        elif answer == 3:
            finish = n - 1
        else:
            print("Некорректный ответ. Пожалуйста, введите 1, 2 или 3.")

    if start > finish:
        print("Что-то пошло не так. Пожалуйста, попробуйте снова.")

# Запускаем программу
guess_number()
