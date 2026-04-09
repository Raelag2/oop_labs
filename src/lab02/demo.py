import sys
import os

# Добавляем папку src в пути поиска
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Теперь можно импортировать из lab01
from lab01.model import Product
from collection import ProductCatalog

def demo():
    # Создание товаров
    p1 = Product(price=1000, discount=10, remains=50, status="В наличии", product_id=101, name="Ноутбук")
    p2 = Product(price=500, discount=0, remains=0, status="Нет", product_id=102, name="Мышь")
    p3 = Product(price=3000, discount=15, remains=20, status="В наличии", product_id=103, name="Монитор")
    p4 = Product(price=200, discount=5, remains=100, status="В наличии", product_id=104, name="Клавиатура")
    
    catalog = ProductCatalog()
    
    # Добавление
    for p in [p1, p2, p3, p4]:
        catalog.add(p)
    print("Каталог после добавления:")
    print(catalog)
    
    # Проверка ограничений
    try:
        catalog.add(Product(price=1200, discount=5, remains=30, status="В наличии", product_id=101, name="Дубль"))
    except ValueError as e:
        print(f"\nОшибка (дубликат): {e}")
    
    # len и итерация
    print(f"\nВсего товаров: {len(catalog)}")
    print("Перебор:")
    for item in catalog:
        print(f"  {item.name} - {item.price} руб.")
    
    # Поиск
    found = catalog.find_by_id(103)
    print(f"\nПоиск ID 103: {found.name if found else 'не найден'}")
    
    # Индексация
    print(f"\ncatalog[0] = {catalog[0].name}")
    print(f"catalog[2] = {catalog[2].name}")
    
    # Удаление по индексу
    removed = catalog.remove_at(1)
    print(f"\nУдален {removed.name}, осталось {len(catalog)} товаров")
    
    # Сортировка
    print("\nСортировка по цене:")
    catalog.sort_by_price()
    for item in catalog:
        print(f"  {item.name}: {item.price} руб.")
    
    # Логическая операция (фильтрация)
    available = catalog.get_available()
    print(f"\nДоступных товаров: {len(available)}")
    
    # Удаление по объекту
    catalog.remove(p1)
    print(f"\nПосле удаления ноутбука: {len(catalog)} товаров")
    print(catalog)
    
    # Дополнительные сценарии
    print("\n=== Сценарии использования ===")
    
    # Сценарий 1: поиск и работа с результатом
    product = catalog.find_by_id(104)
    if product:
        print(f"1. Найден {product.name}, финальная цена: {product.get_final_price()} руб.")
    
    # Сценарий 2: фильтрация и итерация
    cheap = [p for p in catalog if p.price < 1000]
    print(f"2. Товары дешевле 1000 руб: {len(cheap)} шт.")
    
    # Сценарий 3: создание каталога избранного
    favorite = ProductCatalog()
    for p in catalog:
        if p.discount >= 10:
            favorite.add(p)
    print(f"3. Товары со скидкой ≥10%: {len(favorite)}")
    for item in favorite:
        print(f"   - {item.name} (скидка {item.discount}%)")

if __name__ == "__main__":
    demo()