
from abc import ABC, abstractmethod


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании
# и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
# например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


class Warehouse:
    wh = dict()

    @classmethod
    def receive_e(cls, eq):
        cls.wh.setdefault(eq.name)
        dict_1 = vars(eq).copy()
        dict_1.pop('name')
        dict_1.pop('_OfficeEquipment__amount')
        amount_1 = eq.get_amount
        if cls.wh[eq.name] is None:
            dict_1['amount'] = amount_1
            cls.wh[eq.name] = dict_1
        elif type(cls.wh[eq.name]) is list:
            indent = 0
            for i in range(len(cls.wh[eq.name])):
                dict_2 = cls.wh[eq.name][i].copy()
                amount_2 = dict_2.pop('amount')
                if list(dict_1.values()) == list(dict_2.values()):
                    dict_1['amount'] = amount_1 + amount_2
                    cls.wh[eq.name][i] = dict_1
                    indent += 1
            if indent == 0:
                dict_1['amount'] = amount_1
                cls.wh[eq.name].append(dict_1)
        else:
            dict_2 = cls.wh[eq.name].copy()
            amount_2 = dict_2.pop('amount')
            if list(dict_1.values()) == list(dict_2.values()):
                dict_1['amount'] = amount_1 + amount_2
                cls.wh[eq.name] = dict_1
            else:
                dict_1['amount'] = amount_1
                dict_2['amount'] = amount_2
                cls.wh[eq.name] = [dict_1, dict_2]

    @classmethod
    def get_e(cls, key, value, department):
        amount_g = value.pop('amount')
        if type(cls.wh[key]) is list:
            count = 0
            for i in range(len(cls.wh[key])):
                d = cls.wh[key][i].copy()
                amount_i = d.pop('amount')
                if value == d:
                    if amount_i == amount_g:
                        cls.wh[key].pop(i)
                        count += 1
                        print(f'{amount_g} equipment was transferred to the {department}')
                    elif amount_i > amount_g:
                        amount_i -= amount_g
                        cls.wh[key][i]['amount'] = amount_i
                        count += 1
                        print(f'{amount_g} equipment was transferred to the {department}')
                    else:
                        pass
            if count == 0:
                print('The equipment not found')
        else:
            d = cls.wh[key].copy()
            amount_i = d.pop('amount')
            if value == d:
                if int(amount_i) == int(amount_g):
                    cls.wh.pop(key)
                    print(f'{amount_g} equipment was transferred to the {department}')
                elif amount_i > amount_g:
                    amount_i -= amount_g
                    cls.wh[key]['amount'] = amount_i
                    print(f'{amount_g} equipment was transferred to the {department}')
            else:
                print('The equipment not found')


class OfficeEquipment(ABC):
    def __init__(self, name, firm_model, amount, cost):
        self.name = name
        self.firm_model = firm_model
        self.__amount = amount
        self.cost = cost

    @staticmethod
    def validation_int(x):
        if type(x) is not int:
            print('Incorrect data')
        else:
            return x

    @property
    def get_amount(self):
        return self.validation_int(self.__amount)

    @abstractmethod
    def paint_consumption(self):
        return 'This is paint consumption'


class Printer(OfficeEquipment):
    def __init__(self, name, firm_model, amount, cost, paint_volume):
        super().__init__(name, firm_model, amount, cost)
        self.paint_volume = paint_volume
        Warehouse.receive_e(self)

    def paint_consumption(self):
        return self.validation_int(self.paint_volume) * 2 - 7


class Scanner(OfficeEquipment):
    def __init__(self, name, firm_model, amount, cost):
        super().__init__(name, firm_model, amount, cost)
        Warehouse.receive_e(self)

    def paint_consumption(self):
        return f'{self.name} do not need paint'


class Xerox(OfficeEquipment):
    def __init__(self, name, firm_model, amount, cost, paint_volume):
        super().__init__(name, firm_model, amount, cost)
        self.paint_volume = paint_volume
        Warehouse.receive_e(self)

    def paint_consumption(self):
        return self.validation_int(self.paint_volume) / 6 + 3


printer_1 = Printer('Printer', 'HP LaserJet Pro M15w', 5, 10000, 8)
print(Warehouse.wh)
printer_2 = Printer('Printer', 'Brother HL-L2340DWR', 3, 15000, 14)
print(Warehouse.wh)
printer_3 = Printer('Printer', 'HP LaserJet Pro M15w', 10, 10000, 8)
print(Warehouse.wh)
printer_4 = Printer('Printer', 'Brother HL-L2340DWR', 1, 15000, 14)
print(Warehouse.wh)
Warehouse.get_e('Printer', {'firm_model': 'HP LaserJet Pro M15w', 'cost': 10000, 'paint_volume': 8, 'amount': 3},
                'Accounting')
print(Warehouse.wh)
print(printer_4.paint_consumption())
