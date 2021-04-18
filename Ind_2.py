#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 13. Создать класс Goods (товар). В классе должны быть представлены поля: на именование
# товара, дата оформления, цена товара, количество единиц товара, номер накладной, по
# которой товар поступил на склад. Реализовать методы изменения цены товара, изменения
# количества товара (увеличения и умень шения), вычисления стоимости товара.

from ind2pack import Goods

if __name__ == '__main__':
    a1 = Goods("Товар", "дата", 1000, 10, "накладная")
    a2 = Goods("Товар", "дата", 500, 5, "накладная")

    print(f"{a1}")
    print()
    print(f"{a2}")

    print(f"количество1 < количество2: {a1 < a2}")
    print(f"количество1 > количество2: {a1 > a2}")
    print(f"количество1 != количество2: {a1 != a2}")
    print(f"количество1 == количество2: {a1 == a2}")
    print(f"количество1 >= количество2: {a1 >= a2}")
    print(f"количество1 <= количество2: {a1 <= a2}\n")

    print(f"{a1 + a2}")
    print(f"{a1 - a2}")
    print(f"Старая сумма, новая сумма = {a1 * a2}")
