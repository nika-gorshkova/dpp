import pandas as pd

orders = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/orders.csv", sep=",")

filtered = orders[(orders['customer_id'].between(10, 20)) & (orders['total'] > 8000)]
print(filtered[['order_id', 'customer_id', 'total']])