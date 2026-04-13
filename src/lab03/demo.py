"""
Демонстрация работы иерархии классов
"""

from datetime import datetime, timedelta
from base import Product
from models import FoodProduct, DigitalProduct


def main():
    print("=" * 50)
    print("1. СОЗДАНИЕ ОБЪЕКТОВ")
    print("=" * 50)
    
    regular = Product(
        price=1000,
        discount=10,
        remains=50,
        status="available",
        product_id=1,
        name="Обычный товар"
    )
    
    food = FoodProduct(
        price=500,
        discount=5,
        remains=20,
        status="fresh",
        product_id=2,
        name="Молоко",
        expiration_date=datetime.now() + timedelta(days=7),
        storage_temperature=4
    )
    
    digital = DigitalProduct(
        price=2999,
        discount=15,
        remains=100,
        status="active",
        product_id=3,
        name="Лицензия Windows",
        license_key="WIN11-X7K2N-8M4P9",
        download_link="https://microsoft.com/download"
    )
    
    print(regular)
    print(food)
    print(digital)
    
    print("\n" + "=" * 50)
    print("2. МЕТОДЫ БАЗОВОГО КЛАССА")
    print("=" * 50)
    
    print(f"Цена со скидкой (молоко): {food.get_final_price()} руб.")
    print(f"Цена со скидкой (лицензия): {digital.get_final_price()} руб.")
    
    print("\n" + "=" * 50)
    print("3. НОВЫЕ МЕТОДЫ ДОЧЕРНИХ КЛАССОВ")
    print("=" * 50)
    
    print(f"Молоко просрочено? {food.is_expired()}")
    print(digital.activate_license("user@example.com"))
    print(f"Осталось лицензий: {digital.remains}")
    
    print("\n" + "=" * 50)
    print("4. ПОЛИМОРФИЗМ (разное поведение)")
    print("=" * 50)
    
    products = [regular, food, digital]
    
    for p in products:
        print(f"\n{p.name}:")
        print(f"  Цена со скидкой: {p.get_final_price()} руб.")  # Этот метод есть у всех
        
        if isinstance(p, FoodProduct):
            print(f"  Тип: Продукт питания")
            print(f"  Просрочен: {p.is_expired()}")
        elif isinstance(p, DigitalProduct):
            print(f"  Тип: Цифровой товар")
            print(f"  Лицензий осталось: {p.remains}")
        else:
            print(f"  Тип: Обычный товар")
            print(f"  Остаток: {p.remains} шт.")
    
    print("\n" + "=" * 50)
    print("5. ПРОВЕРКА ТИПОВ (isinstance)")
    print("=" * 50)
    
    for p in products:
        print(f"\n{p.name}:")
        print(f"  Это Product? {isinstance(p, Product)}")
        print(f"  Это FoodProduct? {isinstance(p, FoodProduct)}")
        print(f"  Это DigitalProduct? {isinstance(p, DigitalProduct)}")
    
    print("\n" + "=" * 50)
    print("6. КОЛЛЕКЦИЯ РАЗНЫХ ТИПОВ")
    print("=" * 50)
    
    more_products = [
        FoodProduct(
            price=150, discount=0, remains=100, status="fresh",
            product_id=4, name="Хлеб",
            expiration_date=datetime.now() + timedelta(days=3),
            storage_temperature=20
        ),
        DigitalProduct(
            price=499, discount=10, remains=0, status="active",
            product_id=5, name="Антивирус",
            license_key="KAS-2024-XYZ-789",
            download_link="https://kaspersky.com"
        )
    ]
    
    all_products = products + more_products
    
    print("\nВсе товары в коллекции:")
    for i, p in enumerate(all_products, 1):
        print(f"{i}. {p}")
    
    print("\n" + "=" * 50)
    print("7. ФИЛЬТРАЦИЯ ПО ТИПУ")
    print("=" * 50)
    
    digital_items = [p for p in all_products if isinstance(p, DigitalProduct)]
    print(f"\nЦифровые товары ({len(digital_items)} шт.):")
    for p in digital_items:
        print(f"  - {p.name} (остаток: {p.remains})")
    
    food_items = [p for p in all_products if isinstance(p, FoodProduct)]
    print(f"\nПродукты питания ({len(food_items)} шт.):")
    for p in food_items:
        expired = "ПРОСРОЧЕН" if p.is_expired() else "свежий"
        print(f"  - {p.name} ({expired})")
    
    print("\n" + "=" * 50)
    print("8. ДЕАКТИВАЦИЯ ТОВАРА")
    print("=" * 50)
    
    print(f"\nДо деактивации: {all_products[0].name} - активен: {all_products[0].active}")
    all_products[0].deactivate()
    print(f"После деактивации: {all_products[0].name} - активен: {all_products[0].active}")
    
    print("\nАктивные товары:")
    active = [p for p in all_products if p.active]
    for p in active:
        print(f"  - {p.name}")


if __name__ == "__main__":
    main()