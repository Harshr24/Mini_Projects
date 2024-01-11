class BMICalculator:
    def __init__(self):
        self.weight = 0
        self.height_ft = 0
        self.height_inch = 0

    def ft_and_inch_to_m(self, ft, inch=0.0):
        return ft * 0.3048 + inch * 0.0254

    def lb_to_kg(self, lb):
        return lb * 0.4535923

    def calculate_bmi(self):
        self.weight = float(input("Enter your weight in pounds: "))
        self.height_ft = int(input("Enter your height in feet: "))
        self.height_inch = float(input("Enter the remaining inches: "))

        weight_kg = self.lb_to_kg(self.weight)
        height_m = self.ft_and_inch_to_m(self.height_ft, self.height_inch)

        if height_m < 1.0 or height_m > 2.5 or weight_kg < 20 or weight_kg > 200:
            return None

        return weight_kg / height_m ** 2


# Create an instance of the BMICalculator class
bmi_calculator = BMICalculator()

# Calculate BMI and display the result
calculated_bmi = bmi_calculator.calculate_bmi()

if calculated_bmi is None:
    print("Invalid height or weight values entered. Please enter valid values.")
else:
    print(f"Your BMI is: {calculated_bmi:.2f}")
