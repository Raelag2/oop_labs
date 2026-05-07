"""strategies.py - Функции стратегий для работы с продуктами"""

from typing import Callable, Any
from lab01.model import Product
from lab03.models import FoodProduct, DigitalProduct
from datetime import datetime

def by_name(product: Product) -> str:
    """Стратегия сортировки по названию"""
    return product.name

def by_price(product: Product) -> float:
    """Стратегия сортировки по цене"""
    return product.price

def by_final_price(product: Product) -> float:
    """Стратегия сортировки по конечной цене (со скидкой)"""
    if product.active:
        return product.get_final_price()
    return product.price

def by_remains(product: Product) -> int:
    """Стратегия сортировки по остатку"""
    return product.remains

def by_discount(product: Product) -> int:
    """Стратегия сортировки по скидке"""
    return product.discount

def is_available(product: Product) -> bool:
    """Фильтр: товар активен и есть в наличии"""
    return product.active and product.remains > 0

def has_discount(product: Product) -> bool:
    """Фильтр: товар со скидкой"""
    return product.discount > 0

def is_food_product(product: Product) -> bool:
    """Фильтр: продукты питания"""
    return isinstance(product, FoodProduct)

def product_to_dict(product: Product) -> dict:
    """Преобразование продукта в словарь"""
    return {
        'id': product.product_id,
        'name': product.name,
        'price': product.price,
        'final_price': product.get_final_price() if product.active else product.price,
        'remains': product.remains
    }

def make_price_filter(max_price: float) -> Callable[[Product], bool]:
    """Фабрика фильтров по максимальной цене"""
    def filter_by_price(product: Product) -> bool:
        return product.price <= max_price
    return filter_by_price

def make_remains_filter(min_remains: int) -> Callable[[Product], bool]:
    """Фабрика фильтров по минимальному остатку"""
    def filter_by_remains(product: Product) -> bool:
        return product.remains >= min_remains
    return filter_by_remains

class PriceModifierStrategy:
    """Стратегия изменения цены"""
    
    def __init__(self, percent: float, increase: bool = True):
        self.percent = percent
        self.increase = increase
    
    def __call__(self, product: Product) -> Product:
        if product.active:
            if self.increase:
                product._price = product.price * (1 + self.percent / 100)
            else:
                product._price = product.price * (1 - self.percent / 100)
        return product

class ProductInfoFormatter:
    """Стратегия форматирования информации о товаре"""
    
    def __init__(self, format_type: str = 'short'):
        self.format_type = format_type
    
    def __call__(self, product: Product) -> str:
        if self.format_type == 'short':
            if product.active:
                return f"{product.name} - {product.get_final_price():.2f} руб."
            return f"{product.name} - {product.price:.2f} руб. (снят с продажи)"
        elif self.format_type == 'detailed':
            if product.active:
                return f"{product.name}: цена {product.price:.2f} руб., со скидкой {product.get_final_price():.2f} руб., остаток {product.remains} шт."
            return f"{product.name}: цена {product.price:.2f} руб., остаток {product.remains} шт. (НЕАКТИВЕН)"
        return str(product)




