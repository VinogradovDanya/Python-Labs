import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('flights.csv', sep=',')
count = data['CARGO'].value_counts()
print(count)
group = data.groupby('CARGO')[['PRICE', 'WEIGHT']].sum()
res = group.merge(count, left_index=True, right_index=True)
print(res)

fig, ax = plt.subplots(2, 2, figsize=[10, 10])

ax[0, 0].bar(res.index, res['PRICE'], color='red')
ax[0, 0].set_title('Полная стоимость')
ax[0, 0].grid(axis='y')
ax[0, 1].bar(res.index, res['WEIGHT'], color='magenta')
ax[0, 1].set_title('Полная масса')
ax[0, 1].grid(axis='y')
ax[1, 0].bar(res.index, res['CARGO'], color='green')
ax[1, 0].set_title('Количество рейсов')
ax[1, 0].grid(axis='y')
ax[1, 1].remove()
plt.savefig("res.png")
plt.show()
