from lab01.model import Product

class ProductCatalog:
    def __init__(self):
        self._products = []

    def add(self, product):
        """ добавляет объект в каталог """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product")
        if product in self._products:
            raise ValueError(f"Продукт с ID {product.product_id} уже существует в каталоге")
        
        self._products.append(product)

    def remove(self, product):
        """ удаляет объект из каталога """
        if not isinstance(product, Product):
            raise TypeError("Можно удалять только объекты Product")
        if product not in self._products:
            raise ValueError(f"Продукт с ID {product.product_id} не найден в каталоге")
        
        self._products.remove(product)

    def get_all(self):
        """ возвращает список всех продуктов """
        return self._products.copy()

    def find_by_id(self, target_id):
        """ поиск продукта по идентификатору """
        for product in self._products:
            if product.product_id == target_id:
                return product
        return None
    
    def remove_at(self, position):
        """ удаляет элемент по указанному индексу """
        if not isinstance(position, int):
            raise TypeError("Позиция должна быть целым числом")
        if position < 0 or position >= len(self._products):
            raise IndexError("Индекс находится вне границ каталога")
        
        return self._products.pop(position)

    def sort_by_price(self):
        """ сортирует товары по возрастанию цены """
        self._products.sort()

    def get_available(self):
        """ формирует новый каталог из доступных для заказа товаров """
        result_catalog = ProductCatalog()

        for product in self._products:
            if getattr(product, '_active', False):
                result_catalog.add(product)
                
        return result_catalog
    
    # ===== Магические методы =====

    def __len__(self):
        return len(self._products)
    
    def __iter__(self):
        return iter(self._products)

    def __getitem__(self, key):
        return self._products[key]
    
    def __repr__(self) -> str:
        return f"ProductCatalog(products={self._products!r})"
    
    def __str__(self):
        if not self._products:
            return "В каталоге нет товаров."
        
        lines = [f"Всего товаров в каталоге: {len(self)}"]
        for idx, product in enumerate(self._products, 1):
            lines.append(f"  {idx}. {product}")
        
        return "\n".join(lines)