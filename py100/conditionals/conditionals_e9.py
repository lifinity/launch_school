# logical conditions 3
sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")

# prints $3.99; not sale -> not True -> False -> falsy
# branches to 3.99, sale would have to be falsy for 5.25