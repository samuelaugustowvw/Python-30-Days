def display_menu():
    print("\n==============================")
    print("Temperature Converter")
    print("==============================")
    print("1 - Celsius -> Fahrenheit")
    print("2 - Fahrenheit -> Celsius")
    print("3 - Celsius -> Kelvin")
    print("4 - Kelvin -> Celsius")
    print("5 - Fahrenheit -> Kelvin")
    print("6 - Kelvin -> Fahrenheit")
    print("0 - Exit")
def get_option():
    while True:
        try:
            option = int(input("Enter your option: "))
            if(option>=0 and option<=6): return option
            else: print("Invalid option")
        except ValueError:
            print("Please enter a valid number")
def get_temp():
    while True:
        try:
            return float(input("Enter your temperature: "))
        except ValueError:
            print("Please enter a valid temperature")
def main():
    result=0
    while True:
        display_menu()
        option = get_option()
        temp = get_temp()
        print("==============================")
        match option:
            case 0:
                print(f"Goodbye!")
                break
            case 1:
                result = (temp*9/5)+32
                print(f"{temp:.2f}°C = {result:.2f}°F")
            case 2:
                result = (temp-32)*5/9
                print(f"{temp:.2f}°F = {result:.2f}°C")
            case 3:
                result = (temp+273.15)
                print(f"{temp:.2f}°C = {result:.2f}°K")
            case 4:
                result = (temp-273.15)
                print(f"{temp:.2f}°K = {result:.2f}°C")
            case 5:
                result = (temp-32)*5/9+273.15
                print(f"{temp:.2f}°F = {result:.2f}°K")
            case 6:
                result = ((temp-273.15)*9/5+32)
                print(f"{temp:.2f}°K = {result:.2f}°F")

if __name__ == "__main__":
    main()