# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('poem.txt') as poem:
    lines = poem.readlines()
    print('Количество строк: ', len(lines))
    [print(f'{i} строка: {len(line.split())} слов') for i, line in enumerate(lines, 1)]
