dict = {'1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять', '0': 'ноль', '.': 'целых', ',': 'десятых'}

with open('text.txt', 'r') as f_in:
    block_size = 100
    d_array = []
    buffer = ''
    while True:
        data = f_in.read(block_size)
        if not data:
            break
        buffer += data
        digits = [d.replace('77', '', 1) for d in buffer.split() if d.isdigit() and d.startswith('77') and int(d) != '77']
        d_array.extend(digits)
        while '' in d_array:
            d_array.remove('')
        d_arr_int = list(map(int, d_array))
        buffer = buffer[buffer.rfind(digits[-1]) + len(digits[-1]):]

    if not d_array:
        print('Не найдено цифр удовлетворяющих заданию или цифр нет вообще')
    else:
        print('Массив чисел:', d_arr_int)
        max_d = max(d_arr_int)
        min_d = min(d_arr_int)
        print('Максимальное число:', max_d)
        print('Минимальное число:', min_d)
        answer = (max_d + min_d) / 2
        print('Среднее арифметическое:', answer)
        answer_txt = ''
        for digit in str(answer):
            answer_txt += ' ' + dict[digit]
        print('Ответ:', answer_txt, dict[','])
