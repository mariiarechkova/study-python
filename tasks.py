# Выведите все элементы, которые меньше 5.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for el in a:
#     if el < 5:
#         print(el)


# numbers = [0,1,2,3,4,5,6,7,8,9,10]
# new_numbers = []
# num = int(input("Введите число: "))
# if num:
#     # for el in numbers:
#     #     new_numbers.append(el * num)
#     # print(new_numbers)
#
# # else:
# #     print("Разрешено вводить только числа")

# nums = [0,1,2,3,4,5,6,7,8,9,10]
# user_nums = (input("Введите данные: "))
# new_nums = user_nums.split()
# new_numbers = []

# if new_nums:
#     for el in new_nums:
#         new_numbers.append(int(el))
#     result = [el for el in nums if el in new_numbers]
#     print(result)

# data = [{ 'first_name': 'Masha', 'last_name': 'Rechkova', 'age': 24, },
#         { 'first_name': 'Ivan', 'last_name': 'Ivanov', 'age': 30, 'high': 180 },
#         { 'first_name': 'Andrey', 'last_name': 'Rechkov', 'age': -26 },
#         { 'first_name': 'Barbes', 'last_name': 'Rechkov', 'age': -1 }]
# # print(sorted(el for el in data if el['age'] < 0))
# print(data)
# for el in data:
#     el ['city'] = 'Yerevan'
#
# print(data)


# # for el in data:
# #     print(el['first_name'],el['last_name'])
# command = int(input("Введите возраст: "))
# for el in data:
#     if el['age'] >= command:
#        print(el)
#
# data = [i for i in range (-5,6)]
# print(data)
# print(sorted(x for x in data if x>0))


# def year_season(month):
#     if month in range (1,3) or month == 12:
#         print("Зима")
#     elif month in range (3,6):
#         print("Весна")
#     elif month in range (6,9):
#         print("Лето")
#     elif month in range (9,12):
#         print("Осень")
#
# year_season(2)

# def is_prime(num):
#     if num in range(0,1000) and int(num):
#         print('true')
#     else:
#         print ("false")
#
#
# is_prime(999)

# import datetime
# import pandas as pd
#
# test_date = datetime.datetime.strptime("01-08-2023", "%d-%m-%Y")
#
# K = 31
#
# date_generated = pd.date_range(test_date, periods=K)
#
#
# def date_create(day, month, year):
#     new_date = datetime.datetime(year, month, day)
#     if new_date in date_generated:
#         print("true")
#     else:
#         print ("false")
#
# date_create(1, 8, 2023)
#
#
# x = ['0', '01', '012', '', '012345']
# print(max(x, key= len))
#
# for item in x:
#     result = item.rjust(len(max(x, key= len)), "*")
#     print(result)

# x = [1,2,3,4,0,0,5,6,7,4,7,3,5,6,2]
# y = False
# for index, item in enumerate(x):
#     if len(x) - 1 == index:
#         break
#     if item == x[index + 1] and item == 0:
#         y = True
# print(y)

# def time(list):
#     return list[0]
#
# print(time([1,2,3,4,5]))

# ferm = {'kurochki_legs': 2,
#         'korovki_legs': 4,
#         'svinki_legs': 4}
#
# def ferma (kurochki, korovki, svinki):
#         animals = int(kurochki) * ferm['kurochki_legs'] + int(korovki) * ferm['korovki_legs'] + int(svinki) * ferm['svinki_legs']
#         print(animals)
#
# ferma(3,5,6)

# match = {'win_point': 3,
#         'draw_point': 1,
#         'lose_point': 0}
#
# def games (win, draw, lose):
#         team = int(win) * match['win_point'] + int(draw) * match['draw_point'] + int(lose) * match['lose_point']
#         print(team)

# games(4,5,6)
# x = ["Привет как дела", "Что нового","Пример строки с пробелами"]
# for item in x:
#         print(item.count(" "))

# x = [1,3,4,-5,3,5,6,-8,7,4,-9]
# new_x = []
# for item in x:
#         new_x.append(item)
#         if item < 0:
#                 new_x.append(item**(2))
#
# print(new_x)

# x = [1,3,4,0,3,5,6,0,7,4,-9]
# filtered = filter(lambda item: item !=0, x)
# print(list(filtered))

# x = [1,3,4,0,3,5,6,0,7,4,-9,-35, "asfg"]
# half = int (len(x)/2)
# new_x1 = []
# for i in range(half, len(x)):
#         new_x1.append(x[i])
# for i in range(0, half):
#         new_x1.append(x[i])
#
# print(new_x1)



# half = int (len(x)/2)
# print(x[:half],x[half:])
# x[:half], x[half:] = x[half:], x[:half]
# print(x)

# class Cats:
#         name = None
#         age = None
#         isHappy = None
#
#         def __init__(self, name, age, isHappy):
#                 self.set_data(name, age, isHappy)
#                 self.get_data()
#
#
#         def set_data(self, name, age, isHappy = None):
#                 self.name = name
#                 self.age = age
#                 self.isHappy = isHappy
#         def get_data(self):
#                 print(self.name, "age: ", self.age, ". Happy:", self.isHappy)
#
#
# cat1 = Cats("Barsik", 3, True)
# cat2 = Cats("Barbes", 2, False)
#
# cat1.set_data("fghjk", 2)

# class Building:
#         __year = None
#         __city = None
#
#         def __init__(self, year, city):
#                 self.year = year
#                 self.city = city
#
#         def get_info(self):
#                 print("Year:", self.year, ". City:", self.city)
#
# class School(Building):
#         pupils = 0
#
#         def __init__(self, pupils, year, city):
#                 super(School, self).__init__(year, city)
#                 self.pupils = pupils
#         def get_info(self):
#                 super().get_info()
#                 print("Pupils:", self.pupils)
#
# class House (Building):
#         pass
#
# class Shop (Building):
#         pass
#
# school = School(100,2000, "Moscow")
# school.get_info()
# school.year = 5
# house = House (2000, "Moscow")
# shop = Shop (2000, "Moscow")

# import webbrowser
#
# def validator(func):
#         def wrapper (url):
#                 if "." in url:
#                         func (url)
#                 else:
#                         print("Неверный URL")
#         return wrapper
# @validator
# def open_url (url):
#         webbrowser.open(url)
#
# open_url("https://yandex.ru")

# class Soda:
#         ingredient = None
#
#         def __init__(self, ingredient = ''):
#                 self.ingredient = ingredient
#
#         def show_my_drink (self):
#                 if self.ingredient:
#                     print("Газировка:", self.ingredient)
#                 else:
#                     print("Обычная газировка")
#
#
# fanta = Soda("jkl;")
# fanta.show_my_drink()

# class Nicola:
#     __slots__ = ["name", "age"]
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_person (self):
#         if self.name == "Николай":
#             print("Имя: ", self.name, "Возраст: ", self.age)
#         else:
#             print("Мое имя не", self.name, ", а Николай, ", "Возраст: ", self.age)
#
# Maksim = Nicola ("Максим", 31)
# Maksim.show_person()
# Maksim.surname = "Петров"
# Maksim.show_person()

# class RealString:
#     def __init__(self, firstString, secondString):
#         self.firstString = firstString
#         self.secondString = secondString
#
#     def compare1 (self, firstString, secondString):
#         if len(firstString)== len(secondString):
#             print("Строки равны")
#         else:
#             print("Строки не равны")
#
#     def compare2 (self, firstString, secondString):
#         if len(firstString) > len(secondString):
#             print("Первая строка больше второй")
#
#
#     def compare3(self, firstString, secondString):
#         if len(firstString) < len(secondString):
#             print("Первая строка меньше второй")
#
# x = RealString("abc", "abc")
# x.compare1("abcd", x.firstString + '1111')
# x.compare2("abc", "a")
# x.compare3("a","abc")

# import string
# class Alphabet:
#     def __init__(self,lang, letters):
#         self.lang = lang
#         self.letters = letters
#
#     def print(self):
#         print(self.lang, self.letters)
#
#     def letters_num(self):
#         print(len(alph))
#
# alph = list(string.ascii_lowercase)
# Eng = Alphabet("English: ", alph)
# Eng.print()
# Eng.letters_num()

# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# sorted_values = sorted(my_dict.values())[::-1][0:3]
# print(sorted_values)
#
# sorted_keys = []
#
# for i in sorted_values:
#     for k in my_dict.keys():
#         if my_dict [k] == i:
#             sorted_keys.append(k)
#
#
# print(set(sorted_keys))

# def num (n):
#     print(int(n+n*n+n*n*n))
# num(10)

# def command(list1,list2):
#     result = []
#     for el in list1:
#         if el in list2:
#             result.append(el)
#     # result = [el for el in list1 if el in list2]
#     print(result)
#
# command([1,2,"Привет"],[5,6,1,"Привет"])

# string ='abbc1ppp23456789dpddaaawwwpppppppppppp'
# new_str = list(string)
# count_str = new_str.count("p")
# print(new_str)
# print(count_str)

# list1 = [1,2,3,4,1,5,6,7,3,8,9,4,6,7,2,4,5,6]
# for item in list1:
#     if list1.count(item) > 1:
#         print("Есть повторения")
#         break
#     else:
#         print("Значения уникальны")


# def text (text):
#     words = text.lower().split()
#     longest = ""
#     common = ""
#     for word in words:
#         if len(word) > len(longest):
#             longest = word
#         if words.count(word) > words.count(common):
#             common = word
#     print(longest)
#     print(common)
#
# text("Андрей Напишите программу , которая принимает текст андрей и выводит два слова : "
#      "наиболее часто андрей встречающееся и самое длинное.")

# import datetime
#
# def time_sec (n):
#     time_format = str(datetime.timedelta(seconds=n))
#     print("Time in preferred format :", time_format)
#
# time_sec(1000000000)

# n=2**2179
# print(n)

def gyp(a,b):
    c = ((a ** 2) + (b ** 2))**0.5
    print(f"{c:.10f}")
# округление до 10 цифр после запятой

gyp(200,25568)