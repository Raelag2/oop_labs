import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Теперь можно импортировать из lab01
from lab01.model import Product


def main():
    print("=== Лабораторная работа №1. Класс Product ===\n")
    
    # Сценарий 1: Создание объектов и базовые операции (оценка 3)
    print("--- Сценарий 1: Создание и базовая работа ---")
    
    p1 = Product(50000, 10, 5, "в наличии", 1, "Ноутбук")
    p2 = Product(1500, 0, 20, "в наличии", 2, "Мышь")
    p1_copy = Product(50000, 10, 5, "в наличии", 1, "Ноутбук")
    
    print(f"Товар 1: {p1}")
    print(f"Товар 2: {p2}")
    print(f"Сравнение по ID (1 и 1): {p1 == p1_copy}")
    print(f"Сравнение по ID (1 и 2): {p1 == p2}")
    
    print("\nПроверка валидации:")
    try:
        p_bad = Product(-100, 10, 5, "в наличии", 3, "Неверный")
    except ValueError as e:
        print(f"  Ошибка (отрицательная цена): {e}")
    
    try:
        p_bad = Product(1000, 150, 5, "в наличии", 4, "Неверный")
    except ValueError as e:
        print(f"  Ошибка (скидка больше 99): {e}")
    
    try:
        p_bad = Product(1000, 10, -5, "в наличии", 5, "Неверный")
    except ValueError as e:
        print(f"  Ошибка (отрицательный остаток): {e}")
    
    try:
        p_bad = Product(1000, 10, 5, "в наличии", 6, "")
    except ValueError as e:
        print(f"  Ошибка (пустое имя): {e}")
    
    # Сценарий 2: Сеттеры и repr (оценка 4)
    print("\n--- Сценарий 2: Сеттеры и repr ---")
    
    p3 = Product(3000, 5, 10, "в наличии", 7, "Клавиатура")
    print(f"До изменения: {p3}")
    print(f"repr: {repr(p3)}")
    
    p3.price = 3500
    p3.discount = 15
    p3.name = "Механическая клавиатура"
    print(f"После изменения: {p3}")
    
    print("Проверка ограничений сеттеров:")
    try:
        p3.price = -500
    except ValueError as e:
        print(f"  Цена: {e}")
    
    try:
        p3.discount = 200
    except ValueError as e:
        print(f"  Скидка: {e}")
    
    try:
        p3.name = ""
    except ValueError as e:
        print(f"  Имя: {e}")
    
    # Сценарий 3: Бизнес-методы и состояние (оценка 5)
    print("\n--- Сценарий 3: Бизнес-методы и состояние ---")
    
    p4 = Product(10000, 20, 3, "в наличии", 8, "Смартфон")
    print(f"Товар: {p4}")
    print(f"Цена со скидкой: {p4.get_final_price()} руб.")
    print(f"Остаток до продажи: {p4.remains} шт.")
    
    p4.reduce_remains(1)
    print(f"Остаток после продажи: {p4.remains} шт.")
    
    print("\nДемонстрация изменения состояния:")
    print(f"Активен: {p4.active}")
    p4.deactivate()
    print(f"После deactivate(): {p4.active}")
    
    try:
        p4.get_final_price()
    except ValueError as e:
        print(f"  Ошибка при попытке получить цену: {e}")
    
    try:
        p4.reduce_remains(1)
    except ValueError as e:
        print(f"  Ошибка при попытке уменьшить остаток: {e}")
    
    p4.activate()
    print(f"После activate(): {p4.active}")
    print(f"Цена снова доступна: {p4.get_final_price()} руб.")
    
    print("\n--- Завершение ---")
    print("Реализовано: __init__, __str__, __eq__, __repr__")
    print("Сеттеры с валидацией, бизнес-методы, состояние active/inactive")

if __name__ == "__main__":
    main()