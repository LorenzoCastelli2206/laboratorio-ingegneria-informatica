from store_item.store_item import GenericItem

class StoreInventory:
    def __init__(self):
       self.dictItem = {}

    def has_item(self, item, quantity=1):
        return self.dictItem.get(item, 0) >= quantity

    def add_item(self, item, n):
        if item.name not in self.dictItem:
            self.dictItem[item] = 0
        self.dictItem[item] += n

    def remove_item(self, item, n):
        self.dictItem[item] -= n
        if self.dictItem[item] <= 0:
            del self.dictItem[item]

    def __str__(self) :
        rows = [f"{key}: {value}" for key, value in self.dictItem.items()]
        return "\n".join(rows)
