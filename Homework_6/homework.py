"""My homework exercise"""
# Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
first_string = "Robin Singh"  # pylint: disable=invalid-name
print(first_string.split())


'''
"I love arrays they are my favorite" =>
["I", "love", "arrays", "they", "are", "my", "favorite"]
'''
second_string = "I love arrays they are my favorite"  # pylint: disable=invalid-name
print(second_string.split())


'''
Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
'''
name_list = ["Ivan", "Ivanou"]
city = 'Minsk'  # pylint: disable=invalid-name
country = 'Belarus'  # pylint: disable=invalid-name
print(f"Привет, {name_list[0]} {name_list[1]}! Добро пожаловать в {city} {country}")


''' 
Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
сделайте из него строку => "I love arrays they are my favorite"
'''
array = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(" ".join(array))

'''
Создайте список из 10 элементов, вставьте на 3-ю
позицию новое значение, удалите элемент из списка под индексом 6
'''

my_list = ["Hi", "World", "13", "Beautiful", "25", "48", "Name", "Sun", "77", "3"]
my_list[3] = "This is replace"
del my_list[6]
print(my_list)
