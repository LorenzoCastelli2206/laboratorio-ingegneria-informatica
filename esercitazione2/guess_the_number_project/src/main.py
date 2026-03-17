from gui.gui import GUI
from player.player import CpuPlayer, HumanPlayer

def setup_player():
    print("--- INIZIO PARTITA ---")
    print("  [1] se vuoi giocare ")
    print("  [2] se vuoi far giocare la CPU ")
    tipo = input("Scegli: ").strip()

    if tipo == "2":
        return CpuPlayer()
    elif tipo == "1":
        name = input("Nome: ").strip()
        return HumanPlayer(name)
    else:
        print("\n\nScelta non valida\n\n")
        return setup_player()
    

def main():
    player = setup_player()
    gui = GUI(player, max_number=100)
    gui.run()
    return 0


if __name__ == "__main__":
    main()