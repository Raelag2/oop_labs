
### Базовый класс Product
- Атрибуты: name, price, discount, remains, status, product_id, active
- Методы: get_final_price(), activate(), deactivate(), reduce_remains()

### Производный класс FoodProduct
**Новые атрибуты:**
- expiration_date - срок годности
- storage_temperature - температура хранения

**Новые методы:**
- is_expired() - проверка просрочки

**Переопределенные методы:**
- __str__() - добавлена информация о сроке годности

### Производный класс DigitalProduct
**Новые атрибуты:**
- license_key - лицензионный ключ
- download_link - ссылка для скачивания

**Новые методы:**
- activate_license() - активация лицензии

**Переопределенные методы:**
- __str__() - добавлена информация о лицензии

## Демонстрация работы

**Скриншот 1**

![01](https://github.com/Raelag2/oop_labs/blob/main/images/lab03/1.png)

**Скриншот 2**

![01](https://github.com/Raelag2/oop_labs/blob/main/images/lab03/2.png)

**Скриншот 3**

![01](https://github.com/Raelag2/oop_labs/blob/main/images/lab03/3.png)

**Скриншот 4**

![01](https://github.com/Raelag2/oop_labs/blob/main/images/lab03/4.png)