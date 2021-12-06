import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame()

print(df)

# Можно взять и нарисовать фрейм
ax = df.plot()
ax.set_xlabel('x label')
ax.set_ylabel('y label')

print("=================")

# А потом посчитать агрегаты
aggr = df.groupby('A').sum()
print(aggr)

# И их тоже нарисовать
ax2 = aggr.plot()

plt.show()
