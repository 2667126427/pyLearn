import pickle
import pandas as pd


df = pd.DataFrame([['Wang', 29], ['Li', 28]])
df.columns = ['Name', 'Age']

# 哈哈哈，我真没事找事
with open('out.pickle', 'wb') as pickle_out:
    pickle.dump(df, pickle_out)

'''
read operation
data = pd.read_pickle('out.pickle')
print(data.head())
'''
