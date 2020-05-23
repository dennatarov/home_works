# 1. Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено только четное количество таких слов.

def word_in_file_deleter(f_name):
    with open(f_name, "r") as f:
        lines = [line.split() for line in f]
        new_lines = []
    for line in lines:
        new_line = list(filter(lambda w: 2 < len(w) < 6, line))
        n_true = len(new_line)
        if n_true > 1:
            if n_true % 2 != 0: new_line.pop(-1)
            for word in new_line:
                line.remove(word)
        new_lines.append(line)

    # If we need to rewrite new lines in a file:
    with open(f_name, "w") as f:
        for line in new_lines:
            print(' '.join(line), file=f)

    # If we need just display cutted lines:
    # for line in new_lines:
    #     print(' '.join(line))

# word_in_file_deleter("rand_file.txt")

# 2. Текстовый файл содержит записи о телефонах и их владельцах.
# Переписать в другой файл телефоны тех владельцев, фамилии которых начинаются с букв К и С.

def tel_num_sorter(file_name):
    with open(file_name, "r") as f:
        one_note = [line.split() for line in f]
    a_dict = {name: tel for name, tel in one_note if name.startswith("K") or name.startswith("C")}
    with open("sorted_telephones.txt", "w") as f:
        for name in sorted(a_dict):
            print(name, a_dict[name], file=f)

# tel_num_sorter("telephones.txt")

# 3. Получить файл g, в котором текст выровнен по правому краю путем равномерного добавления пробелов.

def right_alignment(file_name):
    with open(file_name, "r") as f:
        a = max([len(line) for line in f])
    with open(file_name, "r") as f, open("file_n.txt", "w") as w:
        for line in f:
            print(line.rjust(a), end="", file=w)

# right_alignment("g.txt")

# 4. Дан текстовый файл со статистикой посещения сайта за неделю. Каждая строка содержит ip адрес,
# время и название дня недели (например, 139.18.150.126 23:12:44 sunday).
# Создайте новый текстовый файл, который бы содержал список ip без повторений из первого файла.
# Для каждого ip укажите количество посещений, наиболее популярный день недели.
# Последней строкой в файле добавьте наиболее популярный отрезок времени в сутках длиной один час в целом для сайта.

def stat_handler(file_name):

    def most_pop_hour(hours):
        """hours is a list of times, func returns the most popular time or list of times"""
        list_of_hours = [int(elem.partition(":")[0]) for elem in hours]
        all_hours = [list_of_hours.count(h) for h in range(24)]
        return [i for i in range(24) if all_hours[i] == max(all_hours)]

    with open(file_name, "r") as f:
        one_note = [line.split() for line in f]
    stat = [{"ip": elem[0], "time": elem[1], "day": elem[2]} for elem in one_note]

    sort_by_ip = {}
    for elem in stat:
        if elem["ip"] not in sort_by_ip.keys():
            sort_by_ip[elem["ip"]] = []
        sort_by_ip[elem.pop("ip")].append(elem["day"])

    week = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
    new_sort_by_ip = {}
    for key, elem in sort_by_ip.items():
        new_sort_by_ip[key] = {day: elem.count(day) for day in week if day in elem}

    sort_by_day = {}
    for key, elem in new_sort_by_ip.items():
        sort_by_day[key] = {}
        for k, v in elem.items():
            if v not in sort_by_day[key].keys():
                sort_by_day[key][v] = []
            sort_by_day[key][v].append(k)

    pop_hour = most_pop_hour([elem["time"] for elem in stat])
    str_pop_hours = ', '.join(["{}:00 - {}:00".format(h, h+1) for h in pop_hour])

    with open("analyzed_stat.txt", "w") as w:
        for key in sort_by_day.keys():
            print("{} {} {}".format(key, len(sort_by_ip[key]),
                                    " ".join(sort_by_day[key][max(sort_by_day[key].keys())])), file=w)
        print("The most popular hour(-s): {}".format(str_pop_hours), file=w)

# stat_handler("stat.txt")