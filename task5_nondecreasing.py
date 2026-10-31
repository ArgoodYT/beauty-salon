
# Считываем количество чисел
n = int(input())

if n == 0:
    print(0)
else:
    numbers = list(map(int, input().split()))

    # Начальная длина фрагмента
    current_length = 1
    max_length = 1

    # Перебираем числа
    for i in range(1, n):
        if numbers[i] >= numbers[i - 1]:
            current_length += 1
        else:
            current_length = 1

        # Обновляем максимальную длину
        max_length = max(max_length, current_length)

    print(max_length)
