# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

help_d = {}

for i in students:
    name = i['first_name']
    if name not in help_d:
        help_d[name] = 1
    else:
        help_d[name] += 1
print(help_d)
for k, v in help_d.items():
    print(k, v)
  

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

help_d = {}

for i in students:
    name = i['first_name']
    if name not in help_d:
        help_d[name] = 1
    else:
        help_d[name] += 1
res = max(help_d.items(), key=lambda x:x[1])
print('Самое частое имя среди учеников:',res[0])



# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

help_d = {'1class':{},'2class':{}}

for lst in range(len(school_students)):
    for i in school_students[lst]:
        #print(i)
        student = i['first_name']
        #print(student)
        if i in school_students[0]:   
            if student not in help_d['1class']:
                help_d['1class'][student] = 1
            else:
                help_d['1class'][student] += 1
        elif i in school_students[1]:
            if student not in help_d['2class']: 
                help_d['2class'][student] = 1
            else:
                help_d['2class'][student] += 1

print(help_d)
res1 = max(help_d['1class'].items(), key=lambda x:x[0])
res2 = max(help_d['2class'].items(), key=lambda x:x[1])
print('Самое частое имя в классе 1:',res1[0])
print('Самое частое имя в классе 2:',res2[0])

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

help_d = {'2a':{'girls': 0, 'boys': 0}, '3c':{'girls': 0 , 'boys': 0}}

for i in school:
    #print(i)
    names = i['students']
    #print(222,names)
    for name in names:
        student = name['first_name']
        #print(1111,name)
        #print(student)
        if is_male[student] is True:
            name = 'Мальчик'
            help_d['3c']['boys'] += 1
        else:
            name = 'девочка'
            help_d['2a']['girls'] += 1
for k, v in help_d.items():
    otvet = f'В классе {k} девочек {v["girls"]} мальчиков {v["boys"]}'
    print(otvet)

        

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

help_d = {'2a':{'girls': 0, 'boys': 0}, '3c':{'girls': 0 , 'boys': 0}}

for i in school:
    #print(i)
    names = i['students']
    #print(222,names)
    for name in names:
        student = name['first_name']
        #print(1111,name)
        #print(student)
        if is_male[student] is True:
            name = 'Мальчик'
            help_d['3c']['boys'] += 1
        else:
            name = 'девочка'
            help_d['2a']['girls'] += 1
print(help_d)
res1 = sorted(help_d.keys())
res2 = sorted(help_d.keys())
print('Больше всего девочек в классе',res1[0])
print('Больше всего мальчиков в классе',res2[1])

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a