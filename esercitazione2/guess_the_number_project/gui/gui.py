import random
import csv
from datetime import datetime
from player.player import Player

class GUI:
    def __init__(self, player: Player, max_number):
        self.player = player
        self.max_number = max_number
        self.target_number = random.randint(0, self.max_number)
        self.tentativi_fatti = []

    def run(self):
        print(f"\n--- INIZIA IL GIOCO: Indovina il numero da 0 a {self.max_number} ---")
        feedback = None
        
        while True:
            guess = self.player.get_guess(feedback)
            self.tentativi_fatti.append(guess)
            try:
                int(guess)
            except: 
                print("ERRORE!") 
                self.salva_risultati_err()
                break

            if guess > self.target_number:
                feedback = "Il tuo numero è troppo alto"
                print(feedback)
            elif guess < self.target_number:
                feedback = "Il tuo numero è troppo basso"
                print(feedback)
            else:
                print("Complimenti, hai vinto!!!!")
                self.salva_risultati()
                break

    def salva_risultati(self):
        nome = self.player.name
        da_indovinare = self.target_number
        num_tentativi = len(self.tentativi_fatti)
        lista_tentativi = str(self.tentativi_fatti)
        
        now = datetime.now()
        data = now.strftime("%d-%m-%Y")
        ora = now.strftime("%H:%M:%S")
        
        file_name = "storico_partite.tsv"
        with open(file_name, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter='\t')
            writer.writerow([nome, da_indovinare, num_tentativi, lista_tentativi, data, ora])
        
        print(f"I risultati della partita sono stati salvati su {file_name}")

    def salva_risultati_err(self):
        nome = self.player.name
        now = datetime.now()
        data = now.strftime("%d-%m-%Y")
        ora = now.strftime("%H:%M:%S")

        file_name = "storico_partite.tsv"
        with open(file_name, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter= '\t')
            writer.writerow([nome, "non ha inserito un numero, causando un errore", data, ora])
        
        print(f"I risultati della partita sono stati salvati su {file_name}")
