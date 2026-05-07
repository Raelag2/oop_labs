import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab04.models import Product, ServiceItem, Printable, Comparable
from lab02.collection import ProductCatalog

def print_all(items: list[Printable]):
    for item in items:
        print(item.to_string())

def main():
    p1 = Product(price=1000, discount=10, remains=50, status="новый", product_id=1, name="Ноутбук")
    p2 = Product(price=500, discount=5, remains=100, status="новый", product_id=2, name="Мышь")
    p3 = Product(price=2000, discount=20, remains=25, status="новый", product_id=3, name="Клавиатура")
    p4 = Product(price=1500, discount=0, remains=30, status="новый", product_id=4, name="Монитор")
    
    s1 = ServiceItem(service_id=101, name="Настройка ПК", price=2000)
    s2 = ServiceItem(service_id=102, name="Антивирус", price=800)
    
    print("=== Демонстрация 1: Разная реализация to_string() ===")
    print(p1.to_string())
    print(s1.to_string())
    
    print("\n=== Демонстрация 2: Разная реализация compare_to() ===")
    print(f"Ноутбук vs Мышь: {p1.compare_to(p2)}")
    print(f"Настройка ПК vs Антивирус: {s1.compare_to(s2)}")
    
    print("\n=== Демонстрация 3: Универсальная функция print_all() ===")
    mixed_list: list[Printable] = [p1, s1, p2, s2, p3]
    print_all(mixed_list)
    
    print("\n=== Демонстрация 4: Проверка isinstance ===")
    print(f"Product реализует Printable: {isinstance(p1, Printable)}")
    print(f"Product реализует Comparable: {isinstance(p1, Comparable)}")
    print(f"ServiceItem реализует Printable: {isinstance(s1, Printable)}")
    print(f"ServiceItem реализует Comparable: {isinstance(s1, Comparable)}")
    
    print("\n=== Демонстрация 5: Интеграция с ProductCatalog ===")
    catalog = ProductCatalog()
    catalog.add(p1)
    catalog.add(p2)
    catalog.add(p3)
    catalog.add(p4)
    
    print("Исходный каталог:")
    print(catalog)
    
    printable_items = [item for item in catalog.get_all() if isinstance(item, Printable)]
    print("\nТовары с интерфейсом Printable:")
    print_all(printable_items)
    
    comparable_items = [item for item in catalog.get_all() if isinstance(item, Comparable)]
    print("\nТовары до сортировки:")
    for p in comparable_items:
        print(f"  {p.name}: {p.price} руб.")
    
    n = len(comparable_items)
    for i in range(n):
        for j in range(i + 1, n):
            if comparable_items[i].compare_to(comparable_items[j]) > 0:
                comparable_items[i], comparable_items[j] = comparable_items[j], comparable_items[i]
    
    print("\nТовары после сортировки (по цене):")
    for p in comparable_items:
        print(f"  {p.name}: {p.price} руб.")

if __name__ == "__main__":
    main()


