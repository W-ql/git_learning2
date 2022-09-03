import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np
from pandas import read_csv
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.metrics import mean_squared_error, r2_score
from pandas import DataFrame
import random
from statsmodels.graphics.tsaplots import *
from statsmodels.tsa import stattools
from brokenaxes import brokenaxes
import statsmodels.api as sm
from statsmodels.tsa.stattools import acf
from statsmodels.tsa.stattools import pacf

series = read_csv('error1.csv',header=0)
data_ = series.values
data = data_[:]
data2 = 1 - data
# plt.figure(figsize=(12,8))   #图形的宽和高
# plt.plot(data2, 'b-+', linewidth=1.0)  # 绘制原始误差序列曲线
# plt.show()
a = []
for i in data:
    a.append(i[0])   #将数组类型转换为列表类型
x = np.array(a)
# plot_acf(x)
# plt.show()
# plot_pacf(x)   #绘制pacf图
# plt.show()


bax = brokenaxes(xlims=((-5,210),),ylims=((-0.3, 0.3), (0.9, 1.02)), hspace=.1, despine=False)
acf_value, acf_interval, _, _ = acf(x, nlags=201, qstat=True, alpha=0.05, fft=False)
acf_value1 = []
for i in range(len(acf_value)):
    if acf_value[i] < 0:
        acf_value1.append(acf_value[i]+0.006)
    elif acf_value[i] > 0:
        acf_value1.append(acf_value[i] - 0.006)
    else:
        acf_value1.append(acf_value[i])
xlabel = np.arange(start=0, stop=acf_value.shape[0], dtype='float')

bax.hlines(y=0, xmin=np.min(xlabel) - 5, xmax=np.max(xlabel) + 10, colors='DodgerBlue', linewidth=1.5)
bax.vlines(x=xlabel, ymin=0, ymax=acf_value1, linewidth=1)
bax.scatter(x=xlabel, y=acf_value,s=15,c='DodgerBlue')     #RoyalBlue

xlabel[1] -= 0.5
xlabel[-1] += 0.5

bax.fill_between(x=xlabel[1:], y1=acf_interval[1:, 0] - acf_value[1:], y2=acf_interval[1:, 1] - acf_value[1:],
                   alpha=0.38, linewidth=0, color='CornflowerBlue')    # CornflowerBlue/RoyalBlue
bax.set_title("Autocorrelation",family='Times New Roman')
# labels1 = [-25,0,25,50,75,100,125,150,175,200]
# bax.set_xticklabels(labels1,family='Times New Roman')
labels1 = bax.get_xticklabels()[1]
[label.set_fontname('Times New Roman') for label in labels1]
labels2 = bax.get_yticklabels()[0]
[label.set_fontname('Times New Roman') for label in labels2]
labels3 = bax.get_yticklabels()[1]
[label.set_fontname('Times New Roman') for label in labels3]
plt.show()

bax = brokenaxes(xlims=((-5,210),),ylims=((-0.3, 0.3), (0.9, 1.02)), hspace=.1, despine=False)
pacf_value, pacf_interval= pacf(x,nlags=201,alpha=0.05,method='ywm')
xlabel = np.arange(start=0, stop=pacf_value.shape[0], dtype='float')
pacf_value1 = []
for i in range(len(pacf_value)):
    if pacf_value[i] < 0:
        pacf_value1.append(pacf_value[i]+0.006)
    elif pacf_value[i] > 0:
        pacf_value1.append(pacf_value[i] - 0.006)
    else:
        pacf_value1.append(pacf_value[i])
bax.hlines(y=0, xmin=np.min(xlabel) - 5, xmax=np.max(xlabel) + 10, colors='DodgerBlue', linewidth=1.5)
bax.vlines(x=xlabel, ymin=0, ymax=pacf_value1,linewidth=1)
bax.scatter(x=xlabel, y=pacf_value, s=15,c='DodgerBlue')
xlabel[1] -= 0.5
xlabel[-1] += 0.5
bax.fill_between(x=xlabel[1:], y1=pacf_interval[1:, 0] - pacf_value[1:], y2=pacf_interval[1:, 1] - pacf_value[1:],
                   alpha=0.38, linewidth=0, color='CornflowerBlue')
bax.set_title("Partial Autocorrelation",family='Times New Roman')
labels1 = bax.get_xticklabels()[1]
[label.set_fontname('Times New Roman') for label in labels1]
labels2 = bax.get_yticklabels()[0]
[label.set_fontname('Times New Roman') for label in labels2]
labels3 = bax.get_yticklabels()[1]
[label.set_fontname('Times New Roman') for label in labels3]
plt.show()


# import statsmodels.api as sm
#
# fig = plt.figure(figsize=(12,8))
# ax1 = fig.add_subplot(211)
# fig = sm.graphics.tsa.plot_acf(x,ax=ax1)
# ax1.set_title("Autocorrelation",family='Times New Roman')
# plt.xticks(family='Times New Roman')
# plt.yticks(family='Times New Roman')
# ax2 = fig.add_subplot(212)
# fig = sm.graphics.tsa.plot_pacf(x,ax=ax2)
# ax2.set_title("Partial Autocorrelation",family='Times New Roman')
# plt.xticks(family='Times New Roman')
# plt.yticks(family='Times New Roman')
# plt.show()


