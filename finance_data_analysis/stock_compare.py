import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 그래프를 노트북 안에 그리기 위해 설정
%matplotlib inline

# 그래프에서 마이너스 폰트 깨지는 문제에 대한 대처
plt.rcParams['axes.unicode_minus'] = False

import pandas_datareader
import datetime
import pandas_datareader.data as web

### 데이터 설정 및 입/출력부분 ###
start = datetime.datetime(2007,1,1)
end = datetime.datetime(2019,9,18)

## 대상 심볼 - LQD
LQD = web.DataReader('LQD', 'yahoo', start, end)
BND = web.DataReader('BND', 'yahoo', start, end)
HYG = web.DataReader('HYG', 'yahoo', start, end)

#차트 출력(시가 기준)
LQD['Open'].plot(label='LQD',figsize=(16,8), title='Open Price')
BND['Open'].plot(label='BND',figsize=(16,8), title='Open Price')
HYG['Open'].plot(label='HYG',figsize=(16,8), title='Open Price')
plt.legend();

#차트 출력( 종가(closing price ) 기준)
LQD['Close'].plot(label='LQD',figsize=(16,8), title='Close Price')
BND['Close'].plot(label='BND',figsize=(16,8), title='Close Price')
HYG['Close'].plot(label='HYG',figsize=(16,8), title='Close Price')
plt.legend();

