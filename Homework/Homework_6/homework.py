"""My homework exercise"""
# Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
s_1 = "Robin Singh"  # pylint: disable=invalid-name
print(s_1.split())


# I love arrays they are my favorite" =>
# ["I", "love", "arrays", "they", "are", "my", "favorite"]

s_2 = "I love arrays they are my favorite"  # pylint: disable=invalid-name
print(s_2.split())


# Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

data = ["Ivan", "Ivanou"]
city = 'Minsk'  # pylint: disable=invalid-name
country = 'Belarus'  # pylint: disable=invalid-name
print(f"Привет, {data[0]} {data[1]}! Добро пожаловать в {city} {country}")


# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"

array = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(" ".join(array))


# Создайте список из 10 элементов, вставьте на 3-ю
# позицию новое значение, удалите элемент из списка под индексом 6


my_list = ["Hi", "World", "13", "Fly", "25", "48", "Name", "Sun", "77", "3"]
my_list[3] = "This is replace"
del my_list[6]
print(my_list)
