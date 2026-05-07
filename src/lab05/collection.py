from typing import Callable, Any, List, Optional
from lab01.model import Product
from lab02.collection import ProductCatalog

class ExtendedProductCatalog(ProductCatalog):
    """Расширенный каталог с поддержкой функциональных операций"""
    
    def __init__(self, products: Optional[List[Product]] = None):
        super().__init__()
        if products:
            for product in products:
                self.add(product)
    
    def sort_by(self, key_func: Callable[[Product], Any], reverse: bool = False) -> 'ExtendedProductCatalog':
        """Сортировка с использованием стратегии"""
        self._products.sort(key=key_func, reverse=reverse)
        return self
    
    def filter_by(self, predicate: Callable[[Product], bool]) -> 'ExtendedProductCatalog':
        """Фильтрация с использованием предиката"""
        filtered = list(filter(predicate, self._products))
        return ExtendedProductCatalog(filtered)
    
    def apply(self, func: Callable[[Product], Any]) -> 'ExtendedProductCatalog':
        """Применение функции ко всем элементам"""
        for product in self._products:
            func(product)
        return self
    
    def map(self, transform: Callable[[Product], Any]) -> List[Any]:
        """Преобразование коллекции"""
        return list(map(transform, self._products))
    
    def get_all(self) -> List[Product]:
        """Получение всех продуктов"""
        return self._products.copy()
    
    def display(self, formatter: Optional[Callable[[Product], str]] = None) -> None:
        """Отображение каталога"""
        if not self._products:
            print("Каталог пуст")
            return
        
        for i, product in enumerate(self._products, 1):
            if formatter:
                print(f"{i}. {formatter(product)}")
            else:
                print(f"{i}. {product}")




