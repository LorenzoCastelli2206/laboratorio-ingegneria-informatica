from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

from store.store import Store
from customer.customer import NormalCustomer, PromotionalCustomer
from store_item.store_item import NormalItem, ForeignItem

app = FastAPI(title= "E-Store API")

# --- POPOLIAMO IL SERVER ---
store = Store("Tech Shop", money= 5000.0)

laptops = NormalItem("Laptop", 800.0, "Italia")
phones = NormalItem("Smartphone", 400.0, "Italia")
tablets = NormalItem("Tablet", 350.0, "Italia")
smartwatches = NormalItem("Smartwatch", 200.0, "Italia")
cavi_usb = NormalItem("Cavo USB", 15.0, "Italia")

visori_vr = ForeignItem("Visore VR", 600.0, "USA")
cani_robot = ForeignItem("Cane Robot", 1200.0, "Giappone")
schede_video = ForeignItem("Scheda Video", 900.0, "Taiwan")
macchine = ForeignItem("Macchina", 300.0, "Islanda")
drones = ForeignItem("Drone", 500.0, "Sapienza Flight Team")

store.inventory.add_item(laptops, 5)
store.inventory.add_item(phones, 10)
store.inventory.add_item(tablets, 8)
store.inventory.add_item(smartwatches, 15)
store.inventory.add_item(cavi_usb, 50)

store.inventory.add_item(macchine, 3)
store.inventory.add_item(drones, 2)
store.inventory.add_item(visori_vr, 4)
store.inventory.add_item(cani_robot, 1) 
store.inventory.add_item(schede_video, 6)

# --- DATABASE UTENTI ---
user_db = {
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

class PurchaseResponse(BaseModel):
    message : str
    balance : float
    item : str
    quantity : int 

class RegisterRequest(BaseModel):
    username: str
    password: str
    customer_type: str 

class RegisterResponse(BaseModel):
    message: str
    success: bool

@app.post("/register", response_model=RegisterResponse)
def register(request: RegisterRequest):
    if request.username in user_db:
        user = user_db[request.username]
        if user.check_pwd(request.password):
            return RegisterResponse(message=f"Bentornato, {request.username}!", success=True)
        else:
            return RegisterResponse(message="Password errata per l'utente esistente.", success=False)
        
    start_balance = 10000

    if request.customer_type.lower() == "promotional":
        new_user = PromotionalCustomer(request.username, start_balance, request.password)
    else:
        new_user = NormalCustomer(request.username, start_balance, request.password)
        
    user_db[request.username] = new_user
    
    return RegisterResponse(message=f"Nuovo utente '{request.username}' registrato con successo!", success=True)


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


@app.post("/purchase", response_model= PurchaseResponse)
def purchase(request: PurchaseRequest):
    if request.username not in user_db:
        raise HTTPException(status_code= 404, detail="User not found")
    
    user = user_db[request.username]
    if not user.check_pwd(request.password):
        raise HTTPException(status_code= 401, detail="Wrong Password")
    
    target = None
    target_q = 0
    for item, q in store.inventory.dictItem.items():
        if item.name == request.item:
            target = item
            target_q = q
            break

    if target is None:
        raise HTTPException(status_code= 404, detail="Item not found in store")
    
    success, message = store.sell_to_customer(target, request.quantity, user)
    if not success: 
        raise HTTPException(status_code= 404, detail= message)
    
    return PurchaseResponse(message= message, balance= user.balance, item= target.name, quantity= target_q)
