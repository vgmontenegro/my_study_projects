import pandas as pd
from enum import Enum, auto
import json


class ProductType(Enum):
    FUNGICIDE = auto()
    HERBICIDE = auto()
    INSECTICIDE = auto()


class Product:

    def __init__(self, name: str, product_type: ProductType):
        self._name = name
        self._type = product_type.name
        self._info = {"Name": self._name, "Type": self._type}

    @property
    def info(self):
        return self._info

    def add_product(self):
        with open('products.json', 'a') as products_file:
            json.dump(self._info, products_file, indent=4)

    @classmethod
    def get_product(cls, name):
        with open('products.json', 'r') as products_file:
            pass


class Talhao:
    def __init__(self, name: str, area: float):
        self._name = name
        self._area = area
        self.spray_operations = {}

    @property
    def area(self):
        return self._area

    def add_spray_operation(self, date: str, products: dict):
        date = pd.to_datetime(date, format='%d/%m/%Y')
        if type(products) == dict:
            self.spray_operations[date.strftime('%d/%m/%Y')] = products
        else:
            raise TypeError("Product must be a dictionary -> {product:dose}")

    def get_spray_operations(self):
        return self.spray_operations
