# Exercise 1

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

for certain_visit in geo_logs:
    certain_visit = geo_logs.index(certain_visit)
    geo_logs_dicts = geo_logs[certain_visit]
    if list(geo_logs_dicts.values())[0][1] == 'Россия':
        print(list(geo_logs_dicts.values()))

# Exercise 2

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

all = []

for i in range(len(ids)):
    all.extend(ids['user' + str(i + 1)])

print(list(set(all)))

# Exercise 3

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]

certain_list = []
certain_dict = {}
for i in queries:
    amount_queries = len(i.split(" "))
    certain_list.append(amount_queries)
    for a in certain_list:
        if a == amount_queries:
            certain_dict[a] = certain_list.count(a) / len(queries) * 100.
print(certain_dict)
