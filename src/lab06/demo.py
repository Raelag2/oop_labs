"""demo.py - Демонстрация работы Generics и typing"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab01.model import Product
from lab03.models import FoodProduct, DigitalProduct
from lab06.container import TypedCollection, D, S
from datetime import datetime, timedelta


class Book:
    def __init__(self, title: str, pages: int, rating: float) -> None:
        self.title = title
        self.pages = pages
        self._rating = rating
    def display(self) -> str:
        return f"Книга: {self.title}"
    def score(self) -> float:
        return self._rating


class VideoGame:
    def __init__(self, name: str, score: float) -> None:
        self.name = name
        self._score = score
    def display(self) -> str:
        return f"Игра: {self.name}"
    def score(self) -> float:
        return self._score


def main() -> None:
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №6 - Generics и typing")
    print("=" * 60)
    
    # ========== ЧАСТЬ 1: Generic коллекция (на 3) ==========
    print("\n--- Generic коллекция TypedCollection[T] ---")
    
    coll_str = TypedCollection[str]()
    coll_str.add("Привет")
    coll_str.add("Мир")
    print(f"TypedCollection[str]: {coll_str.get_all()}")
    
    coll_product = TypedCollection[Product]()
    coll_product.add(Product(1000, 10, 5, "available", 1, "Товар"))
    print(f"TypedCollection[Product]: {len(coll_product)} элемент")
    
    # ========== ЧАСТЬ 2: find, filter, map (на 4) ==========
    print("\n--- find, filter, map ---")
    
    products = TypedCollection[Product]()
    for p in [Product(1500, 10, 25, "available", 1, "Ноутбук"),
              Product(500, 0, 100, "available", 2, "Мышь"),
              Product(3000, 5, 3, "available", 3, "Смартфон"),
              FoodProduct(100, 0, 30, "available", 4, "Молоко",
                         datetime.now() + timedelta(days=7), 4)]:
        products.add(p)
    
    found = products.find(lambda p: p.price > 2000)
    print(f"find(цена>2000): {found.name if found else None}")
    
    not_found = products.find(lambda p: p.price > 10000)
    print(f"find(цена>10000): {not_found}")
    
    filtered = products.filter(lambda p: p.price > 1000)
    print(f"filter(цена>1000): {[p.name for p in filtered]}")
    
    names = products.map(lambda p: p.name)
    prices = products.map(lambda p: p.get_final_price())
    print(f"map -> list[str]: {names}")
    print(f"map -> list[float]: {[round(x,2) for x in prices]}")
    
    # ========== ЧАСТЬ 3: Protocol с bound (на 5) ==========
    print("\n--- Protocol с ограничением bound ---")
    
    displayable_coll = TypedCollection[D]()
    displayable_coll.add(Book("Война и мир", 1200, 4.8))
    displayable_coll.add(VideoGame("Cyberpunk", 7.5))
    print("TypedCollection[D] содержит:")
    for item in displayable_coll.get_all():
        print(f"  {item.display()}")
    
    scorable_coll = TypedCollection[S]()
    scorable_coll.add(Book("Преступление и наказание", 600, 4.9))
    scorable_coll.add(VideoGame("The Witcher 3", 9.5))
    print("\nTypedCollection[S] содержит:")
    for item in scorable_coll.get_all():
        print(f"  {item.display()} - рейтинг: {item.score()}")
    
    print("\n" + "=" * 60)
    print("Демонстрация завершена")
    print("=" * 60)


if __name__ == "__main__":
    main()