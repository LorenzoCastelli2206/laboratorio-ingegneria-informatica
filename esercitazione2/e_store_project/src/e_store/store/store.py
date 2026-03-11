from e_store.store_inventory.store_inventory import StoreInventory

class Store:
    def __init__(self, name, money):
       self.name = name
       self.inventory = StoreInventory()
       self.money = money

    def sell_to_customer(self, item, quantity, customer):
        if not self.inventory.has_item(item, quantity):
            return False, f"Quantità insufficiente per '{item.name}'."

        effective_price = customer.get_price(item) * quantity

        if not customer.check_balance(effective_price):
            return False, (f"Saldo insufficiente: mancano {effective_price - customer.balance}€, "
                           f"il saldo del cliente è {customer.balance:.2f}€.")

        self.inventory.remove_item(item, quantity)
        customer.pay(effective_price)
        self.money += effective_price

        return True, (f"Acquisto completato: {quantity}x '{item.name}' "
                      f"per {effective_price:.2f}€.")

    def __str__(self) :
        return f"'{self.name}', inventory: \n{self.inventory}."