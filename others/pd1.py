import datetime

import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 1, 1)
# 好奇怪是怎么读数据的
df = web.DataReader('XOM', 'yahoo', start, end)
print(df.head())
# 输出到plt，已Adj为纵坐标
df['Adj Close'].plot()
# 显示到显示器
plt.show()
