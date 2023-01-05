# 2.6 Итоги пройденных тем. Проверьте себя

# Задание 1
client = "Петя"
print(client)
print("и")
pet = "Кот"
print(pet)

# Задание 2
r = 'Red'
b = 'Blue'
g = 'Green'

print(r, b, g, r + g + b, b, g + b)

# Задание 3
first_animal = "Заяц"
second_animal = "Черепаха"
print(first_animal + " спит " + second_animal + " идёт.")

# Задание 4
first_name = input('Введите имя пользователя: ')
greeting = 'Утро доброе,'
print(greeting, first_name)
intro = "К сожалению, у Вас нет доступа к системе."
info = "Пожалуйста, обратитесь к системному администратору."
print(intro)
print(info)

# Задание 5
place_departure = input("Город вылета: ")
destination = input("Пункт назаначения: ")
print("Билеты куплены: " + place_departure + "—" + destination)

# Задание 6 (повышенной сложности)
a = input('Введите первое слово: ')
b = input('Введите второе слово: ')
print(a, b)
a, b = b, a  # пришлось гуглить. В целом провёл паралель как в уравнении с X, когда через равенство выводишь
print(a, b)
