
def format_name(last, first, middle=None):
    if middle:
        return f"{last} {first[0].upper()}.{middle[0].upper()}."

    return f"{last} {first}"


# Количество записей
m = int(input())

# Обрабатываем каждую запись
for i in range(m):
    data = input().split()

    last = data[0]
    first = data[1]

    if len(data) == 3:
        middle = data[2]
    else:
        middle = None

    print(format_name(last, first, middle))
