import pandas as pd

df = pd.read_csv("All_Files/group_orders.csv", sep=",", encoding="utf-8")
df['order_date'] = df['order_date'].str.strip()
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

result = df.groupby('city')['order_id'].count().reset_index(name='orders_count')
print('1. Кол-во заказов по городам:')
print(result.to_string(index=True))