import pandas as pd

df = pd.read_csv("C:/Users/user/Downloads/ДПП Питон/All_Files/products.csv", sep=",")
filtered = df[(df['price'] < 500) & (df['volume_ml'] == 5.0)]
print(filtered[['product_name', 'price']])