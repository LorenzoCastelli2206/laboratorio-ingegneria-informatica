from e_store.store.store import Store
from e_store.customer.customer import GenericCustomer


class UI:
    def __init__(self, store: Store, customer: GenericCustomer):
        self.store = store
        self.customer = customer

    def run(self):
        print(f"\nBenvenuto, {self.customer.name}!")
        print(f"Tipo cliente: {self.customer.__class__.__name__}")

        while True:
            print("\n" + str(self.store))
            print(f"Il tuo saldo: {self.customer.balance:.2f}€")
            cmd = input("\nCosa vuoi fare? [buy / quit]: ").strip().lower()

            if cmd == "quit":
                print("Arrivederci!")
                break
            elif cmd == "buy":
                self._handle_purchase()
            else:
                print("Comando non riconosciuto. Usa 'buy' o 'quit'.")

    def _handle_purchase(self):
        items = list(self.store.inventory.dictItem.keys())

        if not items:
            print("Il negozio è vuoto, niente da acquistare.")
            return

        print("\nProdotti disponibili:")
        for i, item in enumerate(items):
            qty = self.store.inventory.dictItem[item]
            effective_price = self.customer.get_price(item)
            print(f"  [{i}] {item.name:<20} {effective_price:.2f}€  (disponibili: {qty})")

        try:
            idx = int(input("Numero prodotto: ").strip())
            qty = int(input("Quantità: ").strip())
        except ValueError:
            print("Input non valido, inserisci numeri interi.")
            return

        if idx < 0 or idx >= len(items):
            print("Indice prodotto fuori range.")
            return

        if qty <= 0:
            print("La quantità deve essere maggiore di zero.")
            return

        pwd = input("Password: ").strip()
        if not self.customer.check_pwd(pwd):
            print("Password errata!")
            return

        item = items[idx]
        success, msg = self.store.sell_to_customer(item, qty, self.customer)
        print(msg)