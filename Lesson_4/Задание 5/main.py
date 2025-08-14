import os
import pandas as pd

home_dir = os.path.expanduser("~")
group_orders_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "group_orders.csv")

df = pd.read_csv(group_orders_path, sep=",")
df['order_date'] = df['order_date'].str.strip()
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

avg_by_city = df.groupby('city')['total'].mean().reset_index(name='avg_total')
top3 = avg_by_city.sort_values('avg_total', ascending=False).head(3)
print('5. Топ-3 города по средней сумме заказа')
print(top3.to_string(index=True))