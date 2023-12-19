
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
#print(data.head())

one_hot_alt = pd.DataFrame()
one_hot_alt["human"] = (data['whoAmI'] == 'human').astype(int)
one_hot_alt["robot"] = (data['whoAmI'] == 'robot').astype(int)

#one_hot_alt = pd.get_dummies(data['whoAmI']).astype(int)

print(one_hot_alt.head())