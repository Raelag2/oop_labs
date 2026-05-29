from lab01.model import Product
from lab03.models import FoodProduct, DigitalProduct
from lab05.strategies import by_name, by_price, by_final_price, by_remains
from lab07.app import ShopApp
from lab07.exceptions import DuplicateItemError, ItemNotFoundError
from datetime import datetime, timedelta


class CLI:
    def __init__(self) -> None:
        self.app = ShopApp()
    
    def _int(self, prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Ошибка: введите число")
    
    def _float(self, prompt: str) -> float:
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Ошибка: введите число")
    
    def _confirm(self, prompt: str) -> bool:
        return input(f"{prompt} (y/n): ").lower() == 'y'
    
    def _menu(self) -> None:
        print("\n" + "=" * 50)
        print("1. Добавить   2. Список   3. Найти по ID   4. Найти по имени")
        print("5. Удалить    6. Фильтр   7. Сортировка    8. Скидка")
        print("9. Статистика 0. Выход")
        print("=" * 50)
    
    def _add(self) -> None:
        print("\nТип: 1-обычный 2-питание 3-цифровой")
        t = self._int("Выбор: ")
        try:
            pid = self._int("ID: ")
            name = input("Название: ")
            price = self._float("Цена: ")
            disc = self._int("Скидка(%): ")
            remains = self._int("Остаток: ")
            status = input("Статус: ")
            
            if t == 1:
                p = Product(price, disc, remains, status, pid, name)
            elif t == 2:
                days = self._int("Срок годности(дней): ")
                temp = self._float("Температура: ")
                p = FoodProduct(price, disc, remains, status, pid, name,
                               datetime.now() + timedelta(days=days), temp)
            elif t == 3:
                p = DigitalProduct(price, disc, remains, status, pid, name,
                                  input("Ключ: "), input("Ссылка: "))
            else:
                print("Неверный тип")
                return
            
            self.app.add(p)
            print(f"Добавлен: {name}")
        except DuplicateItemError as e:
            print(f"Ошибка: {e}")
    
    def _list(self) -> None:
        products = self.app.get_all()
        if not products:
            print("\nКаталог пуст")
            return
        print("\n" + "-" * 70)
        print(f"{'ID':<5} {'Название':<25} {'Цена':<10} {'Скидка':<8} {'Остаток':<8}")
        print("-" * 70)
        for p in products:
            print(f"{p.product_id:<5} {p.name:<25} {p.price:<10.2f} {p.discount:<8}% {p.remains:<8}")
        print("-" * 70)
    
    def _find_id(self) -> None:
        pid = self._int("ID: ")
        p = self.app.find_by_id(pid)
        if p:
            print(f"\n{p.name} | Цена: {p.price} | Со скидкой: {p.get_final_price()} | Остаток: {p.remains}")
        else:
            print("Не найден")
    
    def _find_name(self) -> None:
        name = input("Название: ")
        products = self.app.find_by_name(name)
        if products:
            print(f"\nНайдено {len(products)}:")
            for p in products:
                print(f"  {p.product_id}. {p.name} - {p.price} руб.")
        else:
            print("Не найдено")
    
    def _remove(self) -> None:
        pid = self._int("ID: ")
        p = self.app.find_by_id(pid)
        if not p:
            print("Не найден")
            return
        print(f"Товар: {p.name}")
        if self._confirm("Удалить?"):
            self.app.remove(pid)
            print("Удалён")
    
    def _filter(self) -> None:
        print("\n1. Доступные  2. Со скидкой  3. Цена <= ")
        c = self._int("Выбор: ")
        if c == 1:
            products = self.app.filter_available()
            print(f"\nДоступные ({len(products)}):")
            for p in products:
                print(f"  {p.name} - {p.remains} шт.")
        elif c == 2:
            products = self.app.filter_discounted()
            print(f"\nСо скидкой ({len(products)}):")
            for p in products:
                print(f"  {p.name} - скидка {p.discount}%")
        elif c == 3:
            max_p = self._float("Макс. цена: ")
            products = self.app.filter_price(max_p)
            print(f"\nДо {max_p} руб. ({len(products)}):")
            for p in products:
                print(f"  {p.name} - {p.price} руб.")
    
    def _sort(self) -> None:
        print("\n1.Имя 2.Цена↑ 3.Цена↓ 4.Конечная цена 5.Остаток↓")
        c = self._int("Выбор: ")
        if c == 1:
            self.app.sort_by(by_name)
        elif c == 2:
            self.app.sort_by(by_price)
        elif c == 3:
            self.app.sort_by(by_price, True)
        elif c == 4:
            self.app.sort_by(by_final_price)
        elif c == 5:
            self.app.sort_by(by_remains, True)
        else:
            print("Неверно")
            return
        print("Сортировка выполнена")
        self._list()
    
    def _discount(self) -> None:
        pid = self._int("ID: ")
        percent = self._int("Добавить скидку(%): ")
        try:
            self.app.add_discount(pid, percent)
            p = self.app.find_by_id(pid)
            print(f"Новая цена со скидкой: {p.get_final_price()} руб.")
        except ItemNotFoundError as e:
            print(f"Ошибка: {e}")
    
    def _stats(self) -> None:
        s = self.app.stats()
        print(f"\nТоваров: {s['count']}")
        print(f"Общая стоимость: {s['total']:.2f} руб.")
        print(f"Средняя цена: {s['avg']} руб.")
    
    def run(self) -> None:
        while True:
            self._menu()
            c = input("Выберите пункт: ")
            if c == '1':
                self._add()
            elif c == '2':
                self._list()
            elif c == '3':
                self._find_id()
            elif c == '4':
                self._find_name()
            elif c == '5':
                self._remove()
            elif c == '6':
                self._filter()
            elif c == '7':
                self._sort()
            elif c == '8':
                self._discount()
            elif c == '9':
                self._stats()
            elif c == '0':
                print("До свидания!")
                break
            else:
                print("Неверный пункт")