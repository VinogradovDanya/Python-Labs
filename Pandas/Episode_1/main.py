import numpy as np
import pandas as pd

data = pd.read_csv('transactions.csv', sep=',')
print(data[data['STATUS'] == 'OK'].sort_values(by='SUM', ascending=False).head(3))
RealData = data[data['STATUS'] == 'OK']
print('Amount of Umbrella =', RealData[RealData['CONTRACTOR'] == 'Umbrella, Inc']['SUM'].sum())
print(data.head())
