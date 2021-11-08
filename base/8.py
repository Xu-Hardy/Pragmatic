people = int(input("How many people? "))
pizzas = int(input("How many pizzas do you have? "))

print(f"""
{people} peoples with {pizzas} pizzas.
Each people get {pizzas*8//people} peices.
There are {pizzas*8 % people} peices left.
""")