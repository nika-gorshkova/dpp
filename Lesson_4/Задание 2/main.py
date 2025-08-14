import os
import pandas as pd

home_dir = os.path.expanduser("~")
group_orders_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "group_orders.csv")

df = pd.read_csv(group_orders_path, sep=",")
df['order_date'] = df['order_date'].str.strip()
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

result = df.groupby('city')['total'].mean().round(2).reset_index(name='avg_total')
print('2. Средняя сумма заказа по городам:')
print(result.to_string(index=True))