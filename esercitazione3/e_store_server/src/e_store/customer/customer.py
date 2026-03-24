from abc import ABC, abstractmethod
from e_store.store_item.store_item import NormalItem, GenericItem

class GenericCustomer(ABC):
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password
        self.backpack = {}

    def get_price(self, item):
        return item.price
    
    def check_pwd(self, pwd):
        return self.password == pwd

    def check_balance(self, price_item):
        return self.balance >= price_item
    
    def pay(self, price_item):
        self.balance -= price_item

    def add_to_backpack(self, item, quantity: int):
        """Aggiunge un oggetto allo zaino o ne aggiorna la quantità."""
        if item in self.backpack:
            self.backpack[item] += quantity
        else:
            self.backpack[item] = quantity

    def get_backpack_items(self):
        """Restituisce il dizionario degli oggetti posseduti."""
        return self.backpack

    def __str__(self):
        return f"'{self.name}', balance: {self.balance}, password: {self.password}, backpack items: {sum(self.backpack.values())}."

class NormalCustomer(GenericCustomer):
    def __init__(self, name, balance, password):
        super().__init__(name, balance, password)

class PromotionalCustomer(GenericCustomer):
    discount = 0.05

    def __init__(self, name, balance, password):
        super().__init__(name, balance, password)
    
    def get_price(self, item):
        return item.price * (1 - self.discount)
