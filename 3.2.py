# Выполнить функцию, которая принимает несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город
# проживания, email, телефон.Функция должна принимать параметры
# как именованные аргументы.Осуществить вывод данных о пользователе одной строкой.

def user_info(name, surname, year, city, email, phone):
    return f'{name} {surname} {year} {city} {email} {phone}'
n = input('Имя: ')
s = input('Фамилия: ')
y = input('Год рождения: ')
c = input('Город проживания: ')
e = input('email: ')
p = input('Телефон: ')
result = user_info(name=n, surname=s, year=y, city=c, email=e, phone=p)
print(result)
