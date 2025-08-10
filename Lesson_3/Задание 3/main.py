import pandas as pd

orders = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/orders.csv", sep=",")
customers = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/customers.csv", sep=",")

orders['order_date'] = orders['order_date'].str.strip()
orders['order_date'] = pd.to_datetime(orders['order_date'])

orders = orders[(orders['order_date'].dt.year >= 2022) & (orders['order_date'].dt.year <= 2023)]

df = customers.merge(orders, on='customer_id', how='inner')
print(df['gender'].value_counts())