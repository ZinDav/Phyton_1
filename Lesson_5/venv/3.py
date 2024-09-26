# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('salary.txt') as sal_file:
    lines = sal_file.readlines()
    sal_dict = {}
    sm = []
    for line in lines:
        key, value = line.split()
        sal_dict[key] = int(value)
    [sm.append(key) for key, value in sal_dict.items() if value < 20000]
    print('Оклад меньше 20000 имеют: ', *sm)
    print(f'Средняя величина дохода сотрудников: {sum(sal_dict.values()) / len(sal_dict.values())}')
