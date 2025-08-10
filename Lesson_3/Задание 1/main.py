import pandas as pd

orders = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/orders.csv", sep=",")
customers = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/customers.csv", sep=",")
contacts = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/contacts.csv", sep=",")

df = customers.merge(contacts, on='customer_id', how='left')
df = df.merge(orders, on='customer_id', how='inner')  # только те, кто сделал заказ
df['order_date'] = df['order_date'].str.strip()
df['order_date'] = pd.to_datetime(df['order_date'])
europe_russia = ['Italy', 'Spain', 'UK', 'France', 'Germany', 'Russia']
df = df[df['country'].isin(europe_russia)]
df = df[(df['order_date'] >= '2023-01-01') & (df['order_date'] < '2023-07-01')]

print(df[['order_id', 'total']])
print("Сумма продаж:", df['total'].sum())