import math

length = int(input("input length: "))
width = int(input("input width: "))

square = length*width
square_per_gallon = 350

res = math.ceil(square/square_per_gallon)

print(res)

