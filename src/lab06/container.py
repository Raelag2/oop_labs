"""Generic-коллекция с поддержкой протоколов и аннотаций типов"""

from typing import TypeVar, Generic, Callable, Optional, List, Protocol
from lab01.model import Product
from lab03.models import FoodProduct, DigitalProduct


T = TypeVar('T')
R = TypeVar('R')


class Displayable(Protocol):
    """Протокол для объектов, которые можно отобразить"""
    def display(self) -> str:
        ...


class Scorable(Protocol):
    """Протокол для объектов, которые имеют оценку/рейтинг"""
    def score(self) -> float:
        ...


D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)


class TypedCollection(Generic[T]):
    """версия коллекции с типизацией"""
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def add(self, item: T) -> None:
        """Добавление элемента"""
        self._items.append(item)
    
    def remove(self, item: T) -> None:
        """Удаление элемента"""
        if item not in self._items:
            raise ValueError(f"Элемент не найден")
        self._items.remove(item)
    
    def get_all(self) -> List[T]:
        """Получение всех элементов"""
        return self._items.copy()
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """Поиск первого подходящего элемента"""
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        """Фильтрация элементов по условию"""
        return [item for item in self._items if predicate(item)]
    
    def map(self, transform: Callable[[T], R]) -> List[R]:
        """Преобразование элементов с изменением типа"""
        return [transform(item) for item in self._items]
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __getitem__(self, index: int) -> T:
        return self._items[index]
    
    def __iter__(self):
        return iter(self._items)