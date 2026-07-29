def display_menu():
    print("\n==============================")
    print("Word Counter")
    print("==============================")
def get_text():
    while True:
        try:
            text = str(input("\nEnter your text: ")).strip()
            if text:
                return text
            print("Text empty")
        except ValueError:
            print("Please enter a valid text")
def count_words(text):
    words = text.split()
    return len(words)
def count_characters(text):
    return len(text)
def count_lines(text):
    return len(text.splitlines())
def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        word = word.strip(".,!?;:\"'()[]{}")
        if word:
            if word in frequency:
                frequency[word]+=1
            else:
                frequency[word]=1
    return frequency
def show_results(text):
    print("\n========================")
    print("Results")
    print("========================")
    print(f"Characters: {count_characters(text)}")
    print(f"Words: {count_words(text)}")
    print(f"Lines: {count_lines(text)}")
    print("\nWord Frequency\n")
    frequency = word_frequency(text)
    for word, amount in frequency.items():
        print(f"{word}: {amount}")
def main():
    while True:
        display_menu()
        text = get_text()
        show_results(text)
if __name__ == "__main__":
    main()  