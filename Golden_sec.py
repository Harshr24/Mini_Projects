import math 

# Golden Section Search function using iteration formula
def golden_sec_formula(f, a, b, tolerance):
    if tolerance <= 0 or b - a <= 0:
        print("Error: Please ensure tolerance and interval bounds are positive and the interval is valid.")
        return None

    golden_ratio = (3 - math.sqrt(5)) / 2  # Golden ratio
    iterations = math.ceil(math.log(abs(tolerance) / (b - a)) / math.log(1 - golden_ratio))

    x1 = a + golden_ratio * (b - a)
    x2 = b - golden_ratio * (b - a)
    fx1 = f(x1)
    fx2 = f(x2)

    print("| Iteration |     x1     |     x2     |     a      |     b      |   f(x1)   |   f(x2)   |")
    print("|-----------|------------|------------|------------|------------|-----------|-----------|")

    print(f"|    0     |  {x1:.6f}  |  {x2:.6f}  |  {a:.6f}  |  {b:.6f}  | {fx1:.6f} | {fx2:.6f} |")  # Print initial values

    for i in range(iterations):
        if fx1 < fx2:
            b = x2
            x2 = x1
            x1 = a + golden_ratio * (b - a)
            fx2 = fx1
            fx1 = f(x1)
        else:
            a = x1
            x1 = x2
            x2 = b - golden_ratio * (b - a)
            fx1 = fx2
            fx2 = f(x2)

        print(f"|    {i + 1}     |  {x1:.6f}  |  {x2:.6f}  |  {a:.6f}  |  {b:.6f}  | {fx1:.6f} | {fx2:.6f} |")

    if fx1 < fx2:
        return x1
    else:
        return x2

# Get the range of x and the function from the user
try:
    function_str = input("Enter the function to optimize (use 'math' module functions if needed): ")
    a = float(input("Enter the lower bound of the interval (a): "))
    b = float(input("Enter the upper bound of the interval (b): "))
    tolerance = float(input("Enter the tolerance: "))

    # Define the function to optimize using eval()
    def function_to_optimize(x):
        return eval(function_str)

    # Perform Golden Section Search using iteration formula
    result = golden_sec_formula(function_to_optimize, a, b, tolerance)
    if result is not None:
        print(f"Optimal value found within the interval: {result}")
except ValueError:
    print("Error: Please enter valid numerical values for the interval bounds and tolerance.")
