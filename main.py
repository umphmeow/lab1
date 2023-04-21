dict = {'1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять', '0': 'ноль', '.': 'целых', ',': 'десятых'}

with open('text.txt', 'r') as f_in:
    block_size = 100
    d_array = []
    data = f_in.read(block_size)
    while data:
        digits = [d.replace('77', '', 1) for d in data.split() if d.isdigit() and d.startswith('77') and int(d) != '77']
        d_array.extend(digits)
        while '' in d_array:
            d_array.remove('')
        d_arr_int = list(map(int, d_array))
        data = f_in.read(block_size)

if not d_array:
    print('Не найдено цифр удовлетворяющих заданию или цифр нет')
else:
    max_d = max(d_arr_int)
    min_d = min(d_arr_int)
    answer = (max_d + min_d) / 2
    integer = int(answer)
    fraction = int((answer - integer) * 100)
    int_txt = ' '.join(dict[digit] for digit in str(integer))
    fr_txt = ' '.join(dict[digit] for digit in str(fraction))
    print('Ответ:', int_txt, dict['.'], fr_txt, dict[','])