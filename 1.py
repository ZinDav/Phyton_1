# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    str_date = input('Input date: ')

    @classmethod
    def int_date(cls):
        try:
            list_date = list()
            for ld in cls.str_date.split('-'):
                list_date.append(int(ld))
            return list_date
        except ValueError:
            print('Input date is not valid')

    @staticmethod
    def validation(d_list):
        try:
            d, m, y = d_list
            thd_m = [1, 3, 5, 7, 8, 10]
            if y % 4 == 0 and m == 2 and d > 29 or d < 1:
                print('There is no such day')
            elif m == 2 and d > 28 or d < 1:
                print('There is no such day')
            elif m in thd_m and d > 31 or d < 1:
                print('There is no such day')
            elif m not in thd_m and d > 30 or d < 1:
                print('There is no such day')
            if m > 12 or m < 1:
                print('There is no such month')
        except TypeError:
            pass
        except ValueError:
            print('Input date is not valid')


print(Date().int_date())
Date().validation(Date().int_date())
