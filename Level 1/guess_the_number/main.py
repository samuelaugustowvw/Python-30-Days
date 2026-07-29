import random
def display_menu():
    print("\n==============================")
    print("Guess the Number")
    print("==============================")
    print(f"Choose a Difficulty:")
    print(f"1 - Easy(1-10)")
    print(f"2 - Medium(1-50)")
    print(f"3 - Hard(1-100)")
def get_option():
    while True:
        try:
            option = int(input("\nChoose an option: "))
            if 0<=option<= 3:
                return option
            print("Invalid option.")
        except ValueError:
            print("Please enter a valid number.")
def get_guess(min_number,max_number):
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if(min_number<=guess<=max_number):
                return guess
            print(f"Your guess must be between {min_number} and {max_number}.")
        except ValueError:
            print("Please enter a valid number.")
def game(max_number):
    attempts=0
    secret_number = random.randint(1,max_number)
    print(f"\nI'm thinking of a number between 1 and {max_number}.")
    while True:
        guess = get_guess(1,max_number)
        attempts+=1
        if guess<secret_number:
            print("Too low!")

        elif guess>secret_number:
            print("Too high!")
        else:
            print("==============================")
            print("Congratulations!")
            print("You guessed the number!")
            print(f"Number: {secret_number}")
            print(f"Attempts: {attempts}")
            break
def main():
    while True:
        display_menu()
        option = get_option()
        match option:
            case 1:
                game(10)
            case 2:
                game(50)
            case 3:
                game(100)
            case 0:
                print(f"Goodbye!")
                break
if __name__ == "__main__":
    main()  