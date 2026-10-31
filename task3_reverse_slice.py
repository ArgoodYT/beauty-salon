
# Считываем строку
s = input()

# Считываем границы
i, j = map(int, input().split())

# Разворачиваем выбранную часть строки
result = s[:i] + s[i:j][::-1] + s[j:]

print(result)
