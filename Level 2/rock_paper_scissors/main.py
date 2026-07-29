import random
BEATS = {
    "Rock":     "Scissors",
    "Paper":    "Rock",
    "Scissors": "Paper",
}
MOVES = {
    1: "Rock",
    2: "Paper",
    3: "Scissors",
}
WINS_NEEDED = 3
def display_menu():
    print("\n========================")
    print(" Rock Paper & Scissors")
    print("========================")
    print(f"First to {WINS_NEEDED} wins!\n")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
def get_player_move():
    while True:
        try:
            option = int(input("Enter your choice: "))
            if(option in MOVES):
                return MOVES[option]
        except ValueError:
            print(f"Please invalid number")
def get_round_result(player,computer):
    if player==computer:
        return "tie"
    if BEATS[player]==computer:
        return "player"
    return "computer"
def get_yes_no(message):
    while True:
        answer = str(input(message)).strip().upper()
        if(answer in ("Y","N")):
            return answer == "Y"
        print(f"Please enter Y or N")
def game():
    player_score=computer_score=0
    while player_score<WINS_NEEDED and computer_score<WINS_NEEDED:
        display_menu()
        player_move = get_player_move()
        computer_move = random.choice(list(MOVES.values()))
        print(f"\nYou chose:      {player_move}")
        print(f"Computer chose: {computer_move}")
        result = get_round_result(player_move,computer_move)
        if result=="tie":
            print("It's a tie!")
        elif result=="player":
            player_score+=1
            print("You win this round!")
        else:
            computer_score+=1
            print("Computer wins this round!")
        print(f"\nScore -> You: {player_score} | Computer: {computer_score}")
        print("------------------------")
    print("\n========================")
    print(f"Final Score -> You: {player_score} | Computer: {computer_score}")
    if player_score>computer_score:
        print("You won the game! 🏆")
    else:
        print("Computer won the game! 🤖")
    print("========================")
def main():
    while True:
        game()
        if not get_yes_no("\nPlay again?(Y/N): "):
            print(f"Goodbye!")
            break
if __name__ == "__main__":
    main()