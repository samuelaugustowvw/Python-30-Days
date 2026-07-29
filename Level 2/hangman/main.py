import random
WORDS = [
    {"word": "python",    "hint": "A popular programming language"},
    {"word": "keyboard",  "hint": "You use it to type"},
    {"word": "banana",    "hint": "A yellow fruit"},
    {"word": "guitar",    "hint": "A musical instrument with strings"},
    {"word": "elephant",  "hint": "The largest land animal"},
    {"word": "computer",  "hint": "You are using one right now"},
    {"word": "mountain",  "hint": "A very tall natural elevation"},
    {"word": "coffee",    "hint": "A popular morning drink"},
]
HANGMAN_STAGES = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========""",
]
MAX_ATTEMPTS = 6
def display_menu():
    print("\n========================")
    print("        Hangman")
    print("========================")
def get_letter():
    while True:
        letter = str(input("Enter a letter: "))
def get_yes_no(message):
    while True:
        answer = str(input(message)).strip().upper()
        if(answer in ("Y","N")):
            return answer == "Y"
        print("Invalid option please Y or N")
def is_word_complete(secret_word,guessed_letters):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True
def get_letter(guessed_letters):
    while True:
        letter = input("\nEnter a letter: ").strip().lower()
        if len(letter)!=1:
            print("Please enter exactly one letter.")
        elif not letter.isalpha():
            print("Please enter a letter (a-z).")
        elif letter in guessed_letters:
            print(f"You already guessed '{letter}'. Try another.")
        else:
            return letter
def display_state(secret_word,guessed_letters,wrong_count,hint):
    print(HANGMAN_STAGES[wrong_count])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word+=letter+" "
        else:
            display_word+="_ "
    print(f"\nHint: {hint}")
    print(f"Word: {display_word.strip()}")
    print(f"Attempts left: {MAX_ATTEMPTS - wrong_count}")
    wrong_letters = [l for l in guessed_letters if l not in secret_word]
    if wrong_letters:
        print(f"Wrong letters: {', '.join(sorted(wrong_letters))}")
def game():
    chosen = random.choice(WORDS)
    secret_word = chosen["word"]
    hint = chosen["hint"]
    guessed_letters = set()
    wrong_count = 0
    while True:
        display_state(secret_word, guessed_letters, wrong_count, hint)
        letter = get_letter(guessed_letters)
        guessed_letters.add(letter)
        if letter in secret_word:
            print("Good guess!")
        else:
            wrong_count+=1
            print(f"Wrong! '{letter}' is not in the word.")
        if is_word_complete(secret_word, guessed_letters):
            print("\n========================")
            print(f"Word: {' '.join(secret_word)}")
            print("You won! 🎉")
            print("========================")
            break
        if wrong_count >= MAX_ATTEMPTS:
            print(HANGMAN_STAGES[wrong_count])
            print("\n========================")
            print("You lost! 💀")
            print(f"The word was: {secret_word.upper()}")
            print("========================")
            break
def main():
    display_menu()
    while True:
        game()
        if not get_yes_no("\nPlay again? (Y/N): "):
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()