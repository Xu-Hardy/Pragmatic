p = float(input("principal: "))
r = float(input("rate: "))
t = int(input("years: "))

res = p*(1+r*0.01*t)

print(f"after {t} years at {r}, it will be ${res}. ")