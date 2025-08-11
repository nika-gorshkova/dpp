import pandas as pd

users = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/users_new.csv", sep=",")
orders = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/orders_new.csv", sep=",")

counts = orders['product'].value_counts()
result = counts.rename_axis('product').reset_index(name='order_count')
print(result.to_string(index=True))