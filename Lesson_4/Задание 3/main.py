import pandas as pd

df = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/group_orders.csv", sep=",")
df['order_date'] = df['order_date'].str.strip()
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

qty_by_product = df.groupby('product')['quantity'].sum().reset_index(name='total_quantity')
max_row = qty_by_product.sort_values('total_quantity', ascending=False).head(1)
print('3. Самый популярный товар по количеству:')
print(max_row.to_string(index=False))