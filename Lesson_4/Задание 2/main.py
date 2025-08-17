import pandas as pd

df = pd.read_csv("All_Files/group_orders.csv", sep=",", encoding="utf-8")
df['order_date'] = df['order_date'].str.strip()
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

result = df.groupby('city')['total'].mean().round(2).reset_index(name='avg_total')
print('2. Средняя сумма заказа по городам:')
print(result.to_string(index=True))