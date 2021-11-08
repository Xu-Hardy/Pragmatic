import math

euros_amount = int(input("Enter euros_amount: "))
euros_rate = float(input("change_rate: "))
usd_rate = 100

usd_amount = euros_amount*euros_rate/usd_rate

print(f"{math.ceil(usd_amount*100)/100} USD")