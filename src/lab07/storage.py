import json
import os
from typing import List
from lab01.model import Product
from lab03.models import FoodProduct, DigitalProduct
from datetime import datetime


def _to_dict(p: Product) -> dict:
    data = {'type': type(p).__name__, 'id': p.product_id, 'name': p.name,
            'price': p.price, 'discount': p.discount, 'remains': p.remains,
            'status': p.status, 'active': p.active}
    if isinstance(p, FoodProduct):
        data['exp_date'] = p.expiration_date.isoformat()
        data['temp'] = p.storage_temperature
    elif isinstance(p, DigitalProduct):
        data['license'] = p.license_key
        data['link'] = p.download_link
    return data


def _from_dict(d: dict) -> Product:
    if d['type'] == 'FoodProduct':
        p = FoodProduct(d['price'], d['discount'], d['remains'], d['status'],
                       d['id'], d['name'], datetime.fromisoformat(d['exp_date']), d['temp'])
    elif d['type'] == 'DigitalProduct':
        p = DigitalProduct(d['price'], d['discount'], d['remains'], d['status'],
                          d['id'], d['name'], d['license'], d['link'])
    else:
        p = Product(d['price'], d['discount'], d['remains'], d['status'], d['id'], d['name'])
    if not d['active']:
        p.deactivate()
    return p


def save(collection, path: str) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump([_to_dict(p) for p in collection.get_all()], f, ensure_ascii=False, indent=2)


def load(path: str):
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    from lab05.collection import ExtendedProductCatalog
    coll = ExtendedProductCatalog()
    for d in data:
        coll.add(_from_dict(d))
    return coll