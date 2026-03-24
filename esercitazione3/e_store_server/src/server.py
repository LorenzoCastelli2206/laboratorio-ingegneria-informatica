from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

from e_store.store.store import Store
from e_store.store_inventory.store_inventory import StoreInventory
from e_store.customer.customer import NormalCustomer, PromotionalCustomer
from e_store.store_item.store_item import NormalItem, ForeignItem, GenericItem

app = FastAPI(title= "E-Store API")

# popoliamo il server
store = Store("Tech Shop", money= 5000.0)
laptops = NormalItem("Laptop", 800.0, "Italia")
phones = NormalItem("Smartphone", 400.0, "Italia")
macchine = ForeignItem("Macchina", 300.0, "Milano")
drones = ForeignItem("Drone", 500.0, "Sapienza Flight Team")
store.inventory.add_item(laptops, 5)
store.inventory.add_item(phones, 10)
store.inventory.add_item(macchine, 3)
store.inventory.add_item(drones, 2)

user_db = {
    "GENOVESE": PromotionalCustomer("GENOVESE", 2000, "0"),
    "Lorenzo": NormalCustomer("Lorenzo", 1500, "1")
}

class ItemInventoryResponse(BaseModel):
    name : str
    price : float
    quantity : int

class ItemUserResponse(BaseModel):
    name: str
    quantity : int

class UserBalanceResponse(BaseModel):
    name : str
    balance : float

class PurchaseRequest(BaseModel):
    username : str
    password : str
    item : str
    quantity : int

#class PurchaseResponse(BaseModel):

@app.get("/get_inventory", response_model= List[ItemInventoryResponse])
def get_inventory():
    ret = []

    for item,q in store.inventory.dictItem.items(): 
        ret.append(ItemInventoryResponse(name= item.name, price= item.price, quantity = q))

    return ret


@app.get("/get_user_items", response_model= List[ItemUserResponse])
def get_user_items(username: str):
    if username not in user_db:
        raise HTTPException(status_code= 404, detail="User not found")
        
    ret = []
    customer = user_db[username]
    for item, quantity in customer.get_backpack_items().items():
        ret.append(ItemUserResponse(name=item.name, quantity=quantity))
        
    return ret


@app.get("/get_item_information", response_model= ItemInventoryResponse)
def get_item_information(name: str):
    for item,q  in store.inventory.dictItem.items():
        if item.name==name:
            return ItemInventoryResponse(name = item.name, price = item.price,quantity = q )
    raise HTTPException(status_code= 404, detail="Item not found")


@app.get("/get_balance", response_model= UserBalanceResponse)
def get_balance(username: str):
    if username not in user_db:
        raise HTTPException(status_code= 404, detail="User not found")
        
    customer = user_db[username]
    return UserBalanceResponse(name=customer.name, balance=customer.balance)
        


    
