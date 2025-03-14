from game import Game

def get_user_menu_choice():
    print("\nMenu:")
    print("1 - Play a new game")
    print("2 - Show scores")
    print("X - Quit")
    
    choice = input("Enter your choice: ").strip().lower()
    while choice not in ['1', '2', 'x']:
        choice = input("Invalid choice. Enter 1, 2, or X: ").strip().lower()
    return choice

def print_results(results):
    print("\nGame Summary:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thanks for playing!")

def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}
    
    while True:
        choice = get_user_menu_choice()
        if choice == '1':
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == '2':
            print_results(results)
        elif choice == 'x':
            print_results(results)
            break

if __name__ == "__main__":
    main()
