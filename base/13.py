import math

p = float(input("principal: "))
r = float(input("rate: "))
t = int(input("years: "))
n = int(input("times: "))

res = math.ceil(p*(math.pow(1+r*0.01/n, n*t))*100)/100
print(f"${res}")