RATES = {
    "USD":1.00,
    "BRL":5.14,
    "EUR":0.86,
    "GBP":0.74,
    "JPY":148.0,
    "CAD":1.38,
    "ARS":1328.0,
}
def display_menu():
    print("\n========================")
    print("   Currency Converter")
    print("========================")
    print("Available currencies:")
    print(", ".join(RATES.keys()))
def get_currency(message):
    while True:
        code = input(message).strip().upper()
        if code in RATES:
            return code
        print(f"'{code}' is not available. Choose one of: {', '.join(RATES.keys())}\n")
def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount > 0:
                return amount
            print("Amount must be greater than zero.\n")
        except ValueError:
            print("Please enter a valid number.\n")
def convert(amount,from_currency,to_currency):
    amount_in_usd = amount/RATES[from_currency]
    return amount_in_usd*RATES[to_currency]
def get_yes_no(message):
    while True:
        answer = input(message).strip().upper()
        if(answer in ("Y", "N")):
            return answer=="Y"
        print("Please enter Y or N.\n")
def main():
    history = []
    while True:
        display_menu()
        from_currency = get_currency("\nFrom (currency code): ")
        to_currency = get_currency("To (currency code): ")
        amount = get_amount()
        result = convert(amount,from_currency,to_currency)
        print("========================")
        print(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
        print(f"Rate: 1 {from_currency} = {result / amount:.4f} {to_currency}")
        print("========================")
        history.append(f"{amount:.2f} {from_currency} -> {result:.2f} {to_currency}")
 
        if not get_yes_no("\nConvert again? (Y/N): "):
            break
    if history:
        print("\n========================")
        print("   SESSION HISTORY")
        print("========================")
        for line in history:
            print(line)
    print("\nGoodbye!")
if __name__ == "__main__":
    main()