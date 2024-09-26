
from random import randint


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
with open('sum.txt', 'w') as sum_file:
    rand_list = []
    [rand_list.append(randint(1, 500)) for i in range(randint(2, 20))]
    print(*rand_list, file=sum_file)
    print(f'Сумма чисел: {sum(rand_list)}', file=sum_file)
