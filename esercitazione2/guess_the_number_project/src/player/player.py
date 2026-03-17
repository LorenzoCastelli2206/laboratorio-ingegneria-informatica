from abc import ABC

class Player(ABC):
    def __init__(self, name):
        self.name = name

    def __str__(self) :
        return f"Nome giocatore: '{self.name}'"
    
    def get_guess(self, feedback = None):
        pass

class CpuPlayer(Player):
    def __init__(self, name = "CPU", max_val = 100):
        super().__init__("CPU")
        self.min_val = 0
        self.max_val = max_val
        self.last_guess = None

    def get_guess(self, feedback = None):
        if feedback == "Il tuo numero è troppo alto":
            self.max_val = self.last_guess - 1
        elif feedback == "Il tuo numero è troppo basso":
            self.min_val = self.last_guess + 1
        
        self.last_guess = (self.min_val + self.max_val) // 2
        print(f"La CPU ha scelto: {self.last_guess}")
        return self.last_guess


class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def get_guess(self, feedback = None):
        while True:
            try:
                scelta = input("Fai un tentativo: ")
                return int(scelta)
            except ValueError:
                print("NON E' STATO INSERITO UN NUMERO!")
                break
