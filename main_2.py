import pandas as pd
import matplotlib.pyplot as plt


i = ['KZ', 'RU', 'BY', 'UA']

df = pd.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
}, i)

df.index.name = 'country code'

# df.to_csv('main_2.csv')

print(df)
# df.plot()
# plt.show()