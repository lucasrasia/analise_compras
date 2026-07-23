import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('dataset.csv')
print(df.info())

df['quantity'] = df['quantity'].astype(np.float32)
df['shipping_days'] = df['shipping_days'].astype(np.float32)
df['gender']=df['gender'].fillna(df['gender'].mode()[0])  #mode retora uma série, tem q pegar o primeiro termo
df['discount']=df['discount'].fillna(df['discount'].mean())
df['rating']=df['rating'].fillna(df['rating'].mode()[0])  

print(df.info())