from abc import ABC

class GenericItem(ABC):
    def __init__(self, name, price, nation):
       self.name = name
       self.price = price
       self.nation = nation

    def __str__(self) :
        return f"'{self.name}', price: {self.price}"
    
class NormalItem(GenericItem):
    def __init__(self, name, price, nation):
        super().__init__(name, price, nation)

class ForeignItem(GenericItem):
    def __init__(self, name, price, nation):
        super().__init__(name, price, nation)
        self.price = self.price*1.2
 