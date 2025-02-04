# Function to calculate BMI
def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / (height (m) ** 2)
    bmi = weight / (height ** 2)
    return bmi

# Function to interpret the BMI value
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Main program
def main():
    print("Welcome to the BMI Calculator!")
    
    # Taking input from the user
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in meters (m): "))
    
    # Calculating BMI
    bmi = calculate_bmi(weight, height)
    
    # Output the result
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {interpret_bmi(bmi)}")

# Run the main program
if __name__ == "__main__":
    main()
