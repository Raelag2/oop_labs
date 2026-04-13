from validate import validate_name, validate_price, validate_discount, validate_remains

class Product:
    currency: str = "RUB"
    _product_id: int
    _name: str
    _price: float
    _discount: int
    _remains: int
    _status: str
    _active: bool

    def __init__(self, price, discount, remains, status, product_id, name):
        self.price = price
        self.discount = discount
        self.remains = remains
        self.status = status
        self._product_id = product_id
        self.name = name
        self._active = True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        validate_name(name)
        self._name = name

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        validate_price(price)
        self._price = price

    @property
    def discount(self):
        return self._discount
    
    @discount.setter
    def discount(self, discount):
        validate_discount(discount)
        self._discount = discount

    @discount.deleter
    def discount(self):
        self._discount = 0

    @property
    def remains(self):
        return self._remains

    @remains.setter
    def remains(self, remains):
        validate_remains(remains)
        self._remains = remains

    @property
    def product_id(self):
        return self._product_id
    
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if not isinstance(status, str):
            raise ValueError("status должен быть str")
        self._status = status

    @property
    def active(self):
        return self._active

    def get_final_price(self) -> float:
        if not self._active:
            raise ValueError("Товар снят с продажи")
        return round(self._price * (100 - self._discount) / 100, 2)
    
    def activate(self) -> None:
        self._active = True

    def deactivate(self) -> None:
        self._active = False

    def reduce_remains(self, amount) -> None:
        if not self._active:
            raise ValueError("Товар снят с продажи")
        if self._remains < amount:
            raise ValueError(f"На складе всего {self._remains} шт., а вы хотите {amount}")
        if amount <= 0:
            raise ValueError("Количество должно быть больше 0")
        self._remains -= amount
    
    def __str__(self) -> str:
        return f"{self._name} - {self._price} руб. ({self._remains} шт.)"
    
    def __repr__(self) -> str:
        return f"Product(name={self._name!r}, price={self._price}, remains={self._remains}, discount={self._discount}, product_id={self._product_id})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Product):
            return False
        return self._product_id == other._product_id
    
    def __lt__(self, other):
        """ для сортировки по цене """
        if not isinstance(other, Product):
            return NotImplemented
        return self._price < other._price