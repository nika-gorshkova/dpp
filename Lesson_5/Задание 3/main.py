import pandas as pd

users = pd.read_csv("All_Files/users_new.csv", sep=",", encoding="utf-8")
orders = pd.read_csv("All_Files/orders_new.csv", sep=",", encoding="utf-8")

counts = orders['product'].value_counts()
result = counts.rename_axis('product').reset_index(name='order_count')
print(result.to_string(index=True))