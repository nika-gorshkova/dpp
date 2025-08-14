import os
import pandas as pd

home_dir = os.path.expanduser("~")
products_path = os.path.join(home_dir, "Downloads", "ДПП Питон", "All_Files", "products.csv")

df = pd.read_csv(products_path, sep=",")
filtered = df[(df['price'] < 500) & (df['volume_ml'] == 5.0)]
print(filtered[['product_name', 'price']])