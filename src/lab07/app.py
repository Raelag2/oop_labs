from typing import List, Optional, Callable, Any
from lab01.model import Product
from lab05.collection import ExtendedProductCatalog
from lab05.strategies import is_available, has_discount
from lab07.exceptions import DuplicateItemError, ItemNotFoundError


class ShopApp:
    def __init__(self) -> None:
        self._catalog = ExtendedProductCatalog()
    
    def add(self, p: Product) -> None:
        if self._catalog.find_by_id(p.product_id):
            raise DuplicateItemError(f"ID {p.product_id} уже существует")
        self._catalog.add(p)
    
    def remove(self, pid: int) -> None:
        p = self._catalog.find_by_id(pid)
        if not p:
            raise ItemNotFoundError(f"ID {pid} не найден")
        self._catalog.remove(p)
    
    def get_all(self) -> List[Product]:
        return self._catalog.get_all()
    
    def find_by_id(self, pid: int) -> Optional[Product]:
        return self._catalog.find_by_id(pid)
    
    def find_by_name(self, name: str) -> List[Product]:
        return self._catalog.filter(lambda p: name.lower() in p.name.lower())
    
    def filter_price(self, max_price: float) -> List[Product]:
        return self._catalog.filter(lambda p: p.price <= max_price)
    
    def filter_available(self) -> List[Product]:
        return self._catalog.filter(is_available)
    
    def filter_discounted(self) -> List[Product]:
        return self._catalog.filter(has_discount)
    
    def sort_by(self, key: Callable[[Product], Any], rev: bool = False) -> None:
        self._catalog.sort_by(key, rev)
    
    def add_discount(self, pid: int, percent: int) -> None:
        p = self.find_by_id(pid)
        if not p:
            raise ItemNotFoundError(f"ID {pid} не найден")
        p.discount = min(90, p.discount + percent)
    
    def stats(self) -> dict:
        products = self._catalog.get_all()
        if not products:
            return {'count': 0, 'total': 0, 'avg': 0}
        return {'count': len(products), 'total': sum(p.price * p.remains for p in products if p.active),
                'avg': round(sum(p.price for p in products) / len(products), 2)}
    
    def get_catalog(self):
        return self._catalog