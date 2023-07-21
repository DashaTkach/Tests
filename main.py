def first_task(geo_logs):
    res = []
    for dict_ind in range(len(geo_logs)):
        if list(geo_logs[dict_ind].values())[0][1] == 'Россия':
            res.append(list(geo_logs[dict_ind].values()))
    return res


def second_task(ids):
    all = []
    for i in range(len(ids)):
        all.extend(ids['user' + str(i + 1)])
    return list(set(all))


def third_task(queries):
    certain_list = []
    certain_dict = {}
    for i in queries:
        amount_queries = len(i.split(" "))
        certain_list.append(amount_queries)
        for a in certain_list:
            if a == amount_queries:
                certain_dict[a] = certain_list.count(a) / len(queries) * 100.
    return certain_dict


if __name__ == "__main__":
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
    print(first_task(geo_logs))
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    print(second_task(ids))
    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ]
    print(third_task(queries))
