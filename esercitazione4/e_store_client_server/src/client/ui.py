import requests

class UI:
    def __init__(self, base_url: str,):
        self.base_url = base_url
        self.username = None

    def login(self):
        print("---- LOGIN ----")
        name = input("Inserisci il tuo username: ").strip()
        password = input("Inserisci la tua password: ").strip()
        customer_type = input("Sei un 'promotional' o 'normal' customer? ").strip().lower()
        
        data = {
            "username" : name,
            "password" : password,
            "customer_type" : customer_type
        }

        try:
            response = requests.post(f"{self.base_url}/register", json=data)
            info = response.json()

            if response.status_code == 200 and info.get("success"):
                print(f"{info['message']}")
                self.username = name 
            else:
                print(f"Errore: {info.get('message', 'Registrazione fallita')}")
        except requests.exceptions.ConnectionError:
            print("Impossibile collegarsi al server")


    def run(self):
        self.login()

        while True:
            resp_inv = requests.get(f"{self.base_url}/get_inventory")
            if resp_inv.status_code != 200:
                print("Impossibile ottenere l'inventario dal server.")
                break
            inventory = resp_inv.json()

            resp_bal = requests.get(f"{self.base_url}/get_balance", params={"username": self.username})
            if resp_bal.status_code != 200:
                print("Impossibile ottenere il saldo dal server.")
                break
            balance = resp_bal.json()

            print("\n--- Negozio ---")
            for i, item in enumerate(inventory):
                print(f"[{i}] {item['name']:<15} {item['price']:.2f}€ (disponibili: {item['quantity']})")

            balance = balance["balance"]
            print(f"\nIl tuo saldo: {balance:.2f}€")
            cmd = input("\nCosa vuoi fare? [buy / quit]: ").strip().lower()

            if cmd == "quit":
                print("Arrivederci!")
                break
            elif cmd == "buy":
                self._handle_purchase(inventory)
            else:
                print("Comando non riconosciuto. Usa 'buy' o 'quit'.")


    def _handle_purchase(self, inventory):
        if not inventory:
            print("Il negozio è vuoto, niente da acquistare.")
            return
        
        while(True): 
            try:
                idx = int(input("Numero prodotto: ").strip())
                qty = int(input("Quantità: ").strip())
                if (idx < 0 or idx >= len(inventory))or (qty < 0):
                    print("Non inserire numeri negativi. Riprova.")
                    continue 
                break
            except ValueError:
                print("Input non valido, inserisci numeri interi.")

        pwd = input("Password: ").strip()
        
        item_name = inventory[idx]["name"]

        payload = {
            "username": self.username,
            "password": pwd,
            "item": item_name,
            "quantity": qty
        }

        response = requests.post(f"{self.base_url}/purchase", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            print(f"\n{data['message']}")
        else:
            error_detail = response.json().get("detail", "Errore durante l'acquisto.")
            print(f"\nTransazione fallita: {error_detail}")   
            
        

        