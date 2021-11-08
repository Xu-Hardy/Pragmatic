tax_rate = 5.5*0.01

prices_list = [ {'index': i, 'price': 0, 'item': 0} for i in range(3)]

for index, price in enumerate(prices_list):
    prices_list[index]['price'] = int(input(f"Enter price of item {index}: "))
    prices_list[index]['item'] = int(input(f"Enter quantity of item {index}: "))

subtotal = sum([i['price']*i['item'] for i in prices_list])
tax = subtotal*tax_rate
total = subtotal + tax

print(f"""
subtotal: {subtotal}
Tax： {tax}
Total： {total}
""")
