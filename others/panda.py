# coding: utf-8
import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df2 = pd.DataFrame({'A': 1,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'foo'})

print(df.head())
print(df.tail(3))

print(df.describe())

print(df.sort_index(axis=1, ascending=False))
print(df.sort_index(axis=1))
print(df.sort_index(axis=1))
print(df.sort_values(by='B'))

print(df[df.A > 0])
print(df[df.B > 0])
print(df[df > 0])
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
ts.count()
ts.to_csv('foo.csv')
pd.read_csv('foo.csv')
cs = pd.read_csv('foo.csv')
cs.count()
