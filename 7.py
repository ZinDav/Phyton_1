# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return f'{self.r + other.r} + {self.i + other.i}i'

    def __mul__(self, other):
        return f'{self.r * other.r - self.i * other.i} + {self.r * other.i + other.r * self.i}i'


complex_number1 = ComplexNumber(5, 2)
complex_number2 = ComplexNumber(3, 7)
print(f'result: {complex_number1 + complex_number2}')
print(f'result: {complex_number1 * complex_number2}')
print(complex(5, 2) + complex(3, 7))
print(complex(5, 2) * complex(3, 7))
