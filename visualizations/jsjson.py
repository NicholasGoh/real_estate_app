import json
import pandas as pd
import numpy as np

df = pd.read_csv('transactions.csv')
df = df[df['x'] != -1]
df = df[df['y'] != -1]
df['nettPrice'] = df['nettPrice'].fillna(0)
df = df.astype('object')
df.head()

counter = 1
result = {}
for index in df.index:
    prop = f'property_{index}'
    attributes = df.loc[index].to_dict()
    result[prop] = attributes

with open('transactions.json', 'w') as f:
    json.dump([result], f)
