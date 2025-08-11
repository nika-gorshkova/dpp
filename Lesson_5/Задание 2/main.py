import pandas as pd

users = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/users_new.csv", sep=",")
orders = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/orders_new.csv", sep=",")

result = orders.query('product == "C" and price * quantity > 250').copy()
result['total'] = result['price'] * result['quantity']

print(result.to_string(index=True))