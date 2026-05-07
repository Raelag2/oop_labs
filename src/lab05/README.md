## Описание файлов

### strategies.py
Содержит:
- Стратегии сортировки (`by_name`, `by_price`, `by_final_price` и др.)
- Функции-фильтры (`is_available`, `has_discount`, `is_food_product`)
- Функции для map (`product_to_dict`)
- Фабрики функций (`make_price_filter`, `make_remains_filter`)
- Callable-объекты-стратегии (`PriceModifierStrategy`, `ProductInfoFormatter`)

### collection.py
Содержит класс `ExtendedProductCatalog`, наследующий `ProductCatalog` из ЛР-2.
Методы:
- `sort_by(key_func, reverse)` - сортировка с использованием стратегии
- `filter_by(predicate)` - фильтрация с использованием предиката
- `apply(func)` - применение функции ко всем элементам
- `map(transform)` - преобразование коллекции
- `display(formatter)` - отображение с возможностью форматирования

### demo.py
Демонстрирует:
- Сортировку тремя разными стратегиями
- Фильтрацию двумя разными фильтрами
- Применение map для преобразований
- Работу фабрики функций
- Callable-стратегии
- Цепочку операций

## Демонстрация работы

**Скриншот 1**

![01](https://github.com/Raelag2/oop_labs/blob/main/images/lab05/1.jpg)

**Скриншот 2**

![01](https://github.com/Raelag2/oop_labs/blob/main/images/lab05/2.jpg)

**Скриншот 3**

![03](https://github.com/Raelag2/oop_labs/blob/main/images/lab05/3.jpg)

**Скриншот 4**

![04](https://github.com/Raelag2/oop_labs/blob/main/images/lab05/4.jpg)

**Скриншот 5**

![05](https://github.com/Raelag2/oop_labs/blob/main/images/lab05/5.jpg)

**Скриншот 6**

![06](https://github.com/Raelag2/oop_labs/blob/main/images/lab05/6.jpg)

**Скриншот 7**

![07](https://github.com/Raelag2/oop_labs/blob/main/images/lab05/7.jpg)

**Скриншот 8**

![08](https://github.com/Raelag2/oop_labs/blob/main/images/lab05/8.jpg)