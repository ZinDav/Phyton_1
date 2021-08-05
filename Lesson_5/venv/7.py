
import json


# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
# со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

with open('firms.txt') as f_file:
    f_earn = dict()
    f_loss = dict()
    average_dict = dict()
    result = list()
    for line in f_file.readlines():
        key, _, val_1, val_2 = line.split()
        value = int(val_1) - int(val_2)
        if value > 0:
            f_earn[key] = value
        else:
            f_loss[key] = value

    result.append(f_earn)
    result.append(f_loss)
    average_dict['average_profit'] = sum(f_earn.values()) / len(f_earn.values())
    result.append(average_dict)

with open('firm_res.json', 'w') as js_f:
    json.dump(result, js_f)
