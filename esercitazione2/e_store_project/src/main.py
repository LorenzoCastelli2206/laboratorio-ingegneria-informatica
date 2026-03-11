from e_store.ui.ui import UI
from e_store.store.store import Store
from e_store.customer.customer import NormalCustomer, PromotionalCustomer
from e_store.store_item.store_item import NormalItem, ForeignItem


def setup_store():
    store = Store("Tech Shop", money=5000.0)

    laptops = NormalItem("Laptop", 800.0, "Italia")
    phones = NormalItem("Smartphone", 400.0, "Italia")
    lorenzi = ForeignItem("Lore", 300.0, "Poggio San lorenzo")
    drones = ForeignItem("Drone", 500.0, "Sapienza Flight Team")

    store.inventory.add_item(laptops, 5)
    store.inventory.add_item(phones, 10)
    store.inventory.add_item(lorenzi, 3)
    store.inventory.add_item(drones, 2)

    return store


def create_customer():
    print("=== Registrazione cliente ===")
    print("  [1] Cliente normale")
    print("  [2] Cliente promozionale (5% di sconto su tutto)")
    tipo = input("Scelta: ").strip()

    name = input("Nome: ").strip()
    money = float(input("Saldo iniziale (€): ").strip())
    password = input("Password: ").strip()

    if tipo == "2":
        return PromotionalCustomer(name, money, password)
    return NormalCustomer(name, money, password)


def main():
    store = setup_store()
    customer = create_customer()

    ui = UI(store, customer)
    ui.run()

    # Stampa finale dello stato
    print("\n=== Riepilogo finale ===")
    print(store)
    print(customer)


if __name__ == "__main__":
    main()