import pandas as pd

df = pd.read_csv("All_Files/group_orders.csv", sep=",", encoding="utf-8")
df['order_date'] = df['order_date'].str.strip()
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

avg_by_city = df.groupby('city')['total'].mean().reset_index(name='avg_total')
top3 = avg_by_city.sort_values('avg_total', ascending=False).head(3)
print('5. Топ-3 города по средней сумме заказа')
print(top3.to_string(index=True))