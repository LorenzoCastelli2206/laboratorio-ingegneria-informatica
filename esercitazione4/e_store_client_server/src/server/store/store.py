from store_inventory.store_inventory import StoreInventory

class Store:
    def __init__(self, name, money):
       self.name = name
       self.inventory = StoreInventory()
       self.money = money

    def sell_to_customer(self, item, quantity, customer):
        if not self.inventory.has_item(item, quantity):
            return False, f"Not enough '{item.name}'."

        effective_price = customer.get_price(item) * quantity

        if not customer.check_balance(effective_price):
            return False, (f"Missing money: {effective_price - customer.balance}€ left, "
                           f"balance is {customer.balance:.2f}€.")

        self.inventory.remove_item(item, quantity)
        customer.pay(effective_price)
        self.money += effective_price
        customer.add_to_backpack(item, quantity)  #aggiunge nello zaino del customer lo/gli oggetto/i

        return True, (f"Purchase completed: {quantity}x '{item.name}' "
                      f"for {effective_price:.2f}€.")

    def __str__(self) :
        return f"'{self.name}', inventory: \n{self.inventory}."