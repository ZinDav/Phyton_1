# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

num_translate = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
    'Ten': 'Десять'}

with open('numbers.txt') as numbers, open('numbers_rus.txt', 'w') as numbers1:
    for num in numbers.readlines():
        key, value = num.split(' - ')
        print(f'{num_translate.get(key)} - {value}', file=numbers1)
