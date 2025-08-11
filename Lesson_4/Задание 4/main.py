import pandas as pd

df = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/group_orders.csv", sep=",")
df['order_date'] = df['order_date'].str.strip()
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

df['order_month'] = df['order_date'].dt.to_period('M').astype(str)
result = df.groupby('order_month')['total'].sum().reset_index(name='monthly_revenue')
print('4. Общая выручка по месяцам:')
print(result.to_string(index=True))