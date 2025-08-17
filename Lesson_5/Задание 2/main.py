import pandas as pd

users = pd.read_csv("All_Files/users_new.csv", sep=",", encoding="utf-8")
orders = pd.read_csv("All_Files/orders_new.csv", sep=",", encoding="utf-8")

result = orders.query('product == "C" and price * quantity > 250').copy()
result['total'] = result['price'] * result['quantity']

print(result.to_string(index=True))