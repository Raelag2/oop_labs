import sys
import os
from abc import ABC, abstractmethod

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab01.model import Product as BaseProduct

class Printable(ABC):
    @abstractmethod
    def to_string(self) -> str:
        pass

class Comparable(ABC):
    @abstractmethod
    def compare_to(self, other) -> int:
        pass

class Product(BaseProduct, Printable, Comparable):
    def to_string(self) -> str:
        return f"Товар: {self.name} | Цена: {self.price} | Итого: {self.get_final_price()} | Остаток: {self.remains}"
    
    def compare_to(self, other) -> int:
        if not isinstance(other, Product):
            raise ValueError("Нельзя сравнить с объектом другого типа")
        if self.price < other.price:
            return -1
        elif self.price > other.price:
            return 1
        return 0

class ServiceItem(Printable, Comparable):
    def __init__(self, service_id: int, name: str, price: float):
        self._service_id = service_id
        self._name = name
        self._price = price
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    def to_string(self) -> str:
        return f"Услуга: {self.name} | ID: {self._service_id} | Цена: {self.price}"
    
    def compare_to(self, other) -> int:
        if not isinstance(other, ServiceItem):
            raise ValueError("Нельзя сравнить с объектом другого типа")
        if self.price < other.price:
            return -1
        elif self.price > other.price:
            return 1
        return 0


import sys
import os
from abc import ABC, abstractmethod

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab01.model import Product as BaseProduct

class Printable(ABC):
    @abstractmethod
    def to_string(self) -> str:
        pass

class Comparable(ABC):
    @abstractmethod
    def compare_to(self, other) -> int:
        pass

class Product(BaseProduct, Printable, Comparable):
    def to_string(self) -> str:
        return f"Товар: {self.name} | Цена: {self.price} | Итого: {self.get_final_price()} | Остаток: {self.remains}"
    
    def compare_to(self, other) -> int:
        if not isinstance(other, Product):
            raise ValueError("Нельзя сравнить с объектом другого типа")
        if self.price < other.price:
            return -1
        elif self.price > other.price:
            return 1
        return 0

class ServiceItem(Printable, Comparable):
    def __init__(self, service_id: int, name: str, price: float):
        self._service_id = service_id
        self._name = name
        self._price = price
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    def to_string(self) -> str:
        return f"Услуга: {self.name} | ID: {self._service_id} | Цена: {self.price}"
    
    def compare_to(self, other) -> int:
        if not isinstance(other, ServiceItem):
            raise ValueError("Нельзя сравнить с объектом другого типа")
        if self.price < other.price:
            return -1
        elif self.price > other.price:
            return 1
        return 0


import sys
import os
from abc import ABC, abstractmethod

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab01.model import Product as BaseProduct

class Printable(ABC):
    @abstractmethod
    def to_string(self) -> str:
        pass

class Comparable(ABC):
    @abstractmethod
    def compare_to(self, other) -> int:
        pass

class Product(BaseProduct, Printable, Comparable):
    def to_string(self) -> str:
        return f"Товар: {self.name} | Цена: {self.price} | Итого: {self.get_final_price()} | Остаток: {self.remains}"
    
    def compare_to(self, other) -> int:
        if not isinstance(other, Product):
            raise ValueError("Нельзя сравнить с объектом другого типа")
        if self.price < other.price:
            return -1
        elif self.price > other.price:
            return 1
        return 0

class ServiceItem(Printable, Comparable):
    def __init__(self, service_id: int, name: str, price: float):
        self._service_id = service_id
        self._name = name
        self._price = price
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price
    
    def to_string(self) -> str:
        return f"Услуга: {self.name} | ID: {self._service_id} | Цена: {self.price}"
    
    def compare_to(self, other) -> int:
        if not isinstance(other, ServiceItem):
            raise ValueError("Нельзя сравнить с объектом другого типа")
        if self.price < other.price:
            return -1
        elif self.price > other.price:
            return 1
        return 0




