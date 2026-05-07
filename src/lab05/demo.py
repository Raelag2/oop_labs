"""demo.py - Демонстрация работы лабораторной работы №5"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab01.model import Product
from lab03.models import FoodProduct, DigitalProduct
from lab05.collection import ExtendedProductCatalog
from lab05.strategies import *
from datetime import datetime, timedelta

def create_test_catalog() -> ExtendedProductCatalog:
    """Создание тестового каталога с продуктами"""
    products = [
        Product(1500, 10, 25, "available", 1, "Ноутбук"),
        Product(500, 0, 100, "available", 2, "Мышь"),
        Product(3000, 5, 3, "available", 3, "Смартфон"),
        Product(800, 15, 0, "out_of_stock", 4, "Клавиатура"),
        FoodProduct(100, 0, 30, "available", 5, "Молоко",
                   datetime.now() + timedelta(days=7), 4),
        FoodProduct(250, 20, 5, "available", 6, "Сыр",
                   datetime.now() + timedelta(days=30), 6),
        DigitalProduct(5000, 10, 100, "available", 7, "Лицензия Windows",
                      "WIN-1234567890", "https://download.example.com"),
    ]
    
    products[3].deactivate()
    
    return ExtendedProductCatalog(products)

def safe_final_price(product: Product) -> float:
    """Безопасное получение конечной цены"""
    if product.active:
        return product.get_final_price()
    return product.price

def main():
    catalog = create_test_catalog()
    
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №5 - Функции высшего порядка")
    print("=" * 60)
    
    print("\n--- Исходный каталог ---")
    catalog.display()
    
    print("\n--- Сортировка по названию (strategy: by_name) ---")
    catalog.sort_by(by_name).display(lambda p: f"{p.name} | {p.price} руб.")
    
    print("\n--- Сортировка по конечной цене (strategy: by_final_price, reverse) ---")
    catalog.sort_by(by_final_price, True).display(lambda p: f"{p.name} | {safe_final_price(p)} руб.")
    
    print("\n--- Фильтрация доступных товаров (is_available) ---")
    available = catalog.filter_by(is_available)
    available.display(lambda p: f"{p.name} | остаток: {p.remains}")
    
    print("\n--- Фильтрация товаров со скидкой (has_discount) ---")
    discounted = catalog.filter_by(has_discount)
    discounted.display(lambda p: f"{p.name} | скидка: {p.discount}%")
    
    print("\n--- Применение map: преобразование в словари ---")
    products_dicts = catalog.map(product_to_dict)
    for i, p_dict in enumerate(products_dicts[:3], 1):
        print(f"  {i}. {p_dict}")
    
    print("\n--- Применение map: извлечение названий через lambda ---")
    names = catalog.map(lambda p: p.name)
    print(f"  Названия: {', '.join(names)}")
    
    print("\n--- Фабрика функций: фильтр по цене <= 1000 ---")
    price_filter = make_price_filter(1000)
    cheap = catalog.filter_by(price_filter)
    cheap.display(lambda p: f"{p.name} | {p.price} руб.")
    
    print("\n--- Callable-стратегия: изменение цен (увеличение на 10%) ---")
    test_catalog = ExtendedProductCatalog(catalog.get_all()[:2])
    print("  До применения:")
    test_catalog.display(lambda p: f"{p.name}: {p.price} руб.")
    
    test_catalog.apply(PriceModifierStrategy(10, increase=True))
    print("  После применения:")
    test_catalog.display(lambda p: f"{p.name}: {p.price} руб.")
    
    print("\n--- Callable-стратегия: форматирование в разных стилях ---")
    formatter_detailed = ProductInfoFormatter('detailed')
    formatter_short = ProductInfoFormatter('short')
    
    sample = catalog.get_all()[0]
    print(f"  Краткий формат: {formatter_short(sample)}")
    print(f"  Детальный формат: {formatter_detailed(sample)}")
    
    print("\n--- Цепочка операций: filter -> sort -> apply ---")
    result = (catalog
        .filter_by(is_available)
        .sort_by(by_price)
        .apply(PriceModifierStrategy(5, increase=False)))
    
    print("  Доступные товары с уценкой 5%:")
    result.display(lambda p: f"{p.name} | новая цена: {p.price:.2f} руб.")
    
    print("\n=" * 10)
    print("Демонстрация завершена")

if __name__ == "__main__":
    main()



