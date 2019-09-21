import pandas as pd


list = [1, 2, 3, 4, 5]
i = [2, 3, 4, 5, 6]
indexes = ['a', 'b', 'c', 'd', 'e']

s1 = pd.Series(list, i)
# s1[[2, 5, "a"]] = 0
# s1 = s1[s1 > 4] * 2
s1.index = i

print(s1)
