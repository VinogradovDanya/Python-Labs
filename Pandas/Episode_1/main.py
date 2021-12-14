import pandas as pd

Data = pd.read_csv('transactions.csv', sep=',')
print(Data[Data['STATUS'] == 'OK'].sort_values(by='SUM', ascending=False).head(3))
RealData = Data[Data['STATUS'] == 'OK']
print('Amount of Umbrella =', RealData[RealData['CONTRACTOR'] == 'Umbrella, Inc']['SUM'].sum())
