import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab07.cli import CLI
from lab07.storage import save, load
from lab07.app import ShopApp


def main() -> None:
    print("Загрузка...")
    app = ShopApp()
    loaded = load('data.json')
    if loaded:
        for p in loaded.get_all():
            try:
                app.add(p)
            except:
                pass
        print(f"Загружено {len(loaded.get_all())} товаров")
    
    cli = CLI()
    cli.app = app
    cli.run()
    save(app.get_catalog(), 'data.json')
    print("Сохранено")


if __name__ == "__main__":
    main()