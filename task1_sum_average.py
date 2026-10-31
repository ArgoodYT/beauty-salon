
# Считываем количество элементов
n = int(input())

# Считываем значения
tokens = input().split()

values = []

for token in tokens:
    if token == "True":
        values.append(1)
    elif token == "False":
        values.append(0)
    else:
        number = float(token)

        # Если число целое, сохраняем его как int
        if number.is_integer():
            number = int(number)

        values.append(number)

# Вычисляем сумму
total = sum(values)

# Вычисляем среднее
average = total / n

# Выводим результаты
print(total, f"{average:.6f}")
