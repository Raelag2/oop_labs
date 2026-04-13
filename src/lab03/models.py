"""
Производные классы от Product
"""

from base import Product
from datetime import datetime


class FoodProduct(Product):
    """Продукты питания"""
    
    def __init__(self, price, discount, remains, status, product_id, name,
                 expiration_date, storage_temperature):
        super().__init__(price, discount, remains, status, product_id, name)
        self.expiration_date = expiration_date
        self.storage_temperature = storage_temperature
    
    @property
    def expiration_date(self):
        return self._expiration_date
    
    @expiration_date.setter
    def expiration_date(self, date):
        if date < datetime.now():
            raise ValueError("Срок годности не может быть в прошлом")
        self._expiration_date = date
    
    @property
    def storage_temperature(self):
        return self._storage_temperature
    
    @storage_temperature.setter
    def storage_temperature(self, temp):
        if not isinstance(temp, (int, float)):
            raise ValueError("Температура должна быть числом")
        self._storage_temperature = temp
    
    def is_expired(self):
        return datetime.now() > self._expiration_date
    
    def calculate(self):
        return {
            "type": "FoodProduct",
            "name": self._name,
            "final_price": self.get_final_price(),
            "remains": self._remains,
            "expired": self.is_expired(),
            "days_to_expire": (self._expiration_date - datetime.now()).days
        }
    
    def __str__(self):
        return f"{self._name} - {self._price} руб. | Годен до: {self._expiration_date.strftime('%d.%m.%Y')}"


class DigitalProduct(Product):
    """Цифровые товары"""
    
    def __init__(self, price, discount, remains, status, product_id, name,
                 license_key, download_link):
        super().__init__(price, discount, remains, status, product_id, name)
        self.license_key = license_key
        self.download_link = download_link
    
    @property
    def license_key(self):
        return self._license_key
    
    @license_key.setter
    def license_key(self, key):
        if len(key) < 10:
            raise ValueError("Ключ слишком короткий")
        self._license_key = key
    
    @property
    def download_link(self):
        return self._download_link
    
    @download_link.setter
    def download_link(self, link):
        if not link.startswith(('http://', 'https://')):
            raise ValueError("Ссылка должна начинаться с http")
        self._download_link = link
    
    def activate_license(self, user_email):
        if self._remains <= 0:
            raise ValueError("Нет лицензий")
        self._remains -= 1
        return f"Лицензия {self._license_key} активирована для {user_email}"
    
    def calculate(self):
        return {
            "type": "DigitalProduct",
            "name": self._name,
            "final_price": self.get_final_price(),
            "remains": self._remains,
            "available": self._remains > 0
        }
    
    def __str__(self):
        return f"{self._name} - {self._price} руб. | Ключ: {self._license_key[:8]}..."