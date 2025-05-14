
from menu import show_menu
from game import run_game

def main():
    while True:
        mode = show_menu()
        if mode is None: 
            break
        run_game(mode)

if __name__ == "__main__":
    main()