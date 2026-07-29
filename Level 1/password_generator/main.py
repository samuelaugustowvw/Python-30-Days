import random
import string
def display_menu():
    print("\n==============================")
    print("Password Generator")
    print("==============================")
def get_password_length():
    while True:
        try:
            length = int(input("Password length: "))
            if(length>=4):
                return length
            print("The password must have at least 4 characters\n")
        except ValueError:
            print("Please enter a valid number\n")
def get_yes_no(message):
    while True:
        answer = input(message).strip().upper()
        if(answer in ("Y", "N")):
            return answer == "Y"
        print("Please enter Y or N.\n")
def generate_password(length,uppercase,lowercase,numbers,symbols):
    characters = ""
    if uppercase: characters+=string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    if lowercase: characters+=string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
    if numbers:   characters+=string.digits          # 0123456789
    if symbols:   characters+=string.punctuation     # !@#$%^&*()_+-=[]{}|;:,.<>?
    if not characters: return None
    password = ""
    for _ in range(length):
        password+=random.choice(characters)
    return password
def main():
    display_menu()
    length    = get_password_length()
    uppercase = get_yes_no("Include uppercase letters? (Y/N): ")
    lowercase = get_yes_no("Include lowercase letters? (Y/N): ")
    numbers   = get_yes_no("Include numbers? (Y/N): ")
    symbols   = get_yes_no("Include symbols? (Y/N): ")
    password  = generate_password(length,uppercase,lowercase,numbers,symbols)
    if password is None:
        print("\nYou must select at least one character type.\n")
    print("==============================")
    print(password)
if __name__ == "__main__":
    main()