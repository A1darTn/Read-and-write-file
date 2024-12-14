dict_1 = {}
with open('1.txt', encoding='utf8') as f:
    count = 0
    for line in f:
        count += 1
    dict_1.setdefault('1.txt', count)

with open('2.txt', encoding='utf8') as f:
    count = 0
    for line in f:
        count += 1
    dict_1.setdefault('2.txt', count)

with open('3.txt', encoding='utf8') as f:
    count = 0
    for line in f:
        count += 1
    dict_1.setdefault('3.txt', count)

sorted_dict = dict(sorted(dict_1.items(), key=lambda item: item[1]))

with open('third.txt', 'w', encoding='utf8') as file:
    for key, value in sorted_dict.items():
        with open(key, 'r', encoding='utf8') as f:
            name = f.read().strip()
        file.write(f'{key}\n{value}\n{name}\n')