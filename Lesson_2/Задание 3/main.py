import pandas as pd

df = pd.read_csv("All_Files/products.csv", sep=",", encoding="utf-8")
filtered = df[(df['price'] < 500) & (df['volume_ml'] == 5.0)]
print(filtered[['product_name', 'price']])