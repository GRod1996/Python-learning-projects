temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}
print(temps.keys())
print(temps.values())
print(len(temps))

colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
print("===Colors of Fruits===")
for name, color in colors.items():
    print(f"The {name} is {color}")

total_sum = 0
prices = {"laptop": 999, "phone": 699, "tablet": 499, "watch": 299}
for ind_price in prices.values():
    total_sum += ind_price
print(total_sum)
