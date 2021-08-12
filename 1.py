# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        st = str()
        for ls in self.my_list:
            for num in ls:
                st += f'{num:>10}'
            st += '\n'
        return st

    def __add__(self, other):
        result = []
        ch = '+'
        if len(self.my_list) != len(other.my_list):
            ch = input('Несовпадающее количество элементов списка. Продолжить? (+/-)')
        if ch == '+':
            if len(self.my_list) <= len(other.my_list):
                length = len(self.my_list)
            else:
                length = len(other.my_list)
            for i in range(length):
                not_res = []
                for m, l in zip(self.my_list[i], other.my_list[i]):
                    not_res.append(m + l)
                result.append(not_res)
            return Matrix(result)


matrix_1 = Matrix([[1, 2, 3, 4, 5], [1, 2, 3], [1, 2, 3]])
print(f'Matrix: \n{matrix_1}')
matrix_2 = Matrix([[1, 2, 3], [1, 2, 3, 4, 5]])
print(f'Result: \n{matrix_1.__add__(matrix_2)}')
