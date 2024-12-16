# 1. Задаем переменные разных типов данных
immutable_var = (1, "строка", 3.14, True, (5, 6))

# 2. Выполняем операции вывода кортежа immutable_var на экран
print(immutable_var)

# 3. Изменение значений переменных
try:
    immutable_var[0] = 10  # Попытка изменить первый элемент кортежа
except TypeError as e:
    print("Ошибка:", e)
    print("Нельзя изменить значения элементов кортежа, так как кортежи являются неизменяемыми (immutable) структурами данных в Python.")

# 4. Создание изменяемых структур данных
mutable_list = [1, "строка", 3.14, True]

# Изменяем элементы списка mutable_list
mutable_list[0] = 10
mutable_list[1] = "новая строка"

# Выводим на экран измененный список mutable_list
print(mutable_list)