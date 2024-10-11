import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def count_primes(sequence):
    prime_count = 0
    for number in sequence:
        if is_prime(number):
            prime_count += 1
    return prime_count

# Запрашиваем у пользователя количество чисел
n = int(input("Введите количество чисел: "))

# Создаем список для хранения последовательности чисел
sequence = []

# Запрашиваем у пользователя каждое число и добавляем его в последовательность
for _ in range(n):
    number = int(input("Введите число: "))
    sequence.append(number)

# Считаем количество простых чисел в последовательности
prime_count = count_primes(sequence)

# Выводим результат
print(f"Количество простых чисел в последовательности: {prime_count}")
