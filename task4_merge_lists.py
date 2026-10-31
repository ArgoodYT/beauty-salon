
# Считываем первый список
n = int(input())

if n > 0:
    list1 = list(map(int, input().split()))
else:
    list1 = []

# Считываем второй список
m = int(input())

if m > 0:
    list2 = list(map(int, input().split()))
else:
    list2 = []

# Создаём итоговый список
result = []

# Множество для проверки повторений
seen = set()

# Объединяем списки
for number in list1 + list2:
    if number not in seen:
        result.append(number)
        seen.add(number)

# Выводим результат
print(*result)
