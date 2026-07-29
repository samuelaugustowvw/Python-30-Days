def display_menu():
    print("\n==============================")
    print("IMC Calculator")
    print("==============================")
def get_weight():
    while True:
        try:
            weight = float(input("Enter your weight(kg): "))
            if(weight>0):
                return weight
            print("Weight must be greater than zero.\n")
        except ValueError:
            print("Please enter a valid number.\n")
def get_height():
    while True:
        try:
            height = float(input("Enter your height(m): "))
            if(height>0):
                return height
        except ValueError:
            print("Please enter a valid number.\n")
def calculate_imc(w,h):
    return w/(h**2)
def get_classification(imc):
    if(imc<18.5):
        return "Underweight"
    elif(imc<25):
        return "Normal weight"
    elif(imc<30):
        return "Overweight"
    elif(imc<35):
        return "Obesity Class I"
    elif(imc<40):
        return "Obesity Class II"
    else:
        return "Obesity Class III"
def main():
    display_menu()
    weight = get_weight()
    height = get_height()
    imc = calculate_imc(weight,height)
    result = get_classification(imc)
    print("==============================")
    print(f"IMC: {imc:2f}\nStatus: {result:.2f}")
if __name__ == "__main__":
    main()